import math

import pytest

from ..ch2 import equations


def test_rayleigh_resolution():
    λ = 0.532  # μm
    fno = 10
    ref_value = 1.22 * λ * fno  # μm
    calc_value = equations.rayleigh_resolution(λ, fno)
    assert calc_value == pytest.approx(ref_value)


def test_diffraction_angle_normal():
    λ = 0.532  # μm
    Δ = 1  # μm
    ref_value = -32.140687
    calc_value = equations.diffraction_angle(λ, Δ)
    assert calc_value == pytest.approx(ref_value)


def test_diffraction_angle_angled():
    λ = 0.532  # μm
    Δ = 1  # μm
    angle = 10
    ref_value = -20.99901
    calc_value = equations.diffraction_angle(λ, Δ, angle)
    assert calc_value == pytest.approx(ref_value)


def test_diffraction_angle_order():
    λ = 0.532  # μm
    Δ = 1  # μm
    angle = 10
    order = -2
    ref_value = -62.91749
    calc_value = equations.diffraction_angle(λ, Δ, angle, order)
    assert calc_value == pytest.approx(ref_value)


# TODO: check for different index
def test_fiber_coupling():
    # in μm
    λ = 1.55
    w1 = 5
    w2 = 5
    ref_value = 1
    calc_value = equations.fiber_coupling_efficiency(λ, w1, w2)
    assert calc_value == pytest.approx(ref_value)


def test_fiber_coupling_extremes():
    # in μm
    λ = 1.55
    w1 = 5
    w2 = 5
    ref_value = 0
    calc_value = equations.fiber_coupling_efficiency(
        λ, w1, w2, transverse=1e3
    )
    assert calc_value == pytest.approx(ref_value)

    calc_value = equations.fiber_coupling_efficiency(
        λ, w1, w2, longitudinal=1e12
    )
    assert calc_value == pytest.approx(ref_value)

    calc_value = equations.fiber_coupling_efficiency(
        λ, w1, w2, angular=90
    )
    assert calc_value == pytest.approx(ref_value)


def test_critical_angle():
    ref_value = 30
    calc_value = equations.critical_angle(2)
    assert calc_value == pytest.approx(ref_value)


def test_NA_from_indices():
    from ..ch2 import materials
    test_NA = 0.1
    n_core = materials.fs7980(0.532)
    n_cladding = (n_core**2 - test_NA**2)**0.5
    NA = equations.NA_from_indices(n_core, n_cladding)
    assert NA == pytest.approx(test_NA)



def test_fresnel_reflection():
    n = 1.5
    rho = equations.fresnel_reflection(1, n)
    assert rho**2 == pytest.approx(0.04)

    θ1 = 10
    θ2 = math.degrees(math.asin(math.sin( math.radians(θ1) ) / n))  # Snel's law

    rho = equations.fresnel_reflection(1, 1.5, θ1, S_or_P='P')
    nt1 = 1 / math.cos(math.radians(θ1))
    nt2 = n / math.cos(math.radians(θ2))
    rho_explicit = (nt1 - nt2) / (nt1 + nt2)
    assert rho**2 == pytest.approx(rho_explicit**2)

    rho = equations.fresnel_reflection(1, 1.5, θ1, S_or_P='S')
    nt1 = math.cos(math.radians(θ1))
    nt2 = n * math.cos(math.radians(θ2))
    rho_explicit = (nt1 - nt2) / (nt1 + nt2)
    assert rho**2 == pytest.approx(rho_explicit**2)


# tests for each q_from_X_X function
def test_q_from_Rw():
    R = 10e-3
    w = 1e-3
    λ0 = 532e-9
    n = 1.5
    q = equations.q_from_R_w(R, w, wavelength=λ0, n=n)
    assert 1 / ((1 / q).real / n) == pytest.approx(R)
    assert 1 / math.sqrt(
        -(1 / q).imag * math.pi / λ0
    ) == pytest.approx(w)


def test_q_from_zzR():
    z = 10e-3
    zR = 1e-3
    n = 1.5
    q = equations.q_from_z_zR(z, zR, n=n)
    assert q.real * n == pytest.approx(z)
    assert q.imag * n == pytest.approx(zR)


def test_q_from_Rz():
    R = 10e-3
    z = 1e-3
    n = 1.5
    q = equations.q_from_R_z(R, z, n=n)
    assert 1 / ((1 / q).real / n) == pytest.approx(R)
    assert q.real * n == pytest.approx(z)

    with pytest.raises(ValueError):
        q = equations.q_from_R_z(R=1, z=1, n=n)
    with pytest.raises(ValueError):
        q = equations.q_from_R_z(R=1, z=2, n=n)
    with pytest.raises(ValueError):
        q = equations.q_from_R_z(R=1, z=0, n=n)


def test_q_from_RzR():
    R = 10e-3
    zR = 1e-3
    n = 1.5
    sign = 1
    q = equations.q_from_R_zR(R, zR, n=n, sign=sign)
    assert 1 / ((1 / q).real / n) == pytest.approx(R)
    assert q.imag * n == pytest.approx(zR)

    with pytest.raises(ValueError):
        q = equations.q_from_R_zR(R=1, zR=0.500001, n=n)

    z1 = q.real * n
    sign = -1
    q = equations.q_from_R_zR(R, zR, n=n, sign=sign)
    z2 = q.real * n
    assert z1 < z2


def test_q_from_wz():
    w = 1e-3
    z = 10e-3
    λ0 = 532e-9
    n = 1.5
    sign = 1
    q = equations.q_from_w_z(w, z, wavelength=λ0, n=n, sign=sign)
    assert 1 / math.sqrt(
        -(1 / q).imag * math.pi / λ0
    ) == pytest.approx(w)
    assert q.real * n == pytest.approx(z)

    with pytest.raises(ValueError):
        q = equations.q_from_w_z(
            w=1, z=n * math.pi / λ0 * 1.0001, n=n
        )
    with pytest.raises(ValueError):
        q = equations.q_from_w_z(
            w=-1, z=-n * math.pi / λ0 * 1.0001, n=n
        )

    zR1 = q.imag * n
    sign = -1
    q = equations.q_from_w_z(w, z, wavelength=λ0, n=n, sign=sign)
    zR2 = q.real * n
    assert zR1 > zR2


def test_q_from_wzR():
    w = 1e-3
    zR = 1e-3
    λ0 = 532e-9
    n = 1.5
    sign = 1
    q = equations.q_from_w_zR(w, zR, wavelength=λ0, n=n, sign=sign)
    assert 1 / math.sqrt(
        -(1 / q).imag * math.pi / λ0
    ) == pytest.approx(w)
    assert q.imag * n == pytest.approx(zR)

    with pytest.raises(ValueError):
        q = equations.q_from_w_zR(
            w=1, zR=n * math.pi / λ0 * 1.0001, n=n
        )

    z1 = q.real * n
    sign = -1
    q = equations.q_from_w_zR(w, zR, wavelength=λ0, n=n, sign=sign)
    z2 = q.real * n
    assert z1 == -z2


def test_doublet_equation():
    from ..ch2 import materials
    λC = 0.6563  # µm
    λD = 0.5893  # µm
    λF = 0.4861  # µm

    na = materials.nbk7(λD)
    nb = materials.nsf5(λD)

    va = (materials.nbk7(λD) - 1) / (materials.nbk7(λF) - materials.nbk7(λC))
    vb = (materials.nsf5(λD) - 1) / (materials.nsf5(λF) - materials.nsf5(λC))

    EFL = 100e-3
    solutions = equations.achromatic_doublet(EFL, na, va, nb, vb)
    assert len(solutions[0]) == 4
    assert len(solutions[1]) == 4
    assert round(solutions[0]['C2'], 1) == round(solutions[0]['C3'], 1)

