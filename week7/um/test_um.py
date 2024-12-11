from um import count

def test_one():
    assert count("um") == 1
    assert count("UM") == 1

def test_two():
    assert count("Um?") == 1

def test_three():
    assert count("Um,thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
