from data.assignment_tests.example4 import *
import pytest
import sys

# Mocking sys.argv to simulate command line arguments for testing
sys.argv = ['test_tertiary.py']

def test_tertiary_true_path():
    # Test when x == 42 and y == 2007
    assert tertiary(42, 2007) == 1

def test_tertiary_false_path():
    # Test when x != 42
    assert tertiary(43, 2007) == 3

def test_tertiary_true_path_else():
    # Test when x == 42 and y != 2007
    assert tertiary(42, 2008) == 2

def test_tertiary_false_path_else():
    # Test when x != 42 and y != 2007
    assert tertiary(43, 2008) == 3

def test_tertiary_edge_case_x():
    # Test edge case when x is not an integer
    with pytest.raises(TypeError):
        tertiary('42', 2007)

def test_tertiary_edge_case_y():
    # Test edge case when y is not an integer
    with pytest.raises(TypeError):
        tertiary(42, '2007')

def test_tertiary_edge_case_x_and_y():
    # Test edge case when both x and y are not integers
    with pytest.raises(TypeError):
        tertiary('42', '2007')

def test_tertiary_edge_case_x_none():
    # Test edge case when x is None
    with pytest.raises(TypeError):
        tertiary(None, 2007)

def test_tertiary_edge_case_y_none():
    # Test edge case when y is None
    with pytest.raises(TypeError):
        tertiary(42, None)

def test_tertiary_edge_case_x_and_y_none():
    # Test edge case when both x and y are None
    with pytest.raises(TypeError):
        tertiary(None, None)

if __name__ == "__main__":
    pytest.main()