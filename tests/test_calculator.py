from mlops_practice.calculator import add, divide
import pytest


def test_add_positive_numbers():
    assert add(1, 2) == 3


def test_add_negative_numbers():
    assert add(-1, -2) == -3


def test_add_zeros():
    assert add(0, 0) == 0


def test_add_strings():
    with pytest.raises(TypeError):
        add("hello", "world")


def test_divide_normal():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_divide_floats():
    assert divide(1, 2) == 0.5
