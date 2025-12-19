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
    _copy_atomic_types = copy._copy_atomic_types
    assert isinstance(_copy_atomic_types, frozenset)


def test_56():
    import copy
    Error = copy.Error
    assert issubclass(copy.Error, Exception)


def test_60():
    import copy
    __all__ = copy.__all__
    assert 'Error' in __all__


def test_62():
    import copy
    Error = copy.Error
    assert isinstance(Error, type)


def test_68():
    import copy
    Error = copy.Error
    error = copy.error
    assert error is Error


def test_70():
    import copy
    copy.copy(1)


def test_72():
    import copy
    class MyClass:
        pass
    copy.copy(MyClass)


def test_76():
    import copy
    copy.copy(None)


def test_78():
    import copy
    copy.copy(1j)


def test_80():
    import copy
    class MyClass:
        pass
    copy.copy(MyClass())


def test_82():
    import copy
    class MyClass:
        pass
    copy.copy(MyClass)


def test_84():
    import copy
    class MyClass:
        pass
    copy.deepcopy(MyClass)


def test_86():
    import copy
    class MyClass:
        pass
    copy.deepcopy(MyClass())


def test_88():
    import copy
    class MyClass:
        pass
    copy.deepcopy(MyClass)


def test_90():
    import copy
    class MyClass:
        pass
    copy.deepcopy(MyClass)


def test_92():
    import copy
    class MyClass:
        pass
    copy.deepcopy(MyClass)


def test_94():
    import copy
    class MyClass:
        pass
    copy.deepcopy(MyClass)


def test_96():
    import copy
    class MyClass:
        pass
    copy.deepcopy(MyClass)


def test_98():
    import copy
    class MyClass:
        pass
    copy.deepcopy(MyClass)


def test_100():
    import copy
    class MyClass:
        pass
    copy.deepcopy(MyClass)


def test_103():
    import copy
    _copy_atomic_types = copy._copy_atomic_types
    assert isinstance(_copy_atomic_types, frozenset)


def test_108():
    import copy
    _copy_builtin_cont
