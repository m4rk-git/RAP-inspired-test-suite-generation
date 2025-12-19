import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example5 as example5
from data.assignment_tests.example5 import *


def test_data_assignment_tests_example5_1():
    assert example5.collection(42, -50, 33) == False

def test_4th_array():
    assert example5.collection(3817, 50, 99) == False

def test_5th_array():
    assert example5.collection(1038472, 50, 66) == True
    assert example5.collection(1038472, 50, 99) == False

def test_7th_array():
    assert example5.collection(42, 100, 66) == False

def test_9th_array():
    assert example5.collection(42, 100, 33) == False

def test_11th_array():
    assert example5.collection(42, 0, 33) == False

def test_data_assignment_tests_example5_2():
    assert example5.collection(42, 10, 99)

def test_11():
    assert not example5.collection(100, 50, 66)

def test_data_assignment_tests_example5_3(example5):
    result = example5.collection(3817, 50, 66)
    assert result is False

def test_data_assignment_tests_example5_4():
  assert example5.collection(1038472, 50, 33) == True

def test_data_assignment_tests_example5_5():
    assert example5.collection(42, 50, 33) == True

def test_data_assignment_tests_example5_6():
    result = example5.collection(42, 50, 33)
    assert result == True

def test_7_false():
    result = example5.collection(42, 50, 99)
    assert result == False

def test_data_assignment_tests_example5_7():
    assert not example5.collection(42, 50, 25)
