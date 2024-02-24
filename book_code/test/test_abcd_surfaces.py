"""These tests focus on testing individual children of abcd.ABCD"""
import math

import pytest

from ..ch2 import abcd
from ..ch2 import equations


def test_transfer():
    t = 10e-3
    n = 1.5
    trans = abcd.Transfer(t, n)
    assert trans.B == t / n


def test_refraction():
    n1 = 1
    n2 = 1.5
    R = 50
    refr = abcd.Refraction(R, n1, n2)
    assert refr.n1 == n1
    assert refr.n2 == n2
    assert refr.f1 == R / (n2 - n1)  # air-side
    assert refr.f2 == R / (n2 - n1) * n2  # glass-side


def test_refraction_nonzero_AOI():
    R = 100e-3
    n = 1.5
    AOI = 0.1
    AOE = math.asin(math.sin(AOI) / n)
    C1 = math.cos(AOI)
    C2 = math.cos(AOE)
    M = C2 / C1

    surface = abcd.Refraction(R, 1, n, AOI, "T")
    dne = (n * C2 - C1) / (C1 * C2)
    assert surface.A == pytest.approx(M)
    assert surface.B == 0
    assert surface.C == -dne / R
    assert surface.D == pytest.approx(1 / M)

    surface = abcd.Refraction(R, 1, n, AOI, "S")
    dne = n * C2 - C1
    assert surface.A == 1
    assert surface.B == 0
    assert surface.C == -dne / R
    assert surface.D == 1

    surface = abcd.Refraction(math.inf, 1, n, AOI, "T")
    assert surface.C == 0

    surface = abcd.Refraction(math.inf, 1, n, AOI, "S")
    assert surface.C == 0


def test_mirror():
    R = 50
    refl = abcd.Mirror(R)
    assert refl.n1 == 1
    assert refl.n2 == 1
    assert refl.A == 1
    assert refl.B == 0
    assert refl.C == 2 / R
    assert refl.D == 1


def test_mirror_nonzero_AOI():
    R = 100e-3
    AOI = 0.1

    surface = abcd.Mirror(R, AOI=AOI, T_or_S="T")
    Re = R * math.cos(AOI)
    assert surface.A == 1
    assert surface.B == 0
    assert surface.C == 2 / Re
    assert surface.D == 1

    surface = abcd.Mirror(R, AOI=AOI, T_or_S="S")
    Re = R / math.cos(AOI)
    assert surface.A == 1
    assert surface.B == 0
    assert surface.C == 2 / Re
    assert surface.D == 1

    surface = abcd.Mirror(math.inf, AOI=AOI, T_or_S="T")
    assert surface.C == 0

    surface = abcd.Mirror(math.inf, AOI=AOI, T_or_S="S")
    assert surface.C == 0


def test_duct():
    # Short duct is thin lens with B=z/n0 and C=-n2*z
    duct = abcd.Duct(1e-9, 1, 10e9)
    approx_thin_lens = abcd.ABCD(1, 1e-9, -1 / 100e-3, 1)
    assert duct.A == pytest.approx(approx_thin_lens.A)
    assert duct.B == pytest.approx(approx_thin_lens.B)
    assert duct.C == pytest.approx(approx_thin_lens.C)
    assert duct.D == pytest.approx(approx_thin_lens.D)


def test_grating():
    # Based on a Thorlabs grating in Littrow geometry
    λ0 = 500e-9  # blaze wavelength 500 nm
    d = 1e-3 / 1200  # 1200 lp/mm
    AOI = math.radians(17 + 27 / 60)  # blaze angle
    AOE = math.radians(
        equations.diffraction_angle(
            λ0 * 1e6, d * 1e6, math.degrees(AOI)
        )
    )
    C1 = math.cos(AOI)
    C2 = math.cos(AOE)
    M = C2 / C1

    R = math.inf
    Rt = 2 * R * C1 * C2 / (C1 + C2)
    Rs = 2 * R / (C1 + C2)

    grating = abcd.Grating(R=R, d=d, wavelength=λ0, AOI=AOI, T_or_S="T")
    assert grating.A == M
    assert grating.B == 0
    assert grating.C == 0
    assert grating.D == 1 / M

    grating = abcd.Grating(R=R, d=d, wavelength=λ0, AOI=AOI, T_or_S="S")
    assert grating.A == 1
    assert grating.B == 0
    assert grating.C == 2 / Rs
    assert grating.D == 1

    R = 100e-3
    Rt = 2 * R * C1 * C2 / (C1 + C2)
    Rs = 2 * R / (C1 + C2)

    grating = abcd.Grating(R=R, d=d, wavelength=λ0, AOI=AOI, T_or_S="T")
    assert grating.A == M
    assert grating.B == 0
    assert grating.C == 2 / Rt
    assert grating.D == 1 / M

    grating = abcd.Grating(R=R, d=d, wavelength=λ0, AOI=AOI, T_or_S="S")
    assert grating.A == 1
    assert grating.B == 0
    assert grating.C == 2 / Rs
    assert grating.D == 1


def test_thin_lens():
    f = 25e-3
    thin = abcd.ThinLens(f)
    assert thin.f1 == thin.f2 == f
    assert thin.A == thin.D == 1
    assert thin.B == 0
    assert thin.C == -1 / f
