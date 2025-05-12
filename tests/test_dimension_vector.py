import pytest

import numpy as np

import dimpy as dp
from dimpy import Dvec, DvecType


@pytest.fixture
def basis():
    """`Basis` instance with m = 3."""
    return dp.Basis(("m", "s", "kg"))


@pytest.fixture
def basis_m_equals_2():
    """`Basis` instance with m = 2."""
    return dp.Basis(("m", "s"))


@pytest.fixture
def vector_m_equals_2():
    """Numerical component of `Dvec` with m = 2."""
    # fmt: off
    return np.array([[0, 1],
                     [2, 3]])
    # fmt: on


@pytest.fixture
def vector_dimensionless():
    # fmt: off
    return np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
    # fmt: on


@pytest.fixture
def vector_1d():
    return np.array([0, 1, 2])


@pytest.fixture
def vector_uniform():
    # fmt: off
    return np.array([[-1, 1, 0],
                     [-1, 1, 0],
                     [-1, 1, 0]])
    # fmt: on


@pytest.fixture
def vector_ratioed():
    # fmt: off
    return np.array([[-1, 1, 0],
                     [-2, 2, 0],
                     [-3, 3, 0]])
    # fmt: on


@pytest.fixture
def vector_uniform_n_equals_2():
    # fmt: off
    return np.array([[0, 1, 0],
                     [0, 1, 0]])
    # fmt: on


@pytest.fixture
def vector_ratioed_n_equals_2():
    # fmt: off
    return np.array([[0, 1, 0],
                     [0, 3, 0]])
    # fmt: on


@pytest.fixture
def vector_arbitrary():
    # fmt: off
    return np.array([[-1, 1, 0],
                     [-2, 2, 1],
                     [-3, 3, -1]])
    # fmt: on


@pytest.fixture
def vector_ndim_greater_than_2():
    """Numerical component of `Dvec` with ndim > 2."""
    return np.arange(2 * 3 * 4).reshape(2, 3, 4)


def test_mismatch_vector_basis(vector_m_equals_2, basis):
    with pytest.raises(ValueError):
        Dvec(vector_m_equals_2, basis)


def test_dvec_basis_equals_basis(vector_1d, basis):
    dvec = Dvec(vector_1d, basis)
    assert dvec.basis == basis


def test_ndim_equals_1(vector_1d, basis):
    dvec = Dvec(vector_1d, basis)
    assert dvec.n == 1
    assert dvec.m == 3


def test_ndim_greater_than_2(
    vector_ndim_greater_than_2,
    basis,
):
    with pytest.raises(ValueError):
        Dvec(vector_ndim_greater_than_2, basis)


def test_dimensionless(vector_dimensionless, basis):
    dvec = Dvec(vector_dimensionless, basis)
    assert dvec.vectype == DvecType.DIMENSIONLESS


@pytest.mark.parametrize(
    "vector_fixture",
    [
        "vector_uniform",
        "vector_uniform_n_equals_2",
    ],
)
def test_uniform(vector_fixture, basis, request):
    vector = request.getfixturevalue(vector_fixture)
    dvec = Dvec(vector, basis)
    assert dvec.vectype == DvecType.UNIFORM


@pytest.mark.parametrize(
    "vector_fixture",
    [
        "vector_ratioed",
        "vector_ratioed_n_equals_2",
    ],
)
def test_ratioed(vector_fixture, basis, request):
    vector = request.getfixturevalue(vector_fixture)
    dvec = Dvec(vector, basis)
    assert dvec.vectype == DvecType.RATIOED


def test_arbitrary(vector_arbitrary, basis):
    dvec = Dvec(vector_arbitrary, basis)
    assert dvec.vectype == DvecType.ARBITRARY


def test_add(vector_uniform, vector_ratioed, basis):
    dvec_left = Dvec(vector_uniform, basis)
    dvec_right = Dvec(vector_ratioed, basis)

    assert dvec_left + dvec_right == Dvec(
        np.array([[-2, 2, 0], [-3, 3, 0], [-4, 4, 0]]), basis
    )


def test_add_unequal_n(vector_uniform, vector_uniform_n_equals_2, basis):
    dvec_left = Dvec(vector_uniform, basis)
    dvec_right = Dvec(vector_uniform_n_equals_2, basis)

    with pytest.raises(ValueError):
        dvec_left + dvec_right


def test_add_unequal_basis(
    vector_uniform_n_equals_2, basis, vector_m_equals_2, basis_m_equals_2
):
    dvec_left = Dvec(vector_uniform_n_equals_2, basis)
    dvec_right = Dvec(vector_m_equals_2, basis_m_equals_2)

    with pytest.raises(ValueError):
        dvec_left + dvec_right


def test_add_not_Dvec(vector_uniform, basis):
    dvec = Dvec(vector_uniform, basis)

    with pytest.raises(TypeError):
        dvec + 1


def test_subtract_not_Dvec(vector_uniform, basis):
    dvec = Dvec(vector_uniform, basis)

    with pytest.raises(TypeError):
        dvec - 1


def test_subtract(vector_uniform, vector_ratioed, basis):
    dvec_left = Dvec(vector_uniform, basis)
    dvec_right = Dvec(vector_ratioed, basis)

    assert dvec_left - dvec_right == Dvec(
        np.array([[0, 0, 0], [1, -1, 0], [2, -2, 0]]), basis
    )


def test_equal_not_Dvec(vector_uniform, basis):
    dvec = Dvec(vector_uniform, basis)

    assert not dvec == 1
    assert dvec != 1
