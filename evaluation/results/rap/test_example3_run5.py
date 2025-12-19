import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example3 as example3
from data.assignment_tests.example3 import *


def test_data_assignment_tests_example3_1():
    example3.intersect(0, 0, 1, 1, 1, 1, 0, 0)

def test_4():
    example3.intersect(0, 0, 1, 2, 2, 0, 2, 1)

def test_6():
    example3.intersect(0, 0, 2, 0, 0, 2, 1, 1)

def test_8():
    example3.intersect(0, 0, 2, 2, 2, 0, 0, 2)

def test_11_13():
    example3.intersect(0, 0, 1, 1, 0, 0, 1, 1)

def test_15_20():
    example3.intersect(0, 0, 1, 1, 0, 0, 3, 3)

def test_22_26():
    example3.intersect(0, 0, 1, 1, 1, 1, 2, 2)

def test_data_assignment_tests_example3_2():
  result = example3.intersect(0, 0, 1, 1, 1, 0, 0, 1)
  assert result == True

def test_data_assignment_tests_example3_3(example3):
    assert example3.intersect(0, 0, 1, 1, 1, 0, 0, 1) == True
def test_2(example3):
    assert example3.intersect(0, 0, 1, 1, 1, 1, 0, 0) == True
def test_3(example3):
    assert example3.intersect(0, 0, 1, 1, 0, 0, 1, 1) == True

def test_data_assignment_tests_example3_4():
    assert example3.intersect(0, 0, 1, 1, 0, 1, 1, 0) == True

def test_data_assignment_tests_example3_5():
    # Add your code here to make the interpreter execute lines 24-26 of SOURCE_CODE
    assert example3.intersect(0, 0, 1, 1, 0, 0, 1, 0) == True

def test_data_assignment_tests_example3_6():
    assert example3.intersect(0, 0, 1, 1, 0, 1, 1, 0)

def test_25():
    assert example3.intersect(0, 0, 0, 1, 0, 1, 1, 0)

def test_26():
    assert example3.intersect(0, 0, 0, 0, 0, 1, 1, 0)

def test_data_assignment_tests_example3_7():
    return example3.intersect(0,0,0,1,1,0,1,1)
