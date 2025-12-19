from data.complicated_tests.copy import *
import pytest
from types import MethodType

# Test cases for copy function
def test_copy_atomic_types():
    for atomic_type in _copy_atomic_types:
        assert copy(atomic_type()) == atomic_type()

def test_copy_builtin_containers():
    for container_type in _copy_builtin_containers:
        assert copy(container_type()) == container_type()

def test_copy_class():
    class MyClass:
        def __init__(self, value):
            self.value = value

    obj = MyClass(10)
    copied_obj = copy(obj)
    assert copied_obj.value == 10
    assert copied_obj is not obj

def test_copy_method():
    class MyClass:
        def my_method(self):
            return "Hello"

    obj = MyClass()
    copied_obj = copy(obj)
    assert copied_obj.my_method() == "Hello"
    assert copied_obj.my_method is not obj.my_method

# Test cases for deepcopy function
def test_deepcopy_atomic_types():
    for atomic_type in _atomic_types:
        assert deepcopy(atomic_type()) == atomic_type()

def test_deepcopy_builtin_containers():
    for container_type in _copy_builtin_containers:
        assert deepcopy(container_type()) == container_type()

def test_deepcopy_list():
    original_list = [1, 2, 3]
    copied_list = deepcopy(original_list)
    assert copied_list == original_list
    assert copied_list is not original_list
    assert copied_list[0] is not original_list[0]

def test_deepcopy_tuple():
    original_tuple = (1, 2, 3)
    copied_tuple = deepcopy(original_tuple)
    assert copied_tuple == original_tuple
    assert copied_tuple is not original_tuple
    assert copied_tuple[0] is not original_tuple[0]

def test_deepcopy_dict():
    original_dict = {'a': 1, 'b': 2}
    copied_dict = deepcopy(original_dict)
    assert copied_dict == original_dict
    assert copied_dict is not original_dict
    assert copied_dict['a'] is not original_dict['a']

def test_deepcopy_method():
    class MyClass:
        def my_method(self):
            return "Hello"

    obj = MyClass()
    copied_obj = deepcopy(obj)
    assert copied_obj.my_method() == "Hello"
    assert copied_obj.my_method is not obj.my_method

# Test cases for replace function
def test_replace_immutable_object():
    class MyClass:
        def __init__(self, value):
            self.value = value

        def __replace__(self, **changes):
            return MyClass(**{**self.__dict__, **changes})

    obj = MyClass(10)
    replaced_obj = replace(obj, value=20)
    assert replaced_obj.value == 20
    assert replaced_obj is not obj

def test_replace_method():
    class MyClass:
        def my_method(self):
            return "Hello"

        def __replace__(self, **changes):
            return MyClass(**{**self.__dict__, **changes})

    obj = MyClass()
    replaced_obj = replace(obj, my_method=lambda: "World")
    assert replaced_obj.my_method() == "World"
    assert replaced_obj.my_method is not obj.my_method

def test_replace_non_immutable_object():
    class MyClass:
        def __init__(self, value):
            self.value = value

    obj = MyClass(10)
    with pytest.raises(TypeError):
        replace(obj, value=20)

def test_replace_missing_replace_method():
    class MyClass:
        def __init__(self, value):
            self.value = value

    obj = MyClass(10)
    with pytest.raises(TypeError):
        replace(obj, value=20)

if __name__ == "__main__":
    pytest.main()