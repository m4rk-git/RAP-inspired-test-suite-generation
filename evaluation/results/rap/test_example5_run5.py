import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example5 as example5
from data.assignment_tests.example5 import *


def test_data_assignment_tests_example5_1():
    assert not example5.collection(1038472, 200, 33)

def test_2():
    assert not example5.collection(42, 100, 33)

def test_3():
    assert not example5.collection(1038472, 0, 33)

def test_4():
    assert not example5.collection(42, 100, 99)

def test_5():
    assert not example5.collection(1038472, 200, 66)

def test_6():
    assert not example5.collection(42, 100, 0)

def test_7():
    assert not example5.collection(1038472, 200, 99)

def test_8():
    assert not example5.collection(42, 100, 66)

def test_data_assignment_tests_example5_2():
    example5.collection(1038472, 50, 66)

def test_data_assignment_tests_example5_3(): return example5.collection(42, 50, 33)

def test_data_assignment_tests_example5_4():
    assert example5.collection(42, 10, 33) == True

def test_11():
    assert example5.collection(43, 10, 32) == False
