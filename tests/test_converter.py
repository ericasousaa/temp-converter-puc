import pytest
from app import f_to_c

def test_freezing_point():
    assert f_to_c(32) == 0

def test_boiling_point():
    assert f_to_c(212) == 100

def test_negative_temp():
    assert round(f_to_c(-40), 2) == -40.00

def test_typical_value():
    assert round(f_to_c(100), 2) == 37.78

def test_large_value():
    assert round(f_to_c(1000), 2) == 537.78
