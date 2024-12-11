from jar import Jar
import pytest

def test_init():
    j = Jar(12)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.deposit(555)


def test_withdraw():
    jar = Jar(4)
    with pytest.raises(ValueError):
        jar.withdraw(5)
