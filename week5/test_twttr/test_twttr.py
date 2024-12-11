from twttr import shorten

def test_shorten():
    assert shorten("HELLO, FRIEND") == ("HLL, FRND")
    assert shorten("This Is CS50 PYTHON") == "Ths s CS50 PYTHN"
    assert shorten("Pi = 3.14") == "P = 3.14"
