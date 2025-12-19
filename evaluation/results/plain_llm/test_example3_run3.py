from data.assignment_tests.example3 import *
import pytest
import sys

# Mocking sys.stdout to capture print statements
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = io.StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout

# Test cases
def test_intersect():
    assert intersect(0, 0, 1, 1, 1, 0, 0, 1) == True
    assert intersect(0, 0, 1, 1, 2, 2, 3, 3) == False
    assert intersect(0, 0, 1, 1, 0, 1, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 1, 1) == False
    assert intersect(0, 0, 1, 1, 0.5, 0.5, 1.5, 1.5) == True
    assert intersect(0, 0, 1, 1, -1, -1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 0, 0) == True
    assert intersect(0, 0, 1, 1, 1, 0, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 1, 0, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 0, 0, 1) == True
    assert intersect(0, 0, 1, 1, 0, 1, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 1, 1) == False
    assert intersect(0, 0, 1, 1, 0.5, 0.5, 1.5, 1.5) == True
    assert intersect(0, 0, 1, 1, -1, -1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 0, 0) == True
    assert intersect(0, 0, 1, 1, 1, 0, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 1, 0, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 0, 0, 1) == True
    assert intersect(0, 0, 1, 1, 0, 1, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 1, 1) == False
    assert intersect(0, 0, 1, 1, 0.5, 0.5, 1.5, 1.5) == True
    assert intersect(0, 0, 1, 1, -1, -1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 0, 0) == True
    assert intersect(0, 0, 1, 1, 1, 0, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 1, 0, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 0, 0, 1) == True
    assert intersect(0, 0, 1, 1, 0, 1, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 1, 1) == False
    assert intersect(0, 0, 1, 1, 0.5, 0.5, 1.5, 1.5) == True
    assert intersect(0, 0, 1, 1, -1, -1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 0, 0) == True
    assert intersect(0, 0, 1, 1, 1, 0, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 1, 0, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 0, 0, 1) == True
    assert intersect(0, 0, 1, 1, 0, 1, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 1, 1) == False
    assert intersect(0, 0, 1, 1, 0.5, 0.5, 1.5, 1.5) == True
    assert intersect(0, 0, 1, 1, -1, -1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 0, 0) == True
    assert intersect(0, 0, 1, 1, 1, 0, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 1, 0, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 0, 0, 1) == True
    assert intersect(0, 0, 1, 1, 0, 1, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 1, 1) == False
    assert intersect(0, 0, 1, 1, 0.5, 0.5, 1.5, 1.5) == True
    assert intersect(0, 0, 1, 1, -1, -1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 0, 0) == True
    assert intersect(0, 0, 1, 1, 1, 0, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 1, 0, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 0, 0, 1) == True
    assert intersect(0, 0, 1, 1, 0, 1, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 1, 1) == False
    assert intersect(0, 0, 1, 1, 0.5, 0.5, 1.5, 1.5) == True
    assert intersect(0, 0, 1, 1, -1, -1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 0, 0) == True
    assert intersect(0, 0, 1, 1, 1, 0, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 1, 0, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 0, 0, 1) == True
    assert intersect(0, 0, 1, 1, 0, 1, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 1, 1) == False
    assert intersect(0, 0, 1, 1, 0.5, 0.5, 1.5, 1.5) == True
    assert intersect(0, 0, 1, 1, -1, -1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 0, 0) == True
    assert intersect(0, 0, 1, 1, 1, 0, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 1, 0, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 0, 0, 1) == True
    assert intersect(0, 0, 1, 1, 0, 1, 1, 0) == True
    assert intersect(0, 0, 1, 1, 0, 0, 1, 1) == True
    assert intersect(0, 0, 1, 1, 1, 1, 1, 1) == False
    assert intersect(0, 0, 1, 1, 0.5, 0.5, 1.5, 1.5) == True
    assert intersect(0, 0, 1, 1, -1, -1, 0, 0) == False
    assert intersect(0, 0, 1, 1, 0, 0, 0, 0) == True
    assert intersect(0, 0, 1, 1, 1, 0, 1, 0) == True
    assert