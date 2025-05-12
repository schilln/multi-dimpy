import pytest

import numpy as np

from dimpy import Basis, Dvec, Darray


@pytest.fixture
def basis():
    basis = Basis(("meter", "second", "kilogram"))
    return basis


@pytest.fixture
def basis_other():
    """`Basis` instance with m = 3, with different units."""
    return Basis(("m", "kg", "s"))


@pytest.fixture
def dvec0(basis):
    # fmt: off
    vec = np.array([[1, 0, 1],
                    [0, 1, 1]])
    # fmt: on
    dvec = Dvec(vec, basis)
    return dvec


@pytest.fixture
def dvec1(basis):
    # fmt: off
    vec = np.array([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]])
    # fmt: on
    dvec = Dvec(vec, basis)
    return dvec


@pytest.fixture
def dvec_other_basis(basis_other):
    # fmt: off
    vec = np.array([[1, 0, 1],
                    [0, 1, 1]])
    # fmt: on
    dvec = Dvec(vec, basis_other)
    return dvec


def test_construction(dvec0, dvec1):
    num = np.arange(2 * 3).reshape(2, 3)
    Darray(num, (dvec0, dvec1))


def test_basis(dvec0, basis):
    num = np.array([1, 2])
    assert Darray(num, (dvec0,)).basis == basis


def test_not_num(dvec0):
    num = 1
    with pytest.raises(ValueError):
        Darray(num, (dvec0,))


def test_not_dvec(dvec0):
    num = np.array([1, 2])
    not_dvec = 1
    with pytest.raises(ValueError):
        Darray(num, (dvec0, not_dvec))


def test_num_dvecs_mismatch(dvec0, dvec1):
    num = np.arange(2 * 3 * 4).reshape(2, 3, 4)
    with pytest.raises(ValueError):
        Darray(num, (dvec0, dvec1))


def test_dvecs_dimension_mismatch(dvec0, dvec1):
    num = np.arange(2 * 4).reshape(2, 4)
    with pytest.raises(ValueError):
        Darray(num, (dvec0, dvec1))


def test_basis_mismatch(dvec0, dvec_other_basis):
    num = np.arange(2 * 2).reshape(2, 2)
    with pytest.raises(ValueError):
        Darray(num, (dvec0, dvec_other_basis))
