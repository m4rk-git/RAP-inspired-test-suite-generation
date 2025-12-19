import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example3 as example3
from data.assignment_tests.example3 import *


def test_data_assignment_tests_example3_1():
    assert example3.intersect(0, 0, 1, 1, 1, 0, 2, 0) == True

def test_02():
    assert example3.intersect(0, 0, 1, 1, 1, 1, 2, 1) == True

def test_03():
    assert example3.intersect(0, 0, 1, 1, 2, 0, 3, 0) == False

def test_04():
    assert example3.intersect(0, 0, 1, 1, 2, 1, 3, 1) == False

def test_05():
    assert example3.intersect(0, 0, 1, 1, 1, 0, 2, 0) == True

def test_06():
    assert example3.intersect(0, 0, 1, 1, 1, 1, 2, 1) == True

def test_07():
    assert example3.intersect(0, 0, 1, 1, 2, 0, 3, 0) == False

def test_08():
    assert example3.intersect(0, 0, 1, 1, 2, 1, 3, 1) == False

def test_09():
    assert example3.intersect(0, 0, 1, 1, 1, 0, 2, 0) == True

def test_10():
    assert example3.intersect(0, 0, 1, 1, 1, 1, 2, 1) == True

def test_11():
    assert example3.intersect(0, 0, 1, 1, 2, 0, 3, 0) == False

def test_12():
    assert example3.intersect(0, 0, 1, 1, 2, 1, 3, 1) == False

def test_data_assignment_tests_example3_2():
    assert example3.intersect(0, 0, 1, 1, 0, 1, 1, 0) == True

def test_023():
    assert example3.intersect(0, 0, 1, 1, 1, 0, 0, 1) == True

def test_024():
    assert example3.intersect(0, 0, 0, 1, 1, 0, 1, 1) == True

def test_025():
    assert example3.intersect(0, 0, 1, 0, 0, 1, 1, 1) == True

def test_data_assignment_tests_example3_3():
    assert example3.intersect(0, 0, 1, 1, 0, 1, 1, 0) == True

def test_2():
    assert example3.intersect(0, 0, 1, 1, 1, 0, 0, 1) == True

def test_data_assignment_tests_example3_4():
    assert example3.intersect(0, 0, 1, 0, 0, 1, 1, 1)

def test_25():
    assert example3.intersect(0, 0, 1, 0, 1, 0, 0, 1)

def test_data_assignment_tests_example3_5():
    assert example3.intersect(0, 0, 1, 1, 1, 0, 0, 1) == True

def test_025():
    assert example3.intersect(0, 0, 1, 1, 0, 1, 1, 0) == True

def test_data_assignment_tests_example3_6():
    assert not example3.intersect(1, 1, 2, 2, 3, 3, 4, 4)

def test_25():
    assert not example3.intersect(1, 1, 2, 2, 2, 2, 4, 4)
