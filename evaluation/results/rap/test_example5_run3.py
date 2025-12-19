import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example5 as example5
from data.assignment_tests.example5 import *


def test_data_assignment_tests_example5_1():
    assert example5.collection(42, 50, 33)

def test_2():
    assert example5.collection(1038472, 50, 99)

def test_3():
    assert not example5.collection(3817, 101, 66)

def test_4():
    assert not example5.collection(3817, -1, 66)

def test_5():
    assert not example5.collection(1038472, 0, 66)

def test_data_assignment_tests_example5_2():
    example5.collection(42, 50, 33) 

def test_11():
    example5.collection(42, 0, 33)

def test_data_assignment_tests_example5_3():
    assert not example5.collection(42, 50, 22)
