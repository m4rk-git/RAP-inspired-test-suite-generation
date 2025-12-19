from data.assignment_tests.example6 import *
import pytest
import sys

# Test cases to achieve 100% code coverage
def test_match_5():
    sys.stdout = open('temp.txt', 'w')
    match(4)
    sys.stdout.close()
    with open('temp.txt', 'r') as file:
        assert file.read() == "hit 5!\n"
    sys.stdout = sys.__stdout__

def test_match_11():
    sys.stdout = open('temp.txt', 'w')
    match(7)
    sys.stdout.close()
    with open('temp.txt', 'r') as file:
        assert file.read() == "hit 10!\n"
    sys.stdout = sys.__stdout__

def test_match_neg57():
    sys.stdout = open('temp.txt', 'w')
    match(-32)
    sys.stdout.close()
    with open('temp.txt', 'r') as file:
        assert file.read() == "really?\n"
    sys.stdout = sys.__stdout__

def test_match_43():
    sys.stdout = open('temp.txt', 'w')
    match(23)
    sys.stdout.close()
    with open('temp.txt', 'r') as file:
        assert file.read() == "really?\n"
    sys.stdout = sys.__stdout__

def test_match_default():
    sys.stdout = open('temp.txt', 'w')
    match(0)
    sys.stdout.close()
    with open('temp.txt', 'r') as file:
        assert file.read() == "you haven't done anything yet\n"
    sys.stdout = sys.__stdout__

# Edge cases
def test_match_edge_case_min_int():
    sys.stdout = open('temp.txt', 'w')
    match(sys.maxsize)
    sys.stdout.close()
    with open('temp.txt', 'r') as file:
        assert file.read() == "you haven't done anything yet\n"
    sys.stdout = sys.__stdout__

def test_match_edge_case_max_int():
    sys.stdout = open('temp.txt', 'w')
    match(-sys.maxsize - 1)
    sys.stdout.close()
    with open('temp.txt', 'r') as file:
        assert file.read() == "you haven't done anything yet\n"
    sys.stdout = sys.__stdout__

def test_match_edge_case_zero():
    sys.stdout = open('temp.txt', 'w')
    match(0)
    sys.stdout.close()
    with open('temp.txt', 'r') as file:
        assert file.read() == "you haven't done anything yet\n"
    sys.stdout = sys.__stdout__

def test_match_edge_case_one():
    sys.stdout = open('temp.txt', 'w')
    match(1)
    sys.stdout.close()
    with open('temp.txt', 'r') as file:
        assert file.read() == "you haven't done anything yet\n"
    sys.stdout = sys.__stdout__

def test_match_edge_case_negative_one():
    sys.stdout = open('temp.txt', 'w')
    match(-1)
    sys.stdout.close()
    with open('temp.txt', 'r') as file:
        assert file.read() == "you haven't done anything yet\n"
    sys.stdout = sys.__stdout__

def test_match_edge_case_large_positive():
    sys.stdout = open('temp.txt', 'w')
    match(1000000)
    sys.stdout.close()
    with open('temp.txt', 'r') as file:
        assert file.read() == "you haven't done anything yet\n"
    sys.stdout = sys.__stdout__

def test_match_edge_case_large_negative():
    sys.stdout = open('temp.txt', 'w')
    match(-1000000)
    sys.stdout.close()
    with open('temp.txt', 'r') as file:
        assert file.read() == "you haven't done anything yet\n"
    sys.stdout = sys.__stdout__

# Run tests
if __name__ == "__main__":
    pytest.main()