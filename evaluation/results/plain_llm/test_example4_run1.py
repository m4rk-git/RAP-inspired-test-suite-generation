from data.assignment_tests.example4 import *
import pytest
import sys

# Mocking sys.argv to handle command line arguments
sys.argv = ['test_tertiary.py']

def test_tertiary_x_42_y_2007():
    assert tertiary(42, 2007) == 1

def test_tertiary_x_42_y_not_2007():
    assert tertiary(42, 2008) == 2

def test_tertiary_x_not_42_y_2007():
    assert tertiary(43, 2007) == 3

def test_tertiary_x_not_42_y_not_2007():
    assert tertiary(43, 2008) == 3

def test_tertiary_x_42_y_2007_edge_case():
    assert tertiary(42, 2007) == 1

def test_tertiary_x_42_y_not_2007_edge_case():
    assert tertiary(42, 2008) == 2

def test_tertiary_x_not_42_y_2007_edge_case():
    assert tertiary(43, 2007) == 3

def test_tertiary_x_not_42_y_not_2007_edge_case():
    assert tertiary(43, 2008) == 3

if __name__ == "__main__":
    pytest.main()