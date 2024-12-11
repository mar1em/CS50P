from working import convert
import pytest

def test_one():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("5 PM to 12 AM") == "17:00 to 00:00"

def test_two():
    assert convert("9:00 AM to 4 PM") == "09:00 to 16:00"
    assert convert("12 AM to 1:35 PM") == "00:00 to 13:35"

def test_three():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
