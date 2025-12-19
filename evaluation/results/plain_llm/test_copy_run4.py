from data.complicated_tests.copy import *
import pytest
from copy import Error

def test_copy_atomic_types():
    assert copy(None) is None
    assert copy(1) == 1
    assert copy(1.0) == 1.0
    assert copy(True) is True
    assert copy(1+1j) == 1+1j
    assert copy('a') == 'a'
    assert copy((1, 2, 3)) == (1, 2, 3)
    assert copy(b'abc') == b'abc'
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
    assert copy(bytearray(b'abc')) == bytearray(b'abc')

def test_copy_class_with_copy_method():
    class MyClass:
        def __init__(self, value):
            self.value = value

        def __copy__(self):
            return MyClass(self.value)

    obj = MyClass(1)
    assert copy(obj).value == 1

def test_copy_class_with_reduce_method():
    class MyClass:
        def __init__(self, value):
            self.value = value

        def __reduce__(self):
            return MyClass, (self.value,)

    obj = MyClass(1)
    assert copy(obj).value == 1

def test_copy_class_with_reduce_ex_method():
    class MyClass:
        def __init__(self, value):
            self.value = value

        def __reduce_ex__(self, protocol):
            return MyClass, (self.value,)

    obj = MyClass(1)
    assert copy(obj).value == 1

def test_copy_class_without_copy_reduce_reduce_ex_method():
    class MyClass:
        def __init__(self, value):
            self.value = value

    obj = MyClass(1)
    with pytest.raises(Error):
        copy(obj)

def test_deepcopy_atomic_types():
    assert deepcopy(None) is None
    assert deepcopy(1) == 1
    assert deepcopy(1.0) == 1.0
    assert deepcopy(True) is True
    assert deepcopy(1+1j) == 1+1j
    assert deepcopy('a') == 'a'
    assert deepcopy((1, 2, 3)) == (1, 2, 3)
    assert deepcopy(b'abc') == b'abc'
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
    assert deepcopy(bytearray(b'abc')) == bytearray(b'abc')

def test_deepcopy_class_with_deepcopy_method():
    class MyClass:
        def __init__(self, value):
            self.value = value

        def __deepcopy__(self, memo):
            return MyClass(self.value)

    obj = MyClass(1)
    assert deepcopy(obj).value == 1

def test_deepcopy_class_with_reduce_method():
    class MyClass:
        def __init__(self, value):
            self.value = value

        def __reduce__(self):
            return MyClass, (self.value,)

    obj = MyClass(1)
    assert deepcopy(obj).value == 1

def test_deepcopy_class_with_reduce_ex_method():
    class MyClass:
        def __init__(self, value):
            self.value = value

        def __reduce_ex__(self, protocol):
            return MyClass, (self.value,)

    obj = MyClass(1)
    assert deepcopy(obj).value == 1

def test_deepcopy_class_without_deepcopy_reduce_reduce_ex_method():
    class MyClass:
        def __init__(self, value):
            self.value = value

    obj = MyClass(1)
    with pytest.raises(Error):
        deepcopy(obj)

def test_replace():
    class MyClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __replace__(self, **changes):
            return MyClass(**{**self.__dict__, **changes})

    obj = MyClass(1, 2)
    assert replace(obj, a=3).a == 3
    assert replace(obj, b=4).b == 4
    assert replace(obj, a=3, b=4).a == 3
    assert replace(obj, a=3, b=4).b == 4

def test_replace_immutable():
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    with pytest.raises(TypeError):
        replace(p, x=3)

def test_replace_no_replace_method():
    class MyClass:
        pass

    obj = MyClass()
    with pytest.raises(TypeError):
        replace(obj, a=3)

def test_error():
    with pytest.raises(Error):
        copy(object())
    with pytest.raises(Error):
        deepcopy(object())