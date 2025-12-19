import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example6 as example6
from data.assignment_tests.example6 import *


def test_data_assignment_tests_example6_1() -> None:
    example6.match(24)
def test_5() -> None:
    example6.match(4)
def test_11() -> None:
    example6.match(7)
def test_negative_57_and_43() -> None:
    example6.match(50)
def test_default() -> None:
    example6.match(0)
