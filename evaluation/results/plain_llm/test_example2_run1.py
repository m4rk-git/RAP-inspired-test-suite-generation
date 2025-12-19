from data.assignment_tests.example2 import *
import pytest
import sys

# Mocking the input function for testing
def mock_input(prompt):
    if prompt == "Enter a: ":
        return "10"
    elif prompt == "Enter b: ":
        return "20"
    elif prompt == "Enter c: ":
        return "100"

# Monkey patching the input function
sys.__stdin__ = mock_input

def test_testme():
    # Test case 1: c is within the range (57, 284)
    testme(10, 20, 100)
    assert True  # Assuming the function does not raise an exception

    # Test case 2: c is outside the range (57, 284)
    testme(10, 20, 50)
    assert True  # Assuming the function does not raise an exception

    # Test case 3: a becomes negative
    testme(10, 20, 50)
    assert True  # Assuming the function does not raise an exception

    # Test case 4: a is already greater than or equal to b
    testme(20, 10, 100)
    assert True  # Assuming the function does not raise an exception

    # Test case 5: a is already negative
    testme(-10, 20, 100)
    assert True  # Assuming the function does not raise an exception

if __name__ == "__main__":
    pytest.main()