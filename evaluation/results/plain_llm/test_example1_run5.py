from data.assignment_tests.example1 import *
import pytest
import sys

# Test suite for the code

# Test cases for function foo
def test_foo_x_42_y_0():
    assert foo(42, 0) == 1

def test_foo_x_42_y_non_0():
    assert foo(42, 1) == 0

def test_foo_x_not_42():
    assert foo(43, 0) == -1

# Test cases for function bar
def test_bar_x_greater_than_y():
    assert bar(5, 3, 2) == 2

def test_bar_x_less_than_y():
    assert bar(3, 5, 2) == 5

def test_bar_average_greater_than_z():
    assert bar(5, 3, 1) == 1

def test_bar_average_less_than_z_and_x_greater_than_y():
    assert bar(5, 3, 4) == 5

def test_bar_average_less_than_z_and_x_less_than_y():
    assert bar(3, 5, 4) == 3

# Test edge cases
def test_foo_edge_cases():
    assert foo(42, sys.maxsize) == 0
    assert foo(42, -sys.maxsize) == 0
    assert foo(43, sys.maxsize) == -1
    assert foo(43, -sys.maxsize) == -1

def test_bar_edge_cases():
    assert bar(sys.maxsize, 0, sys.maxsize) == sys.maxsize
    assert bar(0, sys.maxsize, sys.maxsize) == sys.maxsize
    assert bar(sys.maxsize, sys.maxsize, sys.maxsize) == sys.maxsize
    assert bar(-sys.maxsize, -sys.maxsize, -sys.maxsize) == -sys.maxsize
    assert bar(sys.maxsize, -sys.maxsize, sys.maxsize) == sys.maxsize
    assert bar(-sys.maxsize, sys.maxsize, -sys.maxsize) == -sys.maxsize

# Run the test suite
if __name__ == "__main__":
    pytest.main()