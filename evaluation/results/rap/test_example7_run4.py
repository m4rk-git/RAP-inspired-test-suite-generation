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
    example7.sum_of_even(2)

def test_5():
    example7.sum_of_even(3)
