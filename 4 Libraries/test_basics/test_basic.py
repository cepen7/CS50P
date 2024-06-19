import pytest


def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Can't divide by zero")


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(2, 0)
