from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    with pytest.raises(ValueError):
        convert("7/6")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
