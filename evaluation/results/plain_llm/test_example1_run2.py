from data.assignment_tests.example1 import *
import pytest
from typing import *

def test_foo():
    # Test cases for foo function
    assert foo(42, 0) == 1
    assert foo(42, 1) == 0
    assert foo(43, 0) == -1
    assert foo(43, 1) == -1
    assert foo(0, 0) == -1
    assert foo(0, 1) == -1

def test_bar():
    # Test cases for bar function
    assert bar(1, 2, 0) == 0
    assert bar(1, 2, 1) == 1
    assert bar(1, 2, 2) == 2
    assert bar(2, 1, 0) == 0
    assert bar(2, 1, 1) == 2
    assert bar(2, 1, 2) == 1
    assert bar(1, 1, 0) == 0
    assert bar(1, 1, 1) == 1
    assert bar(1, 1, 2) == 1
    assert bar(2, 2, 0) == 0
    assert bar(2, 2, 1) == 2
    assert bar(2, 2, 2) == 2