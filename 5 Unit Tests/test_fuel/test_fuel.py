from fuel import (convert,
                  gauge
)
import pytest

def test_convert_rounding():
    assert convert("1/3") == 33


def test_convert_full():
    assert convert("5/5") == 100


def test_convert_empty():
    assert convert("0/5") == 0


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_zero_spilt_gas():
    with pytest.raises(ValueError):
        convert("5/4")


def test_gauge_empty():
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"


def test_gauge_middle():
    assert gauge(50) == "50%"



