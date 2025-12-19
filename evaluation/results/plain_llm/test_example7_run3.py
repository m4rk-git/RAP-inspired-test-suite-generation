from data.assignment_tests.example7 import *
import pytest
import sys
sys.tracebacklimit = 0

def test_sum_of_even_zero():
    assert sum_of_even(0) == 0

def test_sum_of_even_negative():
    assert sum_of_even(-1) == 0

def test_sum_of_even_one():
    assert sum_of_even(1) == 0

def test_sum_of_even_two():
    assert sum_of_even(2) == 0

def test_sum_of_even_three():
    assert sum_of_even(3) == 0

def test_sum_of_even_four():
    assert sum_of_even(4) == 2

def test_sum_of_even_five():
    assert sum_of_even(5) == 2

def test_sum_of_even_six():
    assert sum_of_even(6) == 6

def test_sum_of_even_seven():
    assert sum_of_even(7) == 6

def test_sum_of_even_eight():
    assert sum_of_even(8) == 12

def test_sum_of_even_nine():
    assert sum_of_even(9) == 12

def test_sum_of_even_ten():
    assert sum_of_even(10) == 20

def test_sum_of_even_large():
    assert sum_of_even(100) == 2450

def test_sum_of_even_odd_large():
    assert sum_of_even(101) == 2450

def test_sum_of_even_one_large():
    assert sum_of_even(1000) == 249500

def test_sum_of_even_odd_large():
    assert sum_of_even(1001) == 249500

def test_sum_of_even_max_int():
    assert sum_of_even(sys.maxsize) == (sys.maxsize // 2) * (sys.maxsize // 2 - 1)

def test_sum_of_even_max_int_odd():
    assert sum_of_even(sys.maxsize - 1) == (sys.maxsize // 2) * (sys.maxsize // 2 - 1)

def test_sum_of_even_min_int():
    assert sum_of_even(-sys.maxsize) == 0

def test_sum_of_even_min_int_odd():
    assert sum_of_even(-sys.maxsize + 1) == 0

def test_sum_of_even_min_int_large():
    assert sum_of_even(-1000) == 0

def test_sum_of_even_min_int_odd_large():
    assert sum_of_even(-1001) == 0

def test_sum_of_even_min_int_one():
    assert sum_of_even(-1) == 0

def test_sum_of_even_min_int_two():
    assert sum_of_even(-2) == 0

def test_sum_of_even_min_int_three():
    assert sum_of_even(-3) == 0

def test_sum_of_even_min_int_four():
    assert sum_of_even(-4) == 0

def test_sum_of_even_min_int_five():
    assert sum_of_even(-5) == 0

def test_sum_of_even_min_int_six():
    assert sum_of_even(-6) == 0

def test_sum_of_even_min_int_seven():
    assert sum_of_even(-7) == 0

def test_sum_of_even_min_int_eight():
    assert sum_of_even(-8) == 0

def test_sum_of_even_min_int_nine():
    assert sum_of_even(-9) == 0

def test_sum_of_even_min_int_ten():
    assert sum_of_even(-10) == 0

def test_sum_of_even_min_int_large():
    assert sum_of_even(-100) == 0

def test_sum_of_even_min_int_odd_large():
    assert sum_of_even(-101) == 0

def test_sum_of_even_min_int_one_large():
    assert sum_of_even(-1000) == 0

def test_sum_of_even_min_int_odd_large():
    assert sum_of_even(-1001) == 0

def test_sum_of_even_min_int_max_int():
    assert sum_of_even(-sys.maxsize) == 0

def test_sum_of_even_min_int_max_int_odd():
    assert sum_of_even(-sys.maxsize + 1) == 0

def test_sum_of_even_min_int_max_int_large():
    assert sum_of_even(-1000) == 0

def test_sum_of_even_min_int_max_int_odd_large():
    assert sum_of_even(-1001) == 0

def test_sum_of_even_min_int_max_int_one():
    assert sum_of_even(-1) == 0

def test_sum_of_even_min_int_max_int_two():
    assert sum_of_even(-2) == 0

def test_sum_of_even_min_int_max_int_three():
    assert sum_of_even(-3) == 0

def test_sum_of_even_min_int_max_int_four():
    assert sum_of_even(-4) == 0

def test_sum_of_even_min_int_max_int_five():
    assert sum_of_even(-5) == 0

def test_sum_of_even_min_int_max_int_six():
    assert sum_of_even(-6) == 0

def test_sum_of_even_min_int_max_int_seven():
    assert sum_of_even(-7) == 0

def test_sum_of_even_min_int_max_int_eight():
    assert sum_of_even(-8) == 0

def test_sum_of_even_min_int_max_int_nine():
    assert sum_of_even(-9) == 0

def test_sum_of_even_min_int_max_int_ten():
    assert sum_of_even(-10) == 0

def test_sum_of_even_min_int_max_int_large():
    assert sum_of_even(-100) == 0

def test_sum_of_even_min_int_max_int_odd_large():
    assert sum_of_even(-101) == 0

def test_sum_of_even_min_int_max_int_one_large():
    assert sum_of_even(-1000) == 0

def test_sum_of_even_min_int_max_int_odd_large():
    assert sum_of_even(-1001) == 0

def test_sum_of_even_min_int_max_int_max_int():
    assert sum_of_even(-sys.maxsize) == 0

def test_sum_of_even_min_int_max_int_max_int_odd():
    assert sum_of_even(-sys.maxsize + 1) == 0

def test_sum_of_even_min_int_max_int_max_int_large():
    assert sum_of_even(-1000) == 0

def test_sum_of_even_min_int_max_int_max_int_odd_large():
    assert sum_of_even(-1001) == 0

def test_sum_of_even_min_int_max_int_max_int_one():
    assert sum_of_even(-1) == 0

def test_sum_of_even_min_int_max_int_max_int_two():
    assert sum_of_even(-2) == 0

def test_sum_of_even_min_int_max_int_max_int_three():
    assert sum_of_even(-3) == 0

def test_sum_of_even_min_int_max_int_max_int_four():
    assert sum_of_even(-4) == 0

def test_sum_of_even_min_int_max_int_max_int_five():
    assert sum_of_even(-5) == 0

def test_sum_of_even_min_int_max_int_max_int_six():
    assert sum_of_even(-6) == 0

def test_sum_of_even_min_int_max_int_max_int_seven():
    assert sum_of_even(-7) == 0

def test_sum_of_even_min_int_max_int_max_int_eight():
    assert sum_of_even(-8) == 0

def test_sum_of_even_min_int_max_int_max_int_nine():
    assert sum_of_even(-9) == 0

def test_sum_of_even_min_int_max_int_max_int_ten():
    assert sum_of_even(-10) == 0

def test_sum_of_even_min_int_max_int_max_int_large():
    assert sum_of_even(-100) == 0

def test_sum_of_even_min_int_max_int_max_int_odd_large():
    assert sum_of_even(-101) == 0

def test_sum_of_even_min_int_max_int_max_int_one_large():
    assert sum_of_even(-1000) == 0

def test_sum_of_even_min_int_max_int_max_int_odd_large():
    assert sum_of_even(-1001) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int():
    assert sum_of_even(-sys.maxsize) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_odd():
    assert sum_of_even(-sys.maxsize + 1) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_large():
    assert sum_of_even(-1000) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_odd_large():
    assert sum_of_even(-1001) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_one():
    assert sum_of_even(-1) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_two():
    assert sum_of_even(-2) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_three():
    assert sum_of_even(-3) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_four():
    assert sum_of_even(-4) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_five():
    assert sum_of_even(-5) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_six():
    assert sum_of_even(-6) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_seven():
    assert sum_of_even(-7) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_eight():
    assert sum_of_even(-8) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_nine():
    assert sum_of_even(-9) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_ten():
    assert sum_of_even(-10) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_large():
    assert sum_of_even(-100) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_odd_large():
    assert sum_of_even(-101) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_one_large():
    assert sum_of_even(-1000) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_odd_large():
    assert sum_of_even(-1001) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int():
    assert sum_of_even(-sys.maxsize) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_odd():
    assert sum_of_even(-sys.maxsize + 1) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_large():
    assert sum_of_even(-1000) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_odd_large():
    assert sum_of_even(-1001) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_one():
    assert sum_of_even(-1) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_two():
    assert sum_of_even(-2) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_three():
    assert sum_of_even(-3) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_four():
    assert sum_of_even(-4) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_five():
    assert sum_of_even(-5) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_six():
    assert sum_of_even(-6) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_seven():
    assert sum_of_even(-7) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_eight():
    assert sum_of_even(-8) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_nine():
    assert sum_of_even(-9) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_ten():
    assert sum_of_even(-10) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_large():
    assert sum_of_even(-100) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_odd_large():
    assert sum_of_even(-101) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_one_large():
    assert sum_of_even(-1000) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_odd_large():
    assert sum_of_even(-1001) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_max_int():
    assert sum_of_even(-sys.maxsize) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_max_int_odd():
    assert sum_of_even(-sys.maxsize + 1) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_max_int_large():
    assert sum_of_even(-1000) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_max_int_odd_large():
    assert sum_of_even(-1001) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_max_int_one():
    assert sum_of_even(-1) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_max_int_two():
    assert sum_of_even(-2) == 0

def test_sum_of_even_min_int_max_int_max_int_max_int_max_int_max_int_three():
    assert sum_of_even(-3) == 0

def test_sum_of_even