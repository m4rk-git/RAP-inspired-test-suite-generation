import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import data.assignment_tests.example1 as example1
from data.assignment_tests.example1 import *


def test_data_assignment_tests_example1_1():
    example1.foo(42, 0)

def test_2():
    example1.bar(1, 2, 3)

def test_3():
    example1.foo(43, 0)

def test_4():
    example1.bar(2, 1, 0)

def test_5():
    example1.foo(42, 1)

def test_6():
    example1.bar(1, 2, 4)

def test_7():
    example1.bar(1, 2, 3)

def test_8():
    example1.bar(2, 1, 0)

def test_9():
    example1.foo(42, 0)

def test_10():
    example1.bar(1, 2, 3)

def test_11():
    example1.foo(43, 0)

def test_12():
    example1.bar(2, 1, 0)

def test_13():
    example1.bar(1, 2, 4)

def test_14():
    example1.foo(42, 1)

def test_15():
    example1.bar(1, 2, 3)

def test_data_assignment_tests_example1_2(example1):
    example1.bar(2, 3, 6)

def test_02(example1):
    example1.bar(5, 2, 4)

def test_03(example1):
    example1.bar(10, 5, 3)

def test_04(example1):
    example1.bar(3, 1, 2)

def test_data_assignment_tests_example1_3():
    assert example1.bar(4, 3, 2) == 4

def test_data_assignment_tests_example1_4():
    assert example1.bar(5, 1, 0) == 5

def test_data_assignment_tests_example1_5():
    result = example1.bar(1, 2, 3) 
    assert result == 1

def test_data_assignment_tests_example1_6():
    assert example1.bar(1, 2, 3) == 2

def test_data_assignment_tests_example1_7(example1):
    return example1.bar(10, 5, -1)

def test_data_assignment_tests_example1_8():
    assert example1.bar(2, 1, 0) == 2

def test_03():
    assert example1.bar(1, 2, 0) == 1

def test_04():
    assert example1.bar(1, 2, 2) == 2

def test_05():
    assert example1.bar(5, 3, 1) == 5

def test_06():
    assert example1.bar(3, 5, 1) == 3

def test_07():
    assert example1.bar(3, 2, 2) == 2

def test_08():
    assert example1.bar(2, 3, 3) == 2

def test_09():
    assert example1.bar(9, 3, 1) == 9

def test_10():
    assert example1.bar(3, 9, 1) == 3

def test_11():
    assert example1.bar(3, 2, 3) == 2

def test_12():
    assert example1.bar(2, 3, 0) == 2

def test_13():
    assert example1.bar(5, 3, 2) == 5

def test_14():
    assert example1.bar(3, 5, 2) == 3

def test_15():
    assert example1.bar(3, 2, 0) == 2

def test_16():
    assert example1.bar(5, 3, 2) == 3

def test_17():
    assert example1.bar(3, 5, 1) == 3

def test_18():
    assert example1.bar(3, 2, 2) == 2

def test_19():
    assert example1.bar(2, 3, 3) == 2

def test_20():
    assert example1.bar(9, 3, 1) == 9

def test_21():
    assert example1.bar(3, 9, 1) == 3

def test_22():
    assert example1.bar(3, 2, 3) == 2

def test_23():
    assert example1.bar
