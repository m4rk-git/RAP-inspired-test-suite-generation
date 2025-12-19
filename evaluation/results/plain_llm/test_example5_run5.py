from data.assignment_tests.example5 import *
import pytest
import sys

# Mocking the sys.argv to simulate command line arguments
sys.argv = ['test_collection.py']

# Test cases for the function 'collection'
def test_collection_valid_input():
    assert collection(42, 50, 33) == True, "Test case 1 failed"
    assert collection(3817, 25, 66) == True, "Test case 2 failed"
    assert collection(1038472, 75, 99) == True, "Test case 3 failed"

def test_collection_invalid_a():
    assert collection(123, 50, 33) == False, "Test case 4 failed"
    assert collection(42, 50, 123) == False, "Test case 5 failed"
    assert collection(3817, 50, 123) == False, "Test case 6 failed"
    assert collection(1038472, 50, 123) == False, "Test case 7 failed"

def test_collection_invalid_b():
    assert collection(42, 0, 33) == False, "Test case 8 failed"
    assert collection(42, 100, 33) == False, "Test case 9 failed"
    assert collection(3817, 0, 66) == False, "Test case 10 failed"
    assert collection(3817, 100, 66) == False, "Test case 11 failed"
    assert collection(1038472, 0, 99) == False, "Test case 12 failed"
    assert collection(1038472, 100, 99) == False, "Test case 13 failed"

def test_collection_invalid_c():
    assert collection(42, 50, 123) == False, "Test case 14 failed"
    assert collection(3817, 50, 123) == False, "Test case 15 failed"
    assert collection(1038472, 50, 123) == False, "Test case 16 failed"

# Running the tests
if __name__ == "__main__":
    pytest.main()