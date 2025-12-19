from data.complicated_tests.copy import *
import pytest
from copy import Error

# Test cases for copy function
def test_copy_atomic_types():
    assert copy(None) is None
    assert copy(1) == 1
    assert copy(1.0) == 1.0
    assert copy(True) is True
    assert copy(1j) == 1j
    assert copy("test") == "test"
    assert copy((1, 2, 3)) == (1, 2, 3)
    assert copy(b"test") == b"test"
    assert copy(frozenset([1, 2, 3])) == frozenset([1, 2, 3])
    assert copy(type) is type
    assert copy(range(3)) == range(3)
    assert copy(slice(1, 2, 3)) == slice(1, 2, 3)
    assert copy(property) is property
    assert copy(types.BuiltinFunctionType) is types.BuiltinFunctionType
    assert copy(types.EllipsisType) is types.EllipsisType
    assert copy(types.NotImplementedType) is types.NotImplementedType
    assert copy(types.FunctionType) is types.FunctionType
    assert copy(types.CodeType) is types.CodeType
    assert copy(weakref.ref) is weakref.ref
    assert copy(super) is super

def test_copy_builtin_containers():
    assert copy([1, 2, 3]) == [1, 2, 3]
    assert copy({1: 2, 3: 4}) == {1: 2, 3: 4}
    assert copy({1, 2, 3}) == {1, 2, 3}
    assert copy(bytearray(b"test")) == bytearray(b"test")

def test_copy_class():
    class MyClass:
        def __init__(self, value):
            self.value = value

    obj = MyClass(1)
    assert copy(obj).value == 1

def test_copy_error():
    with pytest.raises(Error):
        copy(object())

# Test cases for deepcopy function
def test_deepcopy_atomic_types():
    assert deepcopy(None) is None
    assert deepcopy(1) == 1
    assert deepcopy(1.0) == 1.0
    assert deepcopy(True) is True
    assert deepcopy(1j) == 1j
    assert deepcopy("test") == "test"
    assert deepcopy((1, 2, 3)) == (1, 2, 3)
    assert deepcopy(b"test") == b"test"
    assert deepcopy(frozenset([1, 2, 3])) == frozenset([1, 2, 3])
    assert deepcopy(type) is type
    assert deepcopy(range(3)) == range(3)
    assert deepcopy(slice(1, 2, 3)) == slice(1, 2, 3)
    assert deepcopy(property) is property
    assert deepcopy(types.BuiltinFunctionType) is types.BuiltinFunctionType
    assert deepcopy(types.EllipsisType) is types.EllipsisType
    assert deepcopy(types.NotImplementedType) is types.NotImplementedType
    assert deepcopy(types.FunctionType) is types.FunctionType
    assert deepcopy(types.CodeType) is types.CodeType
    assert deepcopy(weakref.ref) is weakref.ref
    assert deepcopy(super) is super

def test_deepcopy_builtin_containers():
    assert deepcopy([1, 2, 3]) == [1, 2, 3]
    assert deepcopy({1: 2, 3: 4}) == {1: 2, 3: 4}
    assert deepcopy({1, 2, 3}) == {1, 2, 3}
    assert deepcopy(bytearray(b"test")) == bytearray(b"test")

def test_deepcopy_class():
    class MyClass:
        def __init__(self, value):
            self.value = value

    obj = MyClass(1)
    assert deepcopy(obj).value == 1

def test_deepcopy_recursive():
    class MyClass:
        def __init__(self, value):
            self.value = value
            self.recursive = None

    obj = MyClass(1)
    obj.recursive = obj
    assert deepcopy(obj).value == 1

def test_deepcopy_error():
    with pytest.raises(Error):
        deepcopy(object())

# Test cases for replace function
def test_replace_immutable():
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    assert replace(p, x=3) == Point(3, 2)

def test_replace_mutable():
    class MyClass:
        def __init__(self, value):
            self.value = value

        def __replace__(self, **changes):
            return MyClass(**{**self.__dict__, **changes})

    obj = MyClass(1)
    assert replace(obj, value=2).value == 2

def test_replace_error():
    class MyClass:
        pass

    obj = MyClass()
    with pytest.raises(TypeError):
        replace(obj, x=1)