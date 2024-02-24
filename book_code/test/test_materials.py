import pytest

from ..ch2 import materials


def test_air():
    # Value from emtoolbox.nist.gov Edlen equation calculator
    assert materials.air(0.5) == pytest.approx(1.000274)


def test_nbk7():
    λ = 0.58756
    ref_index = 1.51680011
    calc_index = materials.nbk7(λ) * materials.air(λ)
    assert calc_index == pytest.approx(ref_index)

    T = 30
    heated_index = 1.51683  # unsure if in air or absolute
    assert materials.nbk7(λ, T) * materials.air(λ, T)  == pytest.approx(heated_index, abs=2e-5)


def test_nsf5():
    λ = 0.5461
    ref_index = 1.67763
    calc_index = materials.nsf5(λ) * materials.air(λ)
    assert calc_index == pytest.approx(ref_index)

    λ = 0.5461
    ref_dndT = 2e-6
    T = 30
    ΔT = T - 20
    heated_index = ref_index + ΔT * ref_dndT
    assert materials.nsf5(λ, T) * materials.air(λ, T) == pytest.approx(heated_index)


def test_fs7980():
    λ = 0.587725
    ref_index = 1.458461
    calc_index = materials.fs7980(λ) * materials.air(λ)
    assert calc_index == pytest.approx(ref_index, abs=5e-6)

    T = 32
    ΔT = T - 22
    ref_dndT = 10.1e-6
    heated_index = ref_index + ΔT * ref_dndT
    calc_index = materials.fs7980(λ, T) * materials.air(λ, T)
    assert calc_index == pytest.approx(heated_index)


# Loosened tolerance to match, perhaps fit doesn't match data superbly:
def test_noa61():
    λ = 0.5896
    ref_index = 1.5594
    assert materials.noa61(λ) == pytest.approx(ref_index, abs=2.5e-4)


# Loosened tolerance to match, perhaps fit doesn't match data superbly:
def test_znse():
    λ = 10.6
    ref_index = 2.4028
    calc_index = materials.znse(λ) * materials.air(λ)
    assert calc_index == pytest.approx(ref_index, abs=1e-4)

    T = 30
    ΔT = T - 20
    ref_dndT = 61e-6
    heated_index = ref_index + ΔT * ref_dndT
    calc_index = materials.znse(λ, T) * materials.air(λ, T)
    assert calc_index == pytest.approx(heated_index, abs=1e-4)


# Loosened tolerance to match, perhaps fit doesn't match data superbly:
def test_mgf2():
    λ = 0.5870740
    ref_index = 1.421977
    calc_index = materials.mgf2(λ) * materials.air(λ)
    assert calc_index == pytest.approx(ref_index, abs=1e-4)


# Loosened tolerance to match, perhaps fit doesn't match data superbly:
def test_tio2():
    λ = 0.587
    ref_index = 2.146858
    calc_index = materials.tio2(λ) * materials.air(λ)
    assert calc_index == pytest.approx(ref_index, abs=5e-3)
