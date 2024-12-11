from numb3rs import validate

def test_one():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True

def test_two():
    assert validate("cat") == False
    assert validate("1.2.3.256") == False
    assert validate("256.0.0.0") == False
    assert validate("259.1546.654.321") == False
