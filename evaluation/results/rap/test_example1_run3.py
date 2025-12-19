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
    example1.foo(10, 10)

def test_4():
    example1.foo(10, 5)

def test_5():
    example1.bar(10, 10, 3)

def test_6():
    example1.bar(10, 5, 1)

def test_7():
    example1.bar(5, 10, 1)

def test_data_assignment_tests_example1_2():
    assert example1.bar(1, 2, 3) == 1

def test_18():
    assert example1.bar(10, 20, 5) == 20
