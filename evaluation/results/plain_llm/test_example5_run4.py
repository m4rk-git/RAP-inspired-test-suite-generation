from data.assignment_tests.example5 import *
import pytest
import sys

# Mocking the input function to handle edge cases
def mock_input(prompt):
    if prompt == "Enter value for a: ":
        return "42"
    elif prompt == "Enter value for b: ":
        return "50"
    elif prompt == "Enter value for c: ":
        return "33"

# Monkey patching the input function
sys.__stdin__ = mock_input

def test_collection():
    # Test case 1: a = 42, b = 50, c = 33
    assert collection(42, 50, 33) == True

    # Test case 2: a = 42, b = 50, c = 66
    assert collection(42, 50, 66) == True

    # Test case 3: a = 42, b = 50, c = 99
    assert collection(42, 50, 99) == True

    # Test case 4: a = 42, b = 50, c = 100
    assert collection(42, 50, 100) == False

    # Test case 5: a = 42, b = 0, c = 33
    assert collection(42, 0, 33) == False

    # Test case 6: a = 42, b = 100, c = 33
    assert collection(42, 100, 33) == False

    # Test case 7: a = 3817, b = 50, c = 33
    assert collection(3817, 50, 33) == True

    # Test case 8: a = 3817, b = 50, c = 66
    assert collection(3817, 50, 66) == True

    # Test case 9: a = 3817, b = 50, c = 99
    assert collection(3817, 50, 99) == True

    # Test case 10: a = 3817, b = 50, c = 100
    assert collection(3817, 50, 100) == False

    # Test case 11: a = 3817, b = 0, c = 33
    assert collection(3817, 0, 33) == False

    # Test case 12: a = 3817, b = 100, c = 33
    assert collection(3817, 100, 33) == False

    # Test case 13: a = 1038472, b = 50, c = 33
    assert collection(1038472, 50, 33) == True

    # Test case 14: a = 1038472, b = 50, c = 66
    assert collection(1038472, 50, 66) == True

    # Test case 15: a = 1038472, b = 50, c = 99
    assert collection(1038472, 50, 99) == True

    # Test case 16: a = 1038472, b = 50, c = 100
    assert collection(1038472, 50, 100) == False

    # Test case 17: a = 1038472, b = 0, c = 33
    assert collection(1038472, 0, 33) == False

    # Test case 18: a = 1038472, b = 100, c = 33
    assert collection(1038472, 100, 33) == False

    # Test case 19: a = 41, b = 50, c = 33
    assert collection(41, 50, 33) == False

    # Test case 20: a = 3816, b = 50, c = 33
    assert collection(3816, 50, 33) == False

    # Test case 21: a = 1038473, b = 50, c = 33
    assert collection(1038473, 50, 33) == False

    # Test case 22: a = 42, b = 50, c = 32
    assert collection(42, 50, 32) == False

    # Test case 23: a = 42, b = 50, c = 65
    assert collection(42, 50, 65) == False

    # Test case 24: a = 42, b = 50, c = 98
    assert collection(42, 50, 98) == False

    # Test case 25: a = 42, b = 50, c = 101
    assert collection(42, 50, 101) == False

    # Test case 26: a = 42, b = 50, c = 0
    assert collection(42, 50, 0) == False

    # Test case 27: a = 42, b = 50, c = 1000
    assert collection(42, 50, 1000) == False

    # Test case 28: a = 42, b = 0, c = 33
    assert collection(42, 0, 33) == False

    # Test case 29: a = 42, b = 100, c = 33
    assert collection(42, 100, 33) == False

    # Test case 30: a = 3817, b = 0, c = 33
    assert collection(3817, 0, 33) == False

    # Test case 31: a = 3817, b = 100, c = 33
    assert collection(3817, 100, 33) == False

    # Test case 32: a = 1038472, b = 0, c = 33
    assert collection(1038472, 0, 33) == False

    # Test case 33: a = 1038472, b = 100, c = 33
    assert collection(1038472, 100, 33) == False

    # Test case 34: a = 42, b = 50, c = 33
    assert collection(42, 50, 33) == True

    # Test case 35: a = 3817, b = 50, c = 33
    assert collection(3817, 50, 33) == True

    # Test case 36: a = 1038472, b = 50, c = 33
    assert collection(1038472, 50, 33) == True

    # Test case 37: a = 42, b = 50, c = 33
    assert collection(42, 50, 33) == True

    # Test case 38: a = 3817, b = 50, c = 33
    assert collection(3817, 50, 33) == True

    # Test case 39: a = 1038472, b = 50, c = 33
    assert collection(1038472, 50, 33) == True

    # Test case 40: a = 42, b = 50, c = 33
    assert collection(42, 50, 33) == True

    # Test case 41: a = 3817, b = 50, c = 33
    assert collection(3817, 50, 33) == True

    # Test case 42: a = 1038472, b = 50, c = 33
    assert collection(1038472, 50, 33) == True

    # Test case 43: a = 42, b = 50, c = 33
    assert collection(42, 50, 33) == True

    # Test case 44: a = 3817, b = 50, c = 33
    assert collection(3817, 50, 33) == True

    # Test case 45: a = 1038472, b = 50, c = 33
    assert collection(1038472, 50, 33) == True

    # Test case 46: a = 42, b = 50, c = 33
    assert collection(42, 50, 33) == True

    # Test case 47: a = 3817, b = 50, c = 33
    assert collection(3817, 50, 33) == True

    # Test case 48: a = 1038472, b = 50, c = 33
    assert collection(1038472, 50, 33) == True

    # Test case 49: a = 42, b = 50, c = 33
    assert collection(42, 50, 33) == True

    # Test case 50: a = 3817, b = 50, c = 33
    assert collection(3817, 50, 33) == True

    # Test case 51: a = 1038472, b = 50, c = 33
    assert collection(1038472, 50, 33) == True

    # Test case 52: a = 42, b = 50, c = 33
    assert collection(42, 50, 33) == True

    # Test case 53: a = 3817, b = 50, c = 33
    assert collection(3817, 50, 33) == True

    # Test case 54: a = 1038472, b = 50, c = 33
    assert collection(1038472, 50, 33) == True

    # Test case 55: a = 42, b = 50, c = 33
    assert collection(42, 50, 33) == True

    # Test case 56: a = 3817, b = 50, c = 33
    assert collection(3817, 50, 33) == True

    # Test case 57: a = 1038472, b = 50, c = 33
    assert collection(1038472, 50, 33) == True

    # Test case 58: a = 42, b = 50, c = 33
    assert collection(42, 50, 33) == True

    # Test case 59: a = 3817, b = 50, c = 33
    assert collection(3817, 50, 33) == True

    # Test case 60: a = 1038472, b = 50, c = 33
    assert collection(1038472, 50, 33) == True

    # Test case 61: a = 42, b = 50, c = 33
    assert collection(42, 50, 33) == True

    # Test case 62: a = 3817, b = 50, c = 33
    assert collection(3817, 50,