"""These tests focus on testing abcd.ABCD"""
import math

import pytest

from ..ch2 import abcd


def test_zero_handling():
    identity = abcd.ABCD()
    assert identity.C == 0
    assert identity.f1 == math.inf


def test_abcd_equality():
    identity_1 = abcd.ABCD()
    identity_2 = abcd.ABCD()
    other = abcd.ABCD(B=1)
    assert identity_2 == identity_2
    assert identity_1 != other


def test_matrix_multiplication():
    identity = abcd.ABCD()
    mtx1 = abcd.ABCD(1, 0, -1 / 10e-3, 1)
    mtx2 = abcd.ABCD(1, 5e-3, 0, 1)
    assert identity == (identity @ identity)
    assert mtx1 @ mtx2 != mtx2 @ mtx1


def test_matrix_multiplication_inplace():
    identity = abcd.ABCD()
    mtx1 = abcd.ABCD(1, 0, -1 / 10e-3, 1)
    mtx2 = abcd.ABCD(1, 5e-3, 0, 1)
    # Logic is: add an mtx1, then an mtx2, etc...
    identity @= mtx1
    identity @= mtx2
    assert identity == (mtx2 @ mtx1)


def test_types():
    mat = abcd.ABCD()
    assert isinstance(mat, abcd.ABCD)


def test_ABCD_case_A0():
    # A == 0 --> inf-to-focus
    ray_set = [abcd.Ray(n / 10) for n in range(11)]
    f = 10e-3
    mtx = abcd.ABCD(B=f) @ abcd.ABCD(C=-1 / f)
    assert mtx.A == pytest.approx(0)
    for ray in ray_set:
        output = mtx @ ray
        assert output.y == pytest.approx(0)

    ray_set = [abcd.Ray(n / 10, 0.1) for n in range(11)]
    for ray in ray_set:
        output = mtx @ ray
        assert output.y == pytest.approx(0.1 * f)


def test_ABCD_case_B0():
    # B == 0 --> finite conjugate imaging
    ray_set = [abcd.Ray(0, n / 100) for n in range(11)]
    f = 10e-3
    mtx = (
        abcd.ABCD(B=2 * f) @ abcd.ABCD(C=-1 / f) @ abcd.ABCD(B=2 * f)
    )
    assert mtx.B == pytest.approx(0)
    for ray in ray_set:
        output = mtx @ ray
        assert output.y == pytest.approx(ray.y)
        assert output.u == pytest.approx(-ray.u)

    ray_set = [abcd.Ray(1, n / 100) for n in range(11)]
    for ray in ray_set:
        output = mtx @ ray
        assert output.y == pytest.approx(-ray.y)


def test_ABCD_case_C0():
    # C == 0 --> afocal
    ray_set = [abcd.Ray(n / 10) for n in range(11)]
    f = 10e-3
    mtx = (
        abcd.ABCD(C=-1 / (2 * f))
        @ abcd.ABCD(B=3 * f)
        @ abcd.ABCD(C=-1 / f)
    )
    assert mtx.C == pytest.approx(0)
    for ray in ray_set:
        output = mtx @ ray
        assert output.y == pytest.approx(-2 * ray.y)

    ray_set = [abcd.Ray(n / 10, 0.1) for n in range(11)]
    for ray in ray_set:
        output = mtx @ ray
        assert output.u == pytest.approx(-ray.u / 2)


def test_ABCD_case_D0():
    # D == 0 --> collimator
    ray_set = [abcd.Ray(0, n / 10) for n in range(11)]
    f = 10e-3
    mtx = abcd.ABCD(C=-1 / f) @ abcd.ABCD(B=f)
    assert mtx.D == pytest.approx(0)
    for ray in ray_set:
        output = mtx @ ray
        assert output.u == pytest.approx(0)
    ray_set = [abcd.Ray(1, n / 10) for n in range(11)]
    for ray in ray_set:
        output = mtx @ ray
        assert output.u == pytest.approx(-1 / f)

# TODO: add a few more pedantic and hard-coded edge cases
# e.g. displacement and matrix multiplication
def test_augmented_matrix():
    perturb = -0.1
    n = 1.5
    f = 100e-3
    axis = abcd.Ray()
    marginal = abcd.Ray(0, 0.1)
    chief = abcd.Ray(1, 0)

    offset = abcd.ThinLens(f, decenter=perturb)
    tilt = abcd.Refraction(math.inf, 1, n, tilt=perturb)

    for ray in (axis, marginal, chief):
        before = ray

        after = offset @ ray
        assert after.y == before.y
        assert after.u == before.u + perturb / f - before.y / f

        after = tilt @ ray
        assert after.y == before.y
        assert after.u == (before.u + perturb * (n - 1)) / n


def test_explicit_thin_lens():
    focal_length = 25
    lens = abcd.ABCD(1, 0, -1 / focal_length, 1)

    assert lens.f1 == focal_length  # focal length calculation
    assert lens.f1 == lens.f2  # lens is in air
    assert lens.P1 == lens.P2  # principal planes superimposed
    assert lens.F1 == -lens.F2  # required by planes and fs
    assert lens.N1 == -lens.N2


def test_curved_face():
    radius = 50
    index = 1.5
    face = abcd.ABCD(1, 0, -(index - 1) / radius, 1, n2=index)

    assert face.P1 == face.P2  # principal planes superimposed
    assert face.n1 == 1  # in air
    assert face.n2 == index  # glass-side
    assert face.f1 == radius / (index - 1)  # air-side
    assert face.f2 == radius / (index - 1) * index  # glass-side
