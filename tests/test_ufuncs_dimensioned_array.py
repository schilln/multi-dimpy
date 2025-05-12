import pytest

import numpy as np

from dimpy import Basis, Dvec, Darray


@pytest.fixture
def basis():
    basis = Basis(("meter", "second", "kilogram"))
    return basis


@pytest.fixture
def codomain(basis):
    # fmt: off
    cod = np.array([[1,  0, 0],
                    [1, -1, 0],
                    [1, -2, 0],
                    [1,  0, 1]])
    # fmt: on
    codomain = Dvec(cod, basis)
    return codomain


@pytest.fixture
def domain(basis):
    # fmt: off
    dom = np.array([[1, 0, 0],
                    [0, 0, 1]])
    # fmt: on
    domain = Dvec(dom, basis)
    return domain


@pytest.fixture
def arr_4by4(codomain, domain):
    num = np.arange(8).reshape(4, 2)
    mat = Darray(num, (codomain, domain))
    return mat


@pytest.fixture
def arr_1d(domain):
    num = np.array([1, 2])
    vec = Darray(num, domain)
    return vec


class Test_Positive:
    def test_1d(self, arr_1d):
        assert np.allclose((+arr_1d).num, np.array([1, 2]))


class Test_Negative:
    def test_1d(self, arr_1d):
        assert np.allclose((-arr_1d).num, np.array([-1, -2]))


class Test_Add:
    def test_1d(self, arr_1d):
        assert np.allclose((arr_1d + arr_1d).num, np.array([2, 4]))


class Test_Subtract:
    def test_1d(self, arr_1d):
        assert np.allclose((arr_1d - arr_1d).num, np.array([0, 0]))


class Test_Multiply:
    @pytest.mark.parametrize(
        "scalar, expected",
        [
            (2, np.array([2, 4])),
            (-1, np.array([-1, -2])),
        ],
    )
    def test_scalar_dimensionless(self, arr_1d, scalar, expected):
        assert np.allclose((arr_1d * scalar).num, expected)
        assert np.allclose((scalar * arr_1d).num, expected)
