import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example3 as example3
from data.assignment_tests.example3 import *


def test_data_assignment_tests_example3_1():
    assert example3.intersect(0, 0, 1, 1, -1, -1, 0, 1) == True

def test_4():
    assert example3.intersect(0, 0, 1, 1, 0, 0, 1, 1) == True

def test_6():
    assert example3.intersect(0, 0, 1, 1, 1, 1, 2, 2) == True

def test_8():
    assert example3.intersect(0, 0, 1, 1, 1, 0, 2, 1) == True

def test_11_13():
    assert example3.intersect(0, 0, 1, 1, 1, 0, 2, 1) == False

def test_15_20():
    assert example3.intersect(0, 0, 1, 1, 1, 0, 2, 1) == True

def test_22_26():
    assert example3.intersect(0, 0, 1, 1, 1, 0, 2, 1) == True

def test_data_assignment_tests_example3_2():
    assert example3.intersect(0, 0, 1, 1, 1, 0, 0, 1) == True

def test_17():
    assert example3.intersect(0, 0, 1, 1, 0, 0, 1, 0) == True

def test_18():
    assert example3.intersect(0, 0, 1, 1, 1, 1, 0, 0) == True

def test_25():
    assert example3.intersect(1, 1, 0, 0, 0, 1, 1, 0) == True
