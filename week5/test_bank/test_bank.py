from bank import value

def test_one():
    assert value("HeLLoooo") == 0
    assert value("Hello, there") == 0

def test_two():
    assert value("Hey!") == 20
    assert value("HOW ARE YOU?") == 20

def test_three():
    assert value("This is CS50") == 100
