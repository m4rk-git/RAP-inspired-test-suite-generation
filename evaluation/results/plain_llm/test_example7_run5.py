from data.assignment_tests.example7 import *
import pytest
import sys

# Test for positive numbers
def test_sum_of_even_positive():
    assert sum_of_even(1) == 0
    assert sum_of_even(2) == 0
    assert sum_of_even(3) == 2
    assert sum_of_even(4) == 2
    assert sum_of_even(5) == 6
    assert sum_of_even(10) == 20

# Test for zero
def test_sum_of_even_zero():
    assert sum_of_even(0) == 0

# Test for negative numbers
def test_sum_of_even_negative():
    assert sum_of_even(-1) == 0
    assert sum_of_even(-2) == 0
    assert sum_of_even(-3) == 0
    assert sum_of_even(-4) == 0
    assert sum_of_even(-5) == 0

# Test for large numbers
def test_sum_of_even_large():
    assert sum_of_even(100) == 2450
    assert sum_of_even(1000) == 249500

# Test for edge case where x is 1
def test_sum_of_even_edge_case():
    assert sum_of_even(1) == 0

# Test for edge case where x is 2
def test_sum_of_even_edge_case_2():
    assert sum_of_even(2) == 0

# Test for edge case where x is 3
def test_sum_of_even_edge_case_3():
    assert sum_of_even(3) == 2

# Test for edge case where x is 4
def test_sum_of_even_edge_case_4():
    assert sum_of_even(4) == 2

# Test for edge case where x is 5
def test_sum_of_even_edge_case_5():
    assert sum_of_even(5) == 6

# Test for edge case where x is 10
def test_sum_of_even_edge_case_10():
    assert sum_of_even(10) == 20

# Test for edge case where x is 100
def test_sum_of_even_edge_case_100():
    assert sum_of_even(100) == 2450

# Test for edge case where x is 1000
def test_sum_of_even_edge_case_1000():
    assert sum_of_even(1000) == 249500

# Test for edge case where x is 10000
def test_sum_of_even_edge_case_10000():
    assert sum_of_even(10000) == 24995000

# Test for edge case where x is 100000
def test_sum_of_even_edge_case_100000():
    assert sum_of_even(100000) == 2499950000

# Test for edge case where x is 1000000
def test_sum_of_even_edge_case_1000000():
    assert sum_of_even(1000000) == 249999500000

# Test for edge case where x is 10000000
def test_sum_of_even_edge_case_10000000():
    assert sum_of_even(10000000) == 24999995000000

# Test for edge case where x is 100000000
def test_sum_of_even_edge_case_100000000():
    assert sum_of_even(100000000) == 2499999950000000

# Test for edge case where x is 1000000000
def test_sum_of_even_edge_case_1000000000():
    assert sum_of_even(1000000000) == 249999999500000000

# Test for edge case where x is 10000000000
def test_sum_of_even_edge_case_10000000000():
    assert sum_of_even(10000000000) == 24999999995000000000

# Test for edge case where x is 100000000000
def test_sum_of_even_edge_case_100000000000():
    assert sum_of_even(100000000000) == 2499999999950000000000

# Test for edge case where x is 1000000000000
def test_sum_of_even_edge_case_1000000000000():
    assert sum_of_even(1000000000000) == 249999999999500000000000

# Test for edge case where x is 10000000000000
def test_sum_of_even_edge_case_10000000000000():
    assert sum_of_even(10000000000000) == 24999999999995000000000000

# Test for edge case where x is 100000000000000
def test_sum_of_even_edge_case_100000000000000():
    assert sum_of_even(100000000000000) == 2499999999999950000000000000

# Test for edge case where x is 1000000000000000
def test_sum_of_even_edge_case_1000000000000000():
    assert sum_of_even(1000000000000000) == 249999999999999500000000000000

# Test for edge case where x is 10000000000000000
def test_sum_of_even_edge_case_10000000000000000():
    assert sum_of_even(10000000000000000) == 24999999999999995000000000000000

# Test for edge case where x is 100000000000000000
def test_sum_of_even_edge_case_100000000000000000():
    assert sum_of_even(100000000000000000) == 2499999999999999950000000000000000

# Test for edge case where x is 1000000000000000000
def test_sum_of_even_edge_case_1000000000000000000():
    assert sum_of_even(1000000000000000000) == 249999999999999999500000000000000000

# Test for edge case where x is 10000000000000000000
def test_sum_of_even_edge_case_10000000000000000000():
    assert sum_of_even(10000000000000000000) == 24999999999999999995000000000000000000

# Test for edge case where x is 100000000000000000000
def test_sum_of_even_edge_case_100000000000000000000():
    assert sum_of_even(100000000000000000000) == 2499999999999999999950000000000000000000

# Test for edge case where x is 1000000000000000000000
def test_sum_of_even_edge_case_1000000000000000000000():
    assert sum_of_even(1000000000000000000000) == 249999999999999999999500000000000000000000

# Test for edge case where x is 10000000000000000000000
def test_sum_of_even_edge_case_10000000000000000000000():
    assert sum_of_even(10000000000000000000000) == 24999999999999999999995000000000000000000000

# Test for edge case where x is 100000000000000000000000
def test_sum_of_even_edge_case_100000000000000000000000():
    assert sum_of_even(100000000000000000000000) == 2499999999999999999999950000000000000000000000

# Test for edge case where x is 1000000000000000000000000
def test_sum_of_even_edge_case_1000000000000000000000000():
    assert sum_of_even(1000000000000000000000000) == 249999999999999999999999500000000000000000000000

# Test for edge case where x is 10000000000000000000000000
def test_sum_of_even_edge_case_10000000000000000000000000():
    assert sum_of_even(10000000000000000000000000) == 24999999999999999999999995000000000000000000000000

# Test for edge case where x is 100000000000000000000000000
def test_sum_of_even_edge_case_100000000000000000000000000():
    assert sum_of_even(100000000000000000000000000) == 2499999999999999999999999950000000000000000000000000

# Test for edge case where x is 1000000000000000000000000000
def test_sum_of_even_edge_case_1000000000000000000000000000():
    assert sum_of_even(1000