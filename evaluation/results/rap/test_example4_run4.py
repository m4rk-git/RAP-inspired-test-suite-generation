import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example4 as example4
from data.assignment_tests.example4 import *


def test_data_assignment_tests_example4_1():
    example4.tertiary(42, 2007)

def test_2():
    example4.tertiary(42, 0)

def test_3():
    example4.tertiary(10, 2007)

def test_4():
    example4.tertiary(10, 0)
    
def test_5():
    example4.tertiary(42, 0)
    
def test_6():
    example4.tertiary(10, 2007)
