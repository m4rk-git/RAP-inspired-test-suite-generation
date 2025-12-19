import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example2 as example2
from data.assignment_tests.example2 import *


def test_data_assignment_tests_example2_1():
    example2.testme(0, 5, 100)
