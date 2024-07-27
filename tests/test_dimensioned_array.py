import pytest

import numpy as np

import dimpy as dp


@pytest.fixture
def basis():
    basis = dp.Basis(("meter", "second", "kilogram"))
    return basis


@pytest.fixture
def codomain(basis):
    # fmt: off
    cod = np.array([[1,  0, 0],
                    [1, -1, 0],
                    [1, -2, 0],
                    [1,  0, 1]])
    # fmt: on
    codomain = dp.Dvec(cod, basis)
    return codomain


@pytest.fixture
def domain(basis):
    # fmt: off
    dom = np.array([[1, 0, 0],
                    [0, 0, 1]])
    # fmt: on
    domain = dp.Dvec(dom, basis)
    return domain


@pytest.fixture
def arr_4by4(codomain, domain):
    matnum = np.arange(8).reshape(4, 2)
    mat = dp.Darray(matnum, codomain, domain)
    return mat


@pytest.fixture
def arr_2(domain):
    vecnum = np.array([1, 2])
    vec = dp.Darray(vecnum, domain)
    return vec


# TODO: This should go in a separate file. This file should be for Darray tests.
class TestUfuncs:
    def test_add(self, arr_2):
        assert np.allclose((arr_2 + arr_2).num, np.array([2, 4]))
