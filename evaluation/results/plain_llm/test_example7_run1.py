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
    assert sum_of_even(3) == 1

def test_sum_of_even_four():
    assert sum_of_even(4) == 2

def test_sum_of_even_five():
    assert sum_of_even(5) == 2

def test_sum_of_even_six():
    assert sum_of_even(6) == 6

def test_sum_of_even_large():
    assert sum_of_even(100) == 2450

def test_sum_of_even_odd_large():
    assert sum_of_even(101) == 2450

def test_sum_of_even_one_hundred():
    assert sum_of_even(100) == 2450

def test_sum_of_even_one_hundred_one():
    assert sum_of_even(101) == 2450

def test_sum_of_even_one_hundred_two():
    assert sum_of_even(102) == 2550

def test_sum_of_even_one_hundred_three():
    assert sum_of_even(103) == 2550

def test_sum_of_even_one_hundred_four():
    assert sum_of_even(104) == 2650

def test_sum_of_even_one_hundred_five():
    assert sum_of_even(105) == 2650

def test_sum_of_even_one_hundred_six():
    assert sum_of_even(106) == 2750

def test_sum_of_even_one_hundred_seven():
    assert sum_of_even(107) == 2750

def test_sum_of_even_one_hundred_eight():
    assert sum_of_even(108) == 2850

def test_sum_of_even_one_hundred_nine():
    assert sum_of_even(109) == 2850

def test_sum_of_even_one_hundred_ten():
    assert sum_of_even(110) == 2950

def test_sum_of_even_one_hundred_eleven():
    assert sum_of_even(111) == 2950

def test_sum_of_even_one_hundred_twelve():
    assert sum_of_even(112) == 3050

def test_sum_of_even_one_hundred_thirteen():
    assert sum_of_even(113) == 3050

def test_sum_of_even_one_hundred_fourteen():
    assert sum_of_even(114) == 3150

def test_sum_of_even_one_hundred_fifteen():
    assert sum_of_even(115) == 3150

def test_sum_of_even_one_hundred_sixteen():
    assert sum_of_even(116) == 3250

def test_sum_of_even_one_hundred_seventeen():
    assert sum_of_even(117) == 3250

def test_sum_of_even_one_hundred_eighteen():
    assert sum_of_even(118) == 3350

def test_sum_of_even_one_hundred_nineteen():
    assert sum_of_even(119) == 3350

def test_sum_of_even_one_hundred_twenty():
    assert sum_of_even(120) == 3450

def test_sum_of_even_one_hundred_twenty_one():
    assert sum_of_even(121) == 3450

def test_sum_of_even_one_hundred_twenty_two():
    assert sum_of_even(122) == 3550

def test_sum_of_even_one_hundred_twenty_three():
    assert sum_of_even(123) == 3550

def test_sum_of_even_one_hundred_twenty_four():
    assert sum_of_even(124) == 3650

def test_sum_of_even_one_hundred_twenty_five():
    assert sum_of_even(125) == 3650

def test_sum_of_even_one_hundred_twenty_six():
    assert sum_of_even(126) == 3750

def test_sum_of_even_one_hundred_twenty_seven():
    assert sum_of_even(127) == 3750

def test_sum_of_even_one_hundred_twenty_eight():
    assert sum_of_even(128) == 3850

def test_sum_of_even_one_hundred_twenty_nine():
    assert sum_of_even(129) == 3850

def test_sum_of_even_one_hundred_thirty():
    assert sum_of_even(130) == 3950

def test_sum_of_even_one_hundred_thirty_one():
    assert sum_of_even(131) == 3950

def test_sum_of_even_one_hundred_thirty_two():
    assert sum_of_even(132) == 4050

def test_sum_of_even_one_hundred_thirty_three():
    assert sum_of_even(133) == 4050

def test_sum_of_even_one_hundred_thirty_four():
    assert sum_of_even(134) == 4150

def test_sum_of_even_one_hundred_thirty_five():
    assert sum_of_even(135) == 4150

def test_sum_of_even_one_hundred_thirty_six():
    assert sum_of_even(136) == 4250

def test_sum_of_even_one_hundred_thirty_seven():
    assert sum_of_even(137) == 4250

def test_sum_of_even_one_hundred_thirty_eight():
    assert sum_of_even(138) == 4350

def test_sum_of_even_one_hundred_thirty_nine():
    assert sum_of_even(139) == 4350

def test_sum_of_even_one_hundred_forty():
    assert sum_of_even(140) == 4450

def test_sum_of_even_one_hundred_forty_one():
    assert sum_of_even(141) == 4450

def test_sum_of_even_one_hundred_forty_two():
    assert sum_of_even(142) == 4550

def test_sum_of_even_one_hundred_forty_three():
    assert sum_of_even(143) == 4550

def test_sum_of_even_one_hundred_forty_four():
    assert sum_of_even(144) == 4650

def test_sum_of_even_one_hundred_forty_five():
    assert sum_of_even(145) == 4650

def test_sum_of_even_one_hundred_forty_six():
    assert sum_of_even(146) == 4750

def test_sum_of_even_one_hundred_forty_seven():
    assert sum_of_even(147) == 4750

def test_sum_of_even_one_hundred_forty_eight():
    assert sum_of_even(148) == 4850

def test_sum_of_even_one_hundred_forty_nine():
    assert sum_of_even(149) == 4850

def test_sum_of_even_one_hundred_fifty():
    assert sum_of_even(150) == 4950

def test_sum_of_even_one_hundred_fifty_one():
    assert sum_of_even(151) == 4950

def test_sum_of_even_one_hundred_fifty_two():
    assert sum_of_even(152) == 5050

def test_sum_of_even_one_hundred_fifty_three():
    assert sum_of_even(153) == 5050

def test_sum_of_even_one_hundred_fifty_four():
    assert sum_of_even(154) == 5150

def test_sum_of_even_one_hundred_fifty_five():
    assert sum_of_even(155) == 5150

def test_sum_of_even_one_hundred_fifty_six():
    assert sum_of_even(156) == 5250

def test_sum_of_even_one_hundred_fifty_seven():
    assert sum_of_even(157) == 5250

def test_sum_of_even_one_hundred_fifty_eight():
    assert sum_of_even(158) == 5350

def test_sum_of_even_one_hundred_fifty_nine():
    assert sum_of_even(159) == 5350

def test_sum_of_even_one_hundred_sixty():
    assert sum_of_even(160) == 5450

def test_sum_of_even_one_hundred_sixty_one():
    assert sum_of_even(161) == 5450

def test_sum_of_even_one_hundred_sixty_two():
    assert sum_of_even(162) == 5550

def test_sum_of_even_one_hundred_sixty_three():
    assert sum_of_even(163) == 5550

def test_sum_of_even_one_hundred_sixty_four():
    assert sum_of_even(164) == 5650

def test_sum_of_even_one_hundred_sixty_five():
    assert sum_of_even(165) == 5650

def test_sum_of_even_one_hundred_sixty_six():
    assert sum_of_even(166) == 5750

def test_sum_of_even_one_hundred_sixty_seven():
    assert sum_of_even(167) == 5750

def test_sum_of_even_one_hundred_sixty_eight():
    assert sum_of_even(168) == 5850

def test_sum_of_even_one_hundred_sixty_nine():
    assert sum_of_even(169) == 5850

def test_sum_of_even_one_hundred_seventy():
    assert sum_of_even(170) == 5950

def test_sum_of_even_one_hundred_seventy_one():
    assert sum_of_even(171) == 5950

def test_sum_of_even_one_hundred_seventy_two():
    assert sum_of_even(172) == 6050

def test_sum_of_even_one_hundred_seventy_three():
    assert sum_of_even(173) == 6050

def test_sum_of_even_one_hundred_seventy_four():
    assert sum_of_even(174) == 6150

def test_sum_of_even_one_hundred_seventy_five():
    assert sum_of_even(175) == 6150

def test_sum_of_even_one_hundred_seventy_six():
    assert sum_of_even(176) == 6250

def test_sum_of_even_one_hundred_seventy_seven():
    assert sum_of_even(177) == 6250

def test_sum_of_even_one_hundred_seventy_eight():
    assert sum_of_even(178) == 6350

def test_sum_of_even_one_hundred_seventy_nine():
    assert sum_of_even(179) == 6350

def test_sum_of_even_one_hundred_eighty():
    assert sum_of_even(180) == 6450

def test_sum_of_even_one_hundred_eighty_one():
    assert sum_of_even(181) == 6450

def test_sum_of_even_one_hundred_eighty_two():
    assert sum_of_even(182) == 6550

def test_sum_of_even_one_hundred_eighty_three():
    assert sum_of_even(183) == 6550

def test_sum_of_even_one_hundred_eighty_four():
    assert sum_of_even(184) == 6650

def test_sum_of_even_one_hundred_eighty_five():
    assert sum_of_even(185) == 6650

def test_sum_of_even_one_hundred_eighty_six():
    assert sum_of_even(186) == 6750

def test_sum_of_even_one_hundred_eighty_seven():
    assert sum_of_even(187) == 6750

def test_sum_of_even_one_hundred_eighty_eight():
    assert sum_of_even(188) == 6850

def test_sum_of_even_one_hundred_eighty_nine():
    assert sum_of_even(189) == 6850

def test_sum_of_even_one_hundred_ninety():
    assert sum_of_even(190) == 6950

def test_sum_of_even_one_hundred_ninety_one():
    assert sum_of_even(191) == 6950

def test_sum_of_even_one_hundred_ninety_two():
    assert sum_of_even(192) == 7050

def test_sum_of_even_one_hundred_ninety_three():
    assert sum_of_even(193) == 7050

def test_sum_of_even_one_hundred_ninety_four():
    assert sum_of_even(194) == 7150

def test_sum_of_even_one_hundred_ninety_five():
    assert sum_of_even(195) == 7150

def test_sum_of_even_one_hundred_ninety_six():
    assert sum_of_even(196) == 7250