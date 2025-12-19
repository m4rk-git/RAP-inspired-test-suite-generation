import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example4 as example4
from data.assignment_tests.example4 import *


def test_data_assignment_tests_example4_1():
    assert example4.tertiary(42, 2007) == 1

def test_42_2008():
    assert example4.tertiary(42, 2008) == 2

def test_not_42_2007():
    assert example4.tertiary(43, 2007) == 3

def test_not_42_2008():
    assert example4.tertiary(43, 2008) == 3

def test_42_not_2007():
    assert example4.tertiary(42, 2000) == 3

def test_42_not_2008():
    assert example4.tertiary(42, 2001) == 3
