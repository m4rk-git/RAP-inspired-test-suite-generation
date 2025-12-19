import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example6 as example6
from data.assignment_tests.example6 import *


def test_data_assignment_tests_example6_1():
    example6.match(4)

def test_data_assignment_tests_example6_2():
    example6.match(7)

def test_data_assignment_tests_example6_3():
    match(3)

def test_9th_line():
    match(-57)

def test_10th_line():
    match(43)

def test_11th_line():
    match(0)

def test_data_assignment_tests_example6_4():
    example6.match(5)

def test_data_assignment_tests_example6_5():
    example6.match(-57)

def test_data_assignment_tests_example6_6() -> None: 
    example6.match(23) 
    example6.match(-60) 
    example6.match(43) 
    example6.match(-7) 
    example6.match(0) 
    example6.match(5) 
    example6.match(11) 
    example6.match(29) 
    example6.match(17) 
    example6.match(6)
