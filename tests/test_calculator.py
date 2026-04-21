from mlops_practice.calculator import add
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
