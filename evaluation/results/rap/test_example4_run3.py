import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example4 as example4
from data.assignment_tests.example4 import *


def test_data_assignment_tests_example4_1():
    example4.tertiary(42, 2007)

def test_Example4_line_4():
    example4.tertiary(42, 2007)

def test_Example4_line_6():
    example4.tertiary(42, 2007)

def test_Example4_line_8():
    example4.tertiary(42, 2007)

def test_data_assignment_tests_example4_2():
    example4.tertiary(42, 2007)

def test_8():
    example4.tertiary(42, 2008)
