from plates import is_valid

def test_one():
    assert is_valid("H") == False
    assert is_valid("GOODBYE") == False
    assert is_valid("HELLO") == True

def test_two():
    assert is_valid("CS 50") == False

def test_three():
    assert is_valid("88") == False
    assert is_valid("8TT") == False
def test_four():
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

