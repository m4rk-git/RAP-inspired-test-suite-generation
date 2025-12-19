import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example2 as example2
from data.assignment_tests.example2 import *


def test_data_assignment_tests_example2_1():
    example2.testme(5, 10, 150)

def test_data_assignment_tests_example2_2():
    example2.testme(0, 1, 300)

def test_9():
    example2.testme(0, -1, 2)
