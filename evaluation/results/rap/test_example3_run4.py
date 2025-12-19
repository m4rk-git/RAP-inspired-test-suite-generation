import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example3 as example3
from data.assignment_tests.example3 import *


def test_data_assignment_tests_example3_1(self):
    example3.intersect(0, 0, 1, 1, 1, 0, 0, 1)

def test_02(self):
    example3.intersect(0, 0, 1, 1, 1, 1, 0, 0)

def test_03(self):
    example3.intersect(0, 0, 1, 1, 1, 0, 1, 0)

def test_04(self):
    example3.intersect(0, 0, 1, 1, 1, 1, 1, 0)

def test_05(self):
    example3.intersect(0, 0, 1, 1, 1, 0, 1, 1)

def test_06(self):
    example3.intersect(0, 0, 1, 1, 1, 1, 1, 1)

def test_07(self):
    example3.intersect(0, 0, 1, 1, -1, 0, 1, 1)

def test_08(self):
    example3.intersect(0, 0, 1, 1, 1, 0, -1, 1)

def test_09(self):
    example3.intersect(0, 0, 1, 1, 1, 0, 0, -1)

def test_10(self):
    example3.intersect(0, 0, 1, 1, -1, 1, 1, 0)

def test_11(self):
    example3.intersect(0, 0, 1, 1, 1, 1, 0, 0)

def test_12(self):
    example3.intersect(0, 0, 1, 1, 1, 1, 1, 1)

def test_13(self):
    example3.intersect(0, 0, 1, 1, -1, 0, 1, 1)

def test_14(self):
    example3.intersect(0, 0, 1, 1, 1, 0, -1, 1)

def test_15(self):
    example3.inter

def test_data_assignment_tests_example3_2():
    assert example3.intersect(0, 0, 1, 1, 1, 0, 0, 1) == False

def test_6():
    assert example3.intersect(0, 0, 1, 1, 1, 1, 0, 0) == False

def test_8():
    assert example3.intersect(0, 0, 1, 1, 1, 1, 1, 0) == False

def test_11_13_15_20():
    assert example3.intersect(0, 0, 0, 1, 1, 0, 1, 1) == True

def test_22_26():
    assert example3.intersect(0, 0, 0, 1, 1, 0, 0, 0) == True
