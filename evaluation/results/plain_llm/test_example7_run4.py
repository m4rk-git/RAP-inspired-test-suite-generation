from data.assignment_tests.example7 import *
import pytest
import sys

def test_sum_of_even_positive():
    assert sum_of_even(5) == 6, "Sum of even numbers up to 5 should be 6"

def test_sum_of_even_zero():
    assert sum_of_even(0) == 0, "Sum of even numbers up to 0 should be 0"

def test_sum_of_even_negative():
    assert sum_of_even(-3) == 0, "Sum of even numbers up to negative should be 0"

def test_sum_of_even_one():
    assert sum_of_even(1) == 0, "Sum of even numbers up to 1 should be 0"

def test_sum_of_even_large():
    assert sum_of_even(100) == 2450, "Sum of even numbers up to 100 should be 2450"

def test_sum_of_even_odd():
    assert sum_of_even(6) == 12, "Sum of even numbers up to 6 should be 12"

def test_sum_of_even_one_even():
    assert sum_of_even(2) == 0, "Sum of even numbers up to 2 should be 0"

def test_sum_of_even_one_odd():
    assert sum_of_even(3) == 2, "Sum of even numbers up to 3 should be 2"

def test_sum_of_even_two():
    assert sum_of_even(4) == 6, "Sum of even numbers up to 4 should be 6"

def test_sum_of_even_three():
    assert sum_of_even(7) == 12, "Sum of even numbers up to 7 should be 12"

def test_sum_of_even_four():
    assert sum_of_even(8) == 20, "Sum of even numbers up to 8 should be 20"

def test_sum_of_even_five():
    assert sum_of_even(9) == 24, "Sum of even numbers up to 9 should be 24"

def test_sum_of_even_six():
    assert sum_of_even(10) == 30, "Sum of even numbers up to 10 should be 30"

def test_sum_of_even_seven():
    assert sum_of_even(11) == 36, "Sum of even numbers up to 11 should be 36"

def test_sum_of_even_eight():
    assert sum_of_even(12) == 42, "Sum of even numbers up to 12 should be 42"

def test_sum_of_even_nine():
    assert sum_of_even(13) == 50, "Sum of even numbers up to 13 should be 50"

def test_sum_of_even_ten():
    assert sum_of_even(14) == 56, "Sum of even numbers up to 14 should be 56"

def test_sum_of_even_eleven():
    assert sum_of_even(15) == 66, "Sum of even numbers up to 15 should be 66"

def test_sum_of_even_twelve():
    assert sum_of_even(16) == 72, "Sum of even numbers up to 16 should be 72"

def test_sum_of_even_thirteen():
    assert sum_of_even(17) == 80, "Sum of even numbers up to 17 should be 80"

def test_sum_of_even_fourteen():
    assert sum_of_even(18) == 88, "Sum of even numbers up to 18 should be 88"

def test_sum_of_even_fifteen():
    assert sum_of_even(19) == 96, "Sum of even numbers up to 19 should be 96"

def test_sum_of_even_sixteen():
    assert sum_of_even(20) == 108, "Sum of even numbers up to 20 should be 108"

def test_sum_of_even_seventeen():
    assert sum_of_even(21) == 118, "Sum of even numbers up to 21 should be 118"

def test_sum_of_even_eighteen():
    assert sum_of_even(22) == 126, "Sum of even numbers up to 22 should be 126"

def test_sum_of_even_nineteen():
    assert sum_of_even(23) == 136, "Sum of even numbers up to 23 should be 136"

def test_sum_of_even_twenty():
    assert sum_of_even(24) == 144, "Sum of even numbers up to 24 should be 144"

def test_sum_of_even_twenty_one():
    assert sum_of_even(25) == 156, "Sum of even numbers up to 25 should be 156"

def test_sum_of_even_twenty_two():
    assert sum_of_even(26) == 168, "Sum of even numbers up to 26 should be 168"

def test_sum_of_even_twenty_three():
    assert sum_of_even(27) == 180, "Sum of even numbers up to 27 should be 180"

def test_sum_of_even_twenty_four():
    assert sum_of_even(28) == 192, "Sum of even numbers up to 28 should be 192"

def test_sum_of_even_twenty_five():
    assert sum_of_even(29) == 204, "Sum of even numbers up to 29 should be 204"

def test_sum_of_even_twenty_six():
    assert sum_of_even(30) == 216, "Sum of even numbers up to 30 should be 216"

def test_sum_of_even_twenty_seven():
    assert sum_of_even(31) == 230, "Sum of even numbers up to 31 should be 230"

def test_sum_of_even_twenty_eight():
    assert sum_of_even(32) == 240, "Sum of even numbers up to 32 should be 240"

def test_sum_of_even_twenty_nine():
    assert sum_of_even(33) == 252, "Sum of even numbers up to 33 should be 252"

def test_sum_of_even_thirty():
    assert sum_of_even(34) == 264, "Sum of even numbers up to 34 should be 264"

def test_sum_of_even_thirty_one():
    assert sum_of_even(35) == 278, "Sum of even numbers up to 35 should be 278"

def test_sum_of_even_thirty_two():
    assert sum_of_even(36) == 290, "Sum of even numbers up to 36 should be 290"

def test_sum_of_even_thirty_three():
    assert sum_of_even(37) == 306, "Sum of even numbers up to 37 should be 306"

def test_sum_of_even_thirty_four():
    assert sum_of_even(38) == 320, "Sum of even numbers up to 38 should be 320"

def test_sum_of_even_thirty_five():
    assert sum_of_even(39) == 336, "Sum of even numbers up to 39 should be 336"

def test_sum_of_even_thirty_six():
    assert sum_of_even(40) == 350, "Sum of even numbers up to 40 should be 350"

def test_sum_of_even_thirty_seven():
    assert sum_of_even(41) == 366, "Sum of even numbers up to 41 should be 366"

def test_sum_of_even_thirty_eight():
    assert sum_of_even(42) == 380, "Sum of even numbers up to 42 should be 380"

def test_sum_of_even_thirty_nine():
    assert sum_of_even(43) == 396, "Sum of even numbers up to 43 should be 396"

def test_sum_of_even_forty():
    assert sum_of_even(44) == 410, "Sum of even numbers up to 44 should be 410"

def test_sum_of_even_forty_one():
    assert sum_of_even(45) == 426, "Sum of even numbers up to 45 should be 426"

def test_sum_of_even_forty_two():
    assert sum_of_even(46) == 440, "Sum of even numbers up to 46 should be 440"

def test_sum_of_even_forty_three():
    assert sum_of_even(47) == 456, "Sum of even numbers up to 47 should be 456"

def test_sum_of_even_forty_four():
    assert sum_of_even(48) == 470, "Sum of even numbers up to 48 should be 470"

def test_sum_of_even_forty_five():
    assert sum_of_even(49) == 486, "Sum of even numbers up to 49 should be 486"

def test_sum_of_even_forty_six():
    assert sum_of_even(50) == 500, "Sum of even numbers up to 50 should be 500"

def test_sum_of_even_forty_seven():
    assert sum_of_even(51) == 516, "Sum of even numbers up to 51 should be 516"

def test_sum_of_even_forty_eight():
    assert sum_of_even(52) == 530, "Sum of even numbers up to 52 should be 530"

def test_sum_of_even_forty_nine():
    assert sum_of_even(53) == 546, "Sum of even numbers up to 53 should be 546"

def test_sum_of_even_fifty():
    assert sum_of_even(54) == 560, "Sum of even numbers up to 54 should be 560"

def test_sum_of_even_fifty_one():
    assert sum_of_even(55) == 576, "Sum of even numbers up to 55 should be 576"

def test_sum_of_even_fifty_two():
    assert sum_of_even(56) == 590, "Sum of even numbers up to 56 should be 590"

def test_sum_of_even_fifty_three():
    assert sum_of_even(57) == 606, "Sum of even numbers up to 57 should be 606"

def test_sum_of_even_fifty_four():
    assert sum_of_even(58) == 620, "Sum of even numbers up to 58 should be 620"

def test_sum_of_even_fifty_five():
    assert sum_of_even(59) == 636, "Sum of even numbers up to 59 should be 636"

def test_sum_of_even_fifty_six():
    assert sum_of_even(60) == 650, "Sum of even numbers up to 60 should be 650"

def test_sum_of_even_fifty_seven():
    assert sum_of_even(61) == 666, "Sum of even numbers up to 61 should be 666"

def test_sum_of_even_fifty_eight():
    assert sum_of_even(62) == 680, "Sum of even numbers up to 62 should be 680"

def test_sum_of_even_fifty_nine():
    assert sum_of_even(63) == 696, "Sum of even numbers up to 63 should be 696"

def test_sum_of_even_sixty():
    assert sum_of_even(64) == 710, "Sum of even numbers up to 64 should be 710"

def test_sum_of_even_sixty_one():
    assert sum_of_even(65) == 726, "Sum of even numbers up to 65 should be 726"

def test_sum_of_even_sixty_two():
    assert sum_of_even(66) == 740, "Sum of even numbers up to 66 should be 740"

def test_sum_of_even_sixty_three():
    assert sum_of_even(67) == 756, "Sum of even numbers up to 67 should be 756"

def test_sum_of_even_sixty_four():
    assert sum_of_even(68) == 770, "Sum of even numbers up to 68 should be 770"

def test_sum_of_even_sixty_five():
    assert sum_of_even(69) == 786, "Sum of even numbers up to 69 should be 786"

def test_sum_of_even_sixty_six():
    assert sum_of_even(70) == 800, "Sum of even numbers up to 70 should be 800"

def test_sum_of_even_sixty_seven():
    assert sum_of_even(71) == 816, "Sum of even numbers up to 71 should be 816"

def test_sum_of_even_sixty_eight():
    assert sum_of_even(72) == 830, "Sum of even numbers up to 72 should be 830"

def test_sum_of_even_sixty_nine():
    assert sum_of_even(73) == 846, "Sum of even numbers up to 73 should be 846"

def test_sum_of_even_seventy():
    assert sum_of_even(74) == 860,