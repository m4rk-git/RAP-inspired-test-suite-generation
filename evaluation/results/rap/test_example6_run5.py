import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example6 as example6
from data.assignment_tests.example6 import *


def test_data_assignment_tests_example6_1():
    example6.match(5)

def test_data_assignment_tests_example6_2():
    example6.match(4)

def test_02_run_example6_line_7():
    example6.match(6)

def test_03_run_example6_line_9():
    example6.match(43)

def test_data_assignment_tests_example6_3():
    example6.match(7)

def test_9_example6():
    example6.match(43)
