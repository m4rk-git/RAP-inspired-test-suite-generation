import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example2 as example2
from data.assignment_tests.example2 import *


def test_data_assignment_tests_example2_1():
    testme(0, 10, 60)  # This should force lines 1-4, 6, 8-10 to be executed

def test_data_assignment_tests_example2_2():
    example2.testme(1, 10, 100)

def test_9():
    example2.testme(-1, 10, 100)

def test_data_assignment_tests_example2_3():
    example2.testme(0, 100, 150)

def test_9():
    example2.testme(-1, 100, 150)

def test_data_assignment_tests_example2_4():
    example2.testme(0, 1, 58)

def test_9():
    example2.testme(0, 1, -1)
