from datetime import date
from seasons import get_date

def test():
    assert get_date("1999-01-01") == date(1999, 1, 1)
