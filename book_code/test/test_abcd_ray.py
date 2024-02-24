import numbers

import pytest

from ..ch2 import abcd


def test_ray_construction():
    r = abcd.Ray()
    assert isinstance(r, abcd.Ray)
    assert isinstance(r.y, numbers.Number)
    assert isinstance(r.u, numbers.Number)


def test_types():
    mat = abcd.ABCD()
    ray = abcd.Ray()
    assert isinstance(ray, abcd.Ray)
    assert isinstance(mat @ ray, abcd.Ray)


def test_explicit_update():
    y = 1
    u = 0.1
    f = 10e-3
    ray = abcd.Ray(y, u)
    mtx = abcd.ABCD(C=-1 / f) @ abcd.ABCD(B=f)
    ray = mtx @ ray
    assert ray.y == pytest.approx(y + u * f)
    assert ray.u == pytest.approx(-1 / f)


def test_inplace_update():
    y = 1
    u = 0.1
    f = 10e-3
    ray = abcd.Ray(y, u)
    mtx = abcd.ABCD(C=-1 / f) @ abcd.ABCD(B=f)
    ray @= mtx
    assert ray.y == pytest.approx(y + u * f)
    assert ray.u == pytest.approx(-1 / f)


def test_ray_angles_across_interface():
    m = 0.1
    n = 1.5

    marginal = abcd.Ray(0, m)
    chief = abcd.Ray(1, 0)

    assert marginal.y == 0
    assert marginal.u == m
    assert chief.y == 1
    assert chief.u == 0

    interface = abcd.ABCD(n2=n)
    marginal @= interface
    chief @= interface
    assert marginal.y == 0
    assert marginal.u == pytest.approx(m / n)
    assert chief.y == pytest.approx(1)
    assert chief.u == pytest.approx(0)
    assert marginal.n == chief.n == n


def test_multiple_ray_updates():
    m = 0.1
    L = 50e-3
    n = 1.5
    R = L / 2

    marginal = abcd.Ray(0, m)
    chief = abcd.Ray(1, 0)

    fs = abcd.ABCD(B=L)
    marginal @= fs
    chief @= fs
    assert marginal.y == pytest.approx(L * m)
    assert marginal.u == m
    assert chief.y == 1
    assert chief.u == 0

    refr = abcd.ABCD(C=-(n - 1) / R, n2=n)
    marginal @= refr
    chief @= refr
    assert marginal.y == pytest.approx(L * m)
    assert marginal.u == pytest.approx(0)
    assert chief.y == pytest.approx(1)
    assert chief.u == pytest.approx(-(n - 1) / (n * R))
    assert marginal.n == chief.n == n

    L_focus = n * R / (n - 1)  # solved (L/n mtx)(y nu) for y == 0
    fs = abcd.ABCD(B=L_focus / n, n1=n, n2=n)
    marginal @= fs
    chief @= fs
    assert marginal.y == pytest.approx(L * m)
    assert marginal.u == pytest.approx(0)
    assert chief.y == pytest.approx(0)
    assert chief.u == pytest.approx(-(n - 1) / (n * R))
    assert marginal.n == chief.n == n

    to_air = abcd.ABCD(n1=n, n2=1)
    marginal @= to_air
    chief @= to_air
    assert marginal.y == pytest.approx(L * m)
    assert marginal.u == pytest.approx(0)
    assert chief.y == pytest.approx(0)
    assert chief.u == pytest.approx(-(n - 1) / R)
    assert marginal.n == chief.n == 1

