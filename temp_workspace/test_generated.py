import sys
import os
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
sys.path.append(r'/root/RAPiT-project/data/assignment_tests')
import pytest
import example1 as example1
from example1 import *


def test_example1_1():
    result = example1.foo(42, 0)
    assert result == 1

def test_2():
    result = example1.foo(42, 1)
    assert result == 0

def test_3():
    result = example1.foo(1, 0)
    assert result == -1

def test_4():
    result = example1.bar(10, 20, 5)
    assert result == 5

def test_5():
    result = example1.bar(20, 10, 1)
    assert result == 20

def test_6():
    result = example1.bar(10, 10, 5)
    assert result == 10

def test_example1_2():
    example1.bar(4, 2, 0)

def test_16():
    example1.bar(4, 2, 1)

def test_18():
    example1.bar(2, 4, 1)

def test_example1_3():
    assert example1.bar(10, 5, 3) == 10
    assert example1.bar(15, 3, 1) == 15

# This code forces the interpreter to execute lines 15 and 16
assert example1.bar(20, 5, 10) == 20

# This code forces the interpreter to execute line 18
assert example1.bar(10, 15, 3) == 15

def test_example1_4():
   assert example1.foo(42, 0) == 1

def test_02():
   assert example1.foo(42, 1) == -1

def test_03():
   assert example1.foo(43, 0) == -1

def test_04():
   assert example1.foo(43, 1) == -1

def test_05():
   assert example1.bar(1, 2, 0) == 2

def test_06():
   assert example1.bar(2, 1, 0) == 1

def test_07():
   assert example1.bar(1, 2, -1) == 2

def test_08():
   assert example1.bar(1, 2, 10) == 2

def test_09():
   assert example1.bar(2, 1, -10) == 1

def test_10():
   assert example1.bar(2, 10, -10) == 10

def test_11():
   assert example1.bar(1, 10, 5) == 10

def test_12():
   assert example1.bar(10, 1, 2) == 10

def test_example1_5():
    foo(42, 0)

def test_2():
    foo(43, 0)

def test_3():
    foo(42, 1)

def test_4():
    bar(2, 1, 1)

def test_5():
    bar(1, 2, 1)

def test_6():
    bar(3, 1, 2)

def test_example1_6():
    assert example1.foo(42, 0) == 1

def test_02():
    assert example1.bar(1, 2, 3) == 2

def test_03():
    assert example1.bar(3, 2, 1) == 3

def test_04():
    assert example1.foo(42, 1) == 0

def test_05():
    assert example1.foo(43, 0) == -1

def test_06():
    assert example1.bar(3, 2, 4) == 3

def test_07():
    assert example1.bar(3, 2, 0) == 2

def test_08():
    assert example1.foo(43, 1) == -1

def test_09():
    assert example1.bar(1, 2, 4) == 2

def test_10():
    assert example1.bar(3, 2, 0) == 2

def test_example1_7():
    foo(42, 0)
    foo(42, 1)
    foo(41, 0)
    foo(41, 1)

def test_2():
    bar(1, 1, 0)
    bar(1, 2, 0)
    bar(2, 1, 0)
    bar(2, 2, 0)

def test_example1_8():
    return example1.foo(42, 0)

def test_5():
    return example1.foo(42, 1)

def test_7():
    return example1.foo(43, 0)

def test_9():
    return example1.foo(41, 0)

def test_10():
    return example1.foo(43, 0)

def test_15():
    return example1.bar(1, 2, 0)

def test_16():
    return example1.bar(2, 1, 0)

def test_18():
    return example1.bar(2, 1, 2)
