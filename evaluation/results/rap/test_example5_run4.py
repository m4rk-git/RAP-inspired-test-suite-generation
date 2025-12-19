import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example5 as example5
from data.assignment_tests.example5 import *


def test_data_assignment_tests_example5_1():
    return example5.collection(42, 50, 66)

def test_02():
    return example5.collection(42, 500, 99)

def test_03():
    return example5.collection(3817, 0, 33)

def test_04():
    return example5.collection(3817, 100, 66)

def test_05():
    return example5.collection(1038472, 50, 99)

def test_06():
    return example5.collection(1038472, 500, 66)

def test_07():
    return example5.collection(1038472, 0, 99)

def test_08():
    return example5.collection(1038472, 100, 33)

def test_09():
    return example5.collection(42, 500, 999)

def test_10():
    return example5.collection(3817, 50, 999)

def test_11():
    return example5.collection(1038472, 50, 999)

def test_data_assignment_tests_example5_2():
    example5.collection(3817, 99, 123)

def test_data_assignment_tests_example5_3():
  example5.collection(1, 2, 3)
