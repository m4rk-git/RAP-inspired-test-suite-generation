from data.assignment_tests.example4 import *
import pytest
from unittest.mock import patch

def test_tertiary_true_true():
    with patch('builtins.input', return_value='42'):
        with patch('builtins.input', return_value='2007'):
            assert tertiary(42, 2007) == 1

def test_tertiary_true_false():
    with patch('builtins.input', return_value='42'):
        with patch('builtins.input', return_value='2008'):
            assert tertiary(42, 2008) == 2

def test_tertiary_false_true():
    with patch('builtins.input', return_value='43'):
        with patch('builtins.input', return_value='2007'):
            assert tertiary(43, 2007) == 3

def test_tertiary_false_false():
    with patch('builtins.input', return_value='43'):
        with patch('builtins.input', return_value='2008'):
            assert tertiary(43, 2008) == 3

def test_tertiary_edge_cases():
    assert tertiary(42, 2007) == 1
    assert tertiary(42, 2008) == 2
    assert tertiary(43, 2007) == 3
    assert tertiary(43, 2008) == 3