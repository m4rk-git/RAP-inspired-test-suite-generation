from data.assignment_tests.example1 import *
import pytest
import sys

# Test suite for foo function
def test_foo():
    # Test case 1: x == 42 and y == 0
    assert foo(42, 0) == 1
    # Test case 2: x == 42 and y != 0
    assert foo(42, 1) == 0
    # Test case 3: x != 42
    assert foo(43, 0) == -1
    # Test case 4: Edge case - x == 42 and y == 0
    assert foo(42, 0) == 1
    # Test case 5: Edge case - x == 42 and y != 0
    assert foo(42, 1) == 0
    # Test case 6: Edge case - x != 42
    assert foo(43, 0) == -1

# Test suite for bar function
def test_bar():
    # Test case 1: (x + y) / 2 > z
    assert bar(10, 20, 5) == 5
    # Test case 2: (x + y) / 3 < z and x > y
    assert bar(10, 5, 20) == 10
    # Test case 3: (x + y) / 3 < z and x < y
    assert bar(5, 10, 20) == 10
    # Test case 4: (x + y) / 3 < z and x == y
    assert bar(5, 5, 20) == 5
    # Test case 5: Edge case - (x + y) / 2 > z
    assert bar(10, 20, 5) == 5
    # Test case 6: Edge case - (x + y) / 3 < z and x > y
    assert bar(10, 5, 20) == 10
    # Test case 7: Edge case - (x + y) / 3 < z and x < y
    assert bar(5, 10, 20) == 10
    # Test case 8: Edge case - (x + y) / 3 < z and x == y
    assert bar(5, 5, 20) == 5

# Run the test suite
if __name__ == "__main__":
    pytest.main(sys.argv)