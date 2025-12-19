import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.colorsys as colorsys
from data.complicated_tests.colorsys import *


def test_data_complicated_tests_colorsys_1():
    return colorsys.rgb_to_yiq(0.5, 0.5, 0.5)

def test_data_complicated_tests_colorsys_2():
    colorsys.rgb_to_yiq(0.5, 0.5, 0.5)

def test_55_67():
    colorsys.yiq_to_rgb(0.5, 0.5, 0.5)

def test_76_84():
    colorsys.rgb_to_hls(0.5, 0.5, 0.5)

def test_86_93():
    colorsys.hls_to_rgb(0.5, 0.5, 0.5)

def test_95_97():
    colorsys.rgb_to_hsv(0.5, 0.5, 0.5)

def test_100_103():
    colorsys.hsv_to_rgb(0.5, 0.5, 0.5)

def test_105_107():
    colorsys.rgb_to_hls(0.5, 0.5, 0.5)

def test_110_117():
    colorsys.rgb_to_hsv(0.5, 0.5, 0.5)

def test_126_139():
    colorsys.rgb_to_hls(0.5, 0.5, 0.5)

def test_141_143():
    colorsys.rgb_to_hsv(0.5, 0.5, 0.5)

def test_146_165():
    colorsys.hsv_to_rgb(0.5, 0.5, 0.5)

def test_data_complicated_tests_colorsys_3():
    return colorsys.rgb_to_yiq(-1, 0, 0)

def test_58():
    return colorsys.rgb_to_yiq(0, -1, 0)

def test_60():
    return colorsys.rgb_to_yiq(0, 0, -1)

def test_64():
    return colorsys.rgb_to_hls(1, -1, 0)

def test_66():
    return colorsys.rgb_to_hls(0, 1, -1)

def test_83():
    return colorsys.rgb_to_hls(1.0, 1.0, 1.0)

def test_84():
    return colorsys.rgb_to_hls(1.0, 1.0, 1.0)

def test_86():
    return colorsys.rgb_to_hsv(0, 0, 0)

def test_87():
    return colorsys.rgb_to_hsv(0, 0, 0)

def test_95():
    return colorsys.rgb_to_hsv(1, 0, 1)

def test_97():
    return colorsys.rgb_to_hsv(0, 1, 1)

def test_101():
    return colorsys.hls_to_rgb(0.5, 0.5, 0.0)

def test_105():
    return colorsys.hls_to_rgb(0.5, 0.0, 0.5)

def test_112():
    return colorsys.hls_to_rgb(1.0, 0.5, 0.5)

def test_132():
    return colorsys.hsv_to_rgb(0.5, 0.0, 1.0)

def test_134():
    return colorsys.hsv_to_rgb(0.5, 1.0, 1.0)

def test_139():
    return colorsys.hsv_to_rgb(0.5, 0.0, 1.0)

def test_141():
    return colorsys.hsv_to_rgb(0.5, 0.0, 1.0)

def test_147():
    return colorsys.hsv_to_rgb(0.0, 0.0, 0.0)

def test_155():
    return color

def test_data_complicated_tests_colorsys_4():
    colorsys.rgb_to_yiq(0, 0, 0)

def test_58():
    colorsys.rgb_to_yiq(0, 0, -1)

def test_60():
    colorsys.rgb_to_yiq(0, 0, 2)

def test_64():
    colorsys.rgb_to_yiq(0, -1, 0)

def test_66():
    colorsys.rgb_to_yiq(0, 2, 0)

def test_86():
    colorsys.rgb_to_hls(1, 0, 0)

def test_93():
    colorsys.rgb_to_hls(0, 1, 0)

def test_95():
    colorsys.rgb_to_hls(0, 0, 1)

def test_97():
    colorsys.rgb_to_hls(1, 1, 1)

def test_105():
    colorsys.rgb_to_hsv(1, 0, 0)

def test_141():
    colorsys.rgb_to_hsv(0, 1, 0)

def test_155():
    colorsys.rgb_to_hsv(0, 0, 1)

def test_157():
    colorsys.rgb_to_hsv(1, 1, 1)

def test_159():
    colorsys.rgb_to_hsv(0, 0, -1)

def test_162():
    colorsys.rgb_to_hsv(0, 0, 2)

def test_165():
    colorsys.rgb_to_hsv(2, 0, 0)
