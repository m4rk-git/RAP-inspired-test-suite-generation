import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example1 as example1
from data.assignment_tests.example1 import *


def test_data_assignment_tests_example1_1():
    assert example1.bar(5, 3, 4) == 5

def test_data_assignment_tests_example1_2(example1):
    assert example1.bar(0,-1,-1) == -1

def test_2(example1):
    assert example1.bar(0,0,0) == 0

def test_3(example1):
    assert example1.bar(0,1,0) == 1

def test_4(example1):
    assert example1.bar(0,0,-2) == 0

def test_5(example1):
    assert example1.bar(0,1,-2) == 1

def test_6(example1):
    assert example1.bar(-1,0,-2) == 0

def test_7(example1):
    assert example1.bar(-1,0,-1) == -1

def test_8(example1):
    assert example1.bar(-2,-1,-2) == -1

def test_9(example1):
    assert example1.bar(-2,-2,-2) == -2

def test_10(example1):
    assert example1.bar(-1,-1,-2) == -1

def test_11(example1):
    assert example1.bar(0,1,-1) == 1

def test_12(example1):
    assert example1.bar(0,1,-2) == 1

def test_13(example1):
    assert example1.bar(0,1,-2) == 1

def test_14(example1):
    assert example1.bar(0,0,-1) == -1

def test_15(example1):
    assert example1.bar(0,0,-2) == 0

def test_16(example1):
    assert example1.bar(0,1,-2) == 1

def test_17(example1):
    assert example1.bar(-1,0,-2) == 0

def test_18(example1):
    assert example1.bar(-2,-1,-2) == -1

def test_19(example1):
    assert example1.bar(-2,-2,-2) == -2

def test_20(example1):
    assert example1.bar(-1,-1,-2) == -1

def test_21(example1):
    assert example1.bar(0,1,-1) == 1

def test_22(example1):
    assert example1.bar(0,1,-2)

def test_data_assignment_tests_example1_3():
    assert example1.foo(42, 0) == 1
    assert example1.foo(42, 1) == 0
    assert example1.foo(43, 0) == -1
    assert example1.bar(1, 2, 0) == 0
    assert example1.bar(2, 1, 3) == 2
    assert example1.bar(3, 2, 4) == 2
