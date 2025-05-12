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
def arr_2(domain):
    num = np.array([1, 2])
    vec = Darray(num, domain)
    return vec
