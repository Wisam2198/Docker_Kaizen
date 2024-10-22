# tests/test_conversion.py
from conversion import convert_currency

def test_convert_currency():
    assert convert_currency(100, 'USD', 'EUR', 0.85) == 85.0
