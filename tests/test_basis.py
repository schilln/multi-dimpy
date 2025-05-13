import pytest

from dimpy import Basis


@pytest.fixture
def basis():
    """`Basis` instance with m = 3."""
    return Basis(("m", "s", "kg"))


@pytest.fixture
def basis_other():
    """`Basis` instance with m = 3, with different units."""
    return Basis(("m", "kg", "s"))


def test_equal(basis):
    assert basis == basis


def test_not_equal(basis, basis_other):
    assert basis != basis_other


def test_not_equal_not_basis(basis):
    assert not basis == 1
    assert basis != 1


def test_no_units():
    with pytest.raises(ValueError):
        Basis(tuple())


def test_units_not_strings():
    with pytest.raises(ValueError):
        Basis(("m", 1))
