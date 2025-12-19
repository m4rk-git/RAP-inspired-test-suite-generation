import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example4 as example4
from data.assignment_tests.example4 import *


def test_data_assignment_tests_example4_1():
    result = example4.tertiary(42, 2007)
    assert result == 1

def test_non_2007_check():
    result = example4.tertiary(42, 2006)
    assert result == 2

def test_non_42_check():
    result = example4.tertiary(41, 2007)
    assert result == 3
