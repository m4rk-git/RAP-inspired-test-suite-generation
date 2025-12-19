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
    assert copy('a') == 'a'
    assert copy((1, 2, 3)) == (1, 2, 3)
    assert copy(b'a') == b'a'
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
    assert copy({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert copy({1, 2, 3}) == {1, 2, 3}
    assert copy(bytearray(b'a')) == bytearray(b'a')

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
    assert deepcopy('a') == 'a'
    assert deepcopy((1, 2, 3)) == (1, 2, 3)
    assert deepcopy(b'a') == b'a'
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
    assert deepcopy({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert deepcopy({1, 2, 3}) == {1, 2, 3}
    assert deepcopy(bytearray(b'a')) == bytearray(b'a')

def test_deepcopy_class():
    class MyClass:
        def __init__(self, value):
            self.value = value

    obj = MyClass(1)
    assert deepcopy(obj).value == 1

def test_deepcopy_recursive():
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    node = Node(1, Node(2), Node(3))
    node.left.right = node
    with pytest.raises(RecursionError):
        deepcopy(node)

def test_deepcopy_memoization():
    class MyClass:
        def __init__(self, value):
            self.value = value

    obj = MyClass(1)
    memo = {id(obj): obj}
    assert deepcopy(obj, memo) is obj

# Test cases for replace function
def test_replace_immutable():
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    assert replace(p, x=3) == Point(3, 2)

def test_replace_mutable():
    from dataclasses import dataclass
    @dataclass(frozen=True)
    class Point:
        x: int
        y: int

    p = Point(1, 2)
    assert replace(p, x=3) == Point(3, 2)

def test_replace_error():
    class MyClass:
        pass

    obj = MyClass()
    with pytest.raises(TypeError):
        replace(obj, x=3)