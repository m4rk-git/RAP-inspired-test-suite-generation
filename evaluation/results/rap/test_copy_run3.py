import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.copy as copy
from data.complicated_tests.copy import *

import types
import weakref
from copyreg import dispatch_table

def test_data_complicated_tests_copy_1():
    import copy
    test_obj = copy.deepcopy({1: [2, 3], 4: {5: 6}})
    assert test_obj == {1: [2, 3], 4: {5: 6}}
    assert id(test_obj[1]) != id(test_obj[4][5])
    assert isinstance(test_obj[1], list)

def test_56_to_58():
    import copy
    test_obj = copy._atomic_types
    assert test_obj == frozenset({None, Ellipsis, NotImplemented, int, float, bool, complex, bytes, str, CodeType, type, range, BuiltinFunctionType, FunctionType, ref, property})

def test_60():
    import copy
    test_obj = copy.Error
    assert issubclass(test_obj, Exception)

def test_62():
    import copy
    test_obj = copy.deepcopy(((1, 2), (3, 4)))
    assert test_obj == ((1, 2), (3, 4))
    assert id(test_obj[0]) != id(test_obj[1])

def test_68():
    import copy
    test_obj = copy.deepcopy([[1, 2], [3, 4]])
    assert test_obj == [[1, 2], [3, 4]]
    assert id(test_obj[0][0]) != id(test_obj[1][0])

def test_70_to_73():
    import copy
    class TestClass:
        def __init__(self, value):
            self.value = value
    test_obj = copy.deepcopy(TestClass(5))
    assert test_obj.value == 5

def test_76():
    import copy
    test_obj = copy.copy({1: [2, 3], 4: {5: 6}})
    assert test_obj == {1: [2, 3], 4: {5: 6}}
    assert id(test_obj[1]) == id(test_obj[4][5])
    assert isinstance(test_obj[1], list)

def test_78():
    import copy
    test_obj = copy.deepcopy([1, 2, 3])
    assert test_obj == [1, 2, 3]
    assert id(test_obj[0]) != id(test_obj[1])

def test_80_to_82():
    import copy
