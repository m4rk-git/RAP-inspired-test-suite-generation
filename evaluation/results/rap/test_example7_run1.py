import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example7 as example7
from data.assignment_tests.example7 import *


def test_data_assignment_tests_example7_1():
    example7.sum_of_even(-1)

def test_2():
    example7.sum_of_even(0)

def test_3():
    example7.sum_of_even(1)

def test_4():
    result = example7.sum_of_even(10)
    assert result == 20

def test_5():
    result = example7.sum_of_even(2)
    assert result == 0

def test_6():
    result = example7.sum_of_even(5)
    assert result == 6

def test_7():
    result = example7.sum_of_even(7)
    assert result == 12

def test_8():
    result = example7.sum_of_even(9)
    assert result == 20
