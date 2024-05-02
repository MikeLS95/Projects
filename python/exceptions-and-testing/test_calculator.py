from calculator import add, subtract, division
import pytest

def test_basic():
    assert add(1, 2) == 3
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 2) == 8
    assert subtract(-5, -15) == 10

def test_division():
    assert division(10, 2) == 5
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)