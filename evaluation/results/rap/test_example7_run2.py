import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example7 as example7
from data.assignment_tests.example7 import *


def test_data_assignment_tests_example7_1():
    assert example7.sum_of_even(1) == 0

def test_2_should_execute_line_2():
    assert example7.sum_of_even(-1) == 0

def test_3_should_execute_line_3():
    assert example7.sum_of_even(0) == 0

def test_4_should_execute_line_5():
    assert example7.sum_of_even(2) == 0

def test_5_should_execute_line_9():
    assert example7.sum_of_even(3) == 2
