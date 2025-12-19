import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example5 as example5
from data.assignment_tests.example5 import *


def test_data_assignment_tests_example5_1():
    assert example5.collection(42, 50, 33)

def test_02():
    assert not example5.collection(42, 50, 66)

def test_03():
    assert not example5.collection(42, 50, 99)

def test_04():
    assert not example5.collection(42, 50, 100)

def test_05():
    assert not example5.collection(42, -1, 33)

def test_06():
    assert not example5.collection(42, 101, 33)

def test_07():
    assert not example5.collection(42, 50, 1038472)

def test_08():
    assert not example5.collection(3817, 50, 33)

def test_09():
    assert not example5.collection(1038472, 50, 33)

def test_10():
    assert not example5.collection(1, 50, 33)
