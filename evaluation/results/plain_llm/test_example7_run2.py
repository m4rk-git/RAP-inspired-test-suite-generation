from data.assignment_tests.example7 import *
import pytest
import sys

# Test cases for the sum_of_even function
def test_sum_of_even_positive():
    assert sum_of_even(5) == 6, "Test case for positive input failed"

def test_sum_of_even_zero():
    assert sum_of_even(0) == 0, "Test case for zero input failed"

def test_sum_of_even_negative():
    assert sum_of_even(-3) == 0, "Test case for negative input failed"

def test_sum_of_even_one():
    assert sum_of_even(1) == 0, "Test case for input 1 failed"

def test_sum_of_even_even_number():
    assert sum_of_even(6) == 12, "Test case for even number input failed"

def test_sum_of_even_odd_number():
    assert sum_of_even(7) == 12, "Test case for odd number input failed"

def test_sum_of_even_large_number():
    assert sum_of_even(100) == 2450, "Test case for large number input failed"

def test_sum_of_even_max_int():
    assert sum_of_even(sys.maxsize) == (sys.maxsize // 2) * (sys.maxsize // 2), "Test case for max int input failed"

def test_sum_of_even_min_int():
    assert sum_of_even(-sys.maxsize - 1) == 0, "Test case for min int input failed"

# Run the tests
if __name__ == "__main__":
    pytest.main()