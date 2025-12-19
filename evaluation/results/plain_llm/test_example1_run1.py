from data.assignment_tests.example1 import *
import pytest
from typing import *

# Test suite for the code

# Test cases for function foo
def test_foo_x_42_y_0():
    assert foo(42, 0) == 1

def test_foo_x_42_y_not_0():
    assert foo(42, 1) == 0

def test_foo_x_not_42():
    assert foo(43, 0) == -1

# Test cases for function bar
def test_bar_x_greater_than_y_and_avg_greater_than_z():
    assert bar(5, 3, 2) == 2

def test_bar_x_greater_than_y_and_avg_less_than_z():
    assert bar(5, 3, 4) == 5

def test_bar_x_less_than_y_and_avg_greater_than_z():
    assert bar(3, 5, 2) == 3

def test_bar_x_less_than_y_and_avg_less_than_z():
    assert bar(3, 5, 4) == 5

def test_bar_x_equal_to_y():
    assert bar(5, 5, 3) == 5

# Test cases for edge cases
def test_foo_edge_case_x_42_y_0():
    assert foo(42, 0) == 1

def test_foo_edge_case_x_42_y_not_0():
    assert foo(42, 1) == 0

def test_foo_edge_case_x_not_42():
    assert foo(43, 0) == -1

def test_bar_edge_case_x_greater_than_y_and_avg_greater_than_z():
    assert bar(5, 3, 2) == 2

def test_bar_edge_case_x_greater_than_y_and_avg_less_than_z():
    assert bar(5, 3, 4) == 5

def test_bar_edge_case_x_less_than_y_and_avg_greater_than_z():
    assert bar(3, 5, 2) == 3

def test_bar_edge_case_x_less_than_y_and_avg_less_than_z():
    assert bar(3, 5, 4) == 5

def test_bar_edge_case_x_equal_to_y():
    assert bar(5, 5, 3) == 5

# Run the test suite
if __name__ == "__main__":
    pytest.main()