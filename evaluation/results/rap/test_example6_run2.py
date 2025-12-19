import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example6 as example6
from data.assignment_tests.example6 import *


def test_data_assignment_tests_example6_1():
    example6.match(4)
def test_2():
    example6.match(-60)
def test_3():
    example6.match(22)
def test_4():
    example6.match(7)

def test_data_assignment_tests_example6_2(example6):
    example6.match(-57)

def test_data_assignment_tests_example6_3():
    example6.match(30)

def test_data_assignment_tests_example6_4():
    example6.match(0)

def test_data_assignment_tests_example6_5():
    example6.match(43)

def test_data_assignment_tests_example6_6():
    example6.match(23)
