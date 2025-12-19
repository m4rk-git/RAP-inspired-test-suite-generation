import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example7 as example7
from data.assignment_tests.example7 import *


def test_data_assignment_tests_example7_1():
    example7.sum_of_even(5)

def test_data_assignment_tests_example7_2():
    result = example7.sum_of_even(1)

def test_data_assignment_tests_example7_3():
    example7.sum_of_even(1)

def test_data_assignment_tests_example7_4(self):
    example7.sum_of_even(0)

def test_data_assignment_tests_example7_5():
    assert example7.sum_of_even(5) == 6

def test_data_assignment_tests_example7_6():
    assert example7.sum_of_even(0) == 0
