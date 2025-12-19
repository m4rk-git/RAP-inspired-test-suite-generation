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
    isinstance(copy.Error, Exception)

def test_56():
    import copy
    copy.error = copy.Error

def test_60():
    import copy
    copy.__all__ = ["Error", "copy", "deepcopy", "replace"]

def test_62():
    import copy
    copy.copy(1)

def test_68():
    import copy
    copy.deepcopy(1)

def test_70():
    import copy
    copy.replace((1, 2), a=1)

def test_73():
    import copy
    copy.replace(1, a=1)

def test_76():
    import copy
    isinstance(copy.copy(None), type(None))

def test_78():
    import copy
    isinstance(copy.deepcopy(None), type(None))

def test_80():
    import copy
    copy._copy_atomic_types

def test_82():
    import copy
    copy._copy_builtin_containers

def test_84():
    import copy
    copy._deepcopy_dispatch

def test_86():
    import copy
    copy._atomic_types

def test_88():
    import copy
    copy._deepcopy_list([])

def test_90():
    import copy
    copy._deepcopy_tuple(())

def test_92():
    import copy
    copy._deepcopy_dict({})

def test_94():
    import copy
    copy._deepcopy_method(None)

def test_96():
    import copy
    copy._keep_alive(1, {})

def test_98():
    import copy
    isinstance(copy._reconstruct(1, {}, None, ()))

def test_100():
    import copy
    isinstance(copy._reconstruct(1, {}, None, (), state=None), int)

def test_103():
    import copy
    copy._deepcopy_list([1], {})

def test_108():
    import copy
    copy._deepcopy_tuple((1,), {})

def test_110():
    import copy
    copy._deepcopy_dict({1: 2}, {})

def test_116():
    import copy
    isinstance(copy.deepcopy(1, {}), int)

def test_118():
    import copy
    copy.deepcopy({1: 2}, {})

def test_120():
    import copy
    isinstance
