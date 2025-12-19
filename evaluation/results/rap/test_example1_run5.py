import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example1 as example1
from data.assignment_tests.example1 import *


def test_data_assignment_tests_example1_1():
    example1.foo(42, 0)
def test_2():
    example1.foo(42, 1)
def test_3():
    example1.bar(57, 20, 18)
def test_4():
    example1.bar(30, 20, 10)
def test_5():
    example1.bar(20, 10, 30)

def test_data_assignment_tests_example1_2():
    assert example1.foo(42, 0) == 1

def test_ensure_line_18_is_executed():
    assert example1.bar(10, 5, 2) == 5

def test_data_assignment_tests_example1_3():
    result = example1.foo(43, 0)
    assert result == -1

def test_2():
    result = example1.bar(1, 1, 0)
    assert result == 1

def test_data_assignment_tests_example1_4():
    return example1.foo(42, 1)

def test_18():
    return example1.bar(1, 2, -1)

def test_data_assignment_tests_example1_5(example1):
    result = example1.bar(10, 20, 30)
    return result

def test_data_assignment_tests_example1_6():
    result = example1.bar(20, 10, 3)
    assert result == 10

def test_data_assignment_tests_example1_7():
    assert example1.bar(1, 2, 3) == 2
