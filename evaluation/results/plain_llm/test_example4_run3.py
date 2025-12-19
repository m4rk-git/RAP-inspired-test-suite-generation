from data.assignment_tests.example4 import *
import pytest
from typing import *

# Test cases for the tertiary function
def test_tertiary_x_is_42_y_is_2007():
    assert tertiary(42, 2007) == 1

def test_tertiary_x_is_42_y_is_not_2007():
    assert tertiary(42, 2008) == 2

def test_tertiary_x_is_not_42_y_is_2007():
    assert tertiary(43, 2007) == 3

def test_tertiary_x_is_not_42_y_is_not_2007():
    assert tertiary(43, 2008) == 3

# Test cases for edge cases
def test_tertiary_x_is_42_y_is_2007_edge_case():
    assert tertiary(42, 2007) == 1

def test_tertiary_x_is_42_y_is_not_2007_edge_case():
    assert tertiary(42, 2008) == 2

def test_tertiary_x_is_not_42_y_is_2007_edge_case():
    assert tertiary(43, 2007) == 3

def test_tertiary_x_is_not_42_y_is_not_2007_edge_case():
    assert tertiary(43, 2008) == 3

# Test cases for invalid input types
def test_tertiary_invalid_input_types():
    with pytest.raises(TypeError):
        tertiary("42", 2007)
    with pytest.raises(TypeError):
        tertiary(42, "2007")
    with pytest.raises(TypeError):
        tertiary("42", "2007")

# Test cases for invalid input values
def test_tertiary_invalid_input_values():
    with pytest.raises(ValueError):
        tertiary(42, 2007)
    with pytest.raises(ValueError):
        tertiary(42, 2008)
    with pytest.raises(ValueError):
        tertiary(43, 2007)
    with pytest.raises(ValueError):
        tertiary(43, 2008)

# Test cases for edge cases with invalid input types
def test_tertiary_invalid_input_types_edge_case():
    with pytest.raises(TypeError):
        tertiary("42", 2007)
    with pytest.raises(TypeError):
        tertiary(42, "2007")
    with pytest.raises(TypeError):
        tertiary("42", "2007")

# Test cases for edge cases with invalid input values
def test_tertiary_invalid_input_values_edge_case():
    with pytest.raises(ValueError):
        tertiary(42, 2007)
    with pytest.raises(ValueError):
        tertiary(42, 2008)
    with pytest.raises(ValueError):
        tertiary(43, 2007)
    with pytest.raises(ValueError):
        tertiary(43, 2008)

# Test cases for edge cases with invalid input types and values
def test_tertiary_invalid_input_types_and_values_edge_case():
    with pytest.raises(TypeError):
        tertiary("42", 2007)
    with pytest.raises(TypeError):
        tertiary(42, "2007")
    with pytest.raises(TypeError):
        tertiary("42", "2007")
    with pytest.raises(ValueError):
        tertiary(42, 2007)
    with pytest.raises(ValueError):
        tertiary(42, 2008)
    with pytest.raises(ValueError):
        tertiary(43, 2007)
    with pytest.raises(ValueError):
        tertiary(43, 2008)