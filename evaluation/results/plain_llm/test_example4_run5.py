from data.assignment_tests.example4 import *
import pytest
from unittest.mock import patch

def test_tertiary_true_path():
    with patch('builtins.input', return_value='42'):
        assert tertiary(42, 2007) == 1

def test_tertiary_false_path():
    with patch('builtins.input', return_value='43'):
        assert tertiary(43, 2007) == 3

def test_tertiary_true_path_false_condition():
    with patch('builtins.input', return_value='42'):
        assert tertiary(42, 2008) == 2

def test_tertiary_false_path_true_condition():
    with patch('builtins.input', return_value='43'):
        assert tertiary(43, 2007) == 3

def test_tertiary_false_path_false_condition():
    with patch('builtins.input', return_value='43'):
        assert tertiary(43, 2008) == 3