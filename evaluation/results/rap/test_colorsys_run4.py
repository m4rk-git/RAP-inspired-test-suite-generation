import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.colorsys as colorsys
from data.complicated_tests.colorsys import *


def test_data_complicated_tests_colorsys_1():
    colorsys.rgb_to_yiq(0, 0, 0)

def test_029_31():
    colorsys.ONE_THIRD

def test_040_44():
    colorsys.rgb_to_yiq(1, 0, 0)

def test_046():
    colorsys.yiq_to_rgb(1, 0, 0)

def test_051_53():
    colorsys._v(0, 0, 0)

def test_055_67():
    colorsys.hls_to_rgb(0.5, 0.5, 1)

def test_075_84():
    colorsys.rgb_to_hls(1, 1, 1)

def test_086_93():
    colorsys.rgb_to_hsv(0, 1, 0)

def test_095_97():
    colorsys.rgb_to_hls(0, 1, 0)

def test_099_103():
    colorsys.rgb_to_hsv(1, 0, 0)

def test_105_107():
    colorsys.hsv_to_rgb(0.5, 0.5, 1)

def test_109_117():
    colorsys.hsv_to_rgb(0.5, 0.5, 1)

def test_125_139():
    colorsys.rgb_to_hsv(1, 1, 0)

def test_141_143():
    colorsys.hsv_to_rgb(0, 0, 1)

def test_145_165():
    colorsys.hsv_to_rgb(0.5, 0.5, 0.5)

def test_data_complicated_tests_colorsys_2():
    colorsys.rgb_to_yiq(0,0,0)

def test_058():
    colorsys.rgb_to_yiq(-1,0,0)

def test_060():
    colorsys.rgb_to_yiq(0,-1,0)

def test_062():
    colorsys.rgb_to_yiq(0,0,-1)

def test_064():
    colorsys.rgb_to_yiq(0,0,2)

def test_066():
    colorsys.rgb_to_hls(0,0,0)

def test_086():
    colorsys.rgb_to_hls(0,0,0.5)

def test_091():
    colorsys.rgb_to_hls(0,0,1)

def test_095():
    colorsys.rgb_to_hsv(0,0,0)

def test_101():
    colorsys.rgb_to_hsv(0,0,0.5)

def test_105():
    colorsys.rgb_to_hsv(0,0,1)

def test_131():
    colorsys.rgb_to_hsv(1,1,1)

def test_141():
    colorsys.rgb_to_hsv(1,1,0.5)

def test_155():
    colorsys.rgb_to_hsv(1,0,0)

def test_157():
    colorsys.rgb_to_hsv(0,1,0)

def test_159():
    colorsys.rgb_to_hsv(0,0,1)

def test_162():
    colorsys.rgb_to_hsv(0,0,0)

def test_163():
    colorsys.rgb_to_hsv(0,0,0.5)

def test_164():
    colorsys.rgb_to_hsv(0,0,1)

def test_165():
    colorsys.rgb_to_hsv(1,1,1)

def test_data_complicated_tests_colorsys_3():
    colorsys.rgb_to_yiq(0, 0, 0)

def test_58():
    colorsys.rgb_to_yiq(-1, 0, 0)

def test_60():
    colorsys.rgb_to_yiq(0, -1, 0)

def test_62():
    colorsys.rgb_to_yiq(0, 0, -1)

def test_64():
    colorsys.rgb_to_yiq(2, 0, 0)

def test_66():
    colorsys.rgb_to_yiq(0, 2, 0)

def test_86():
    colorsys.rgb_to_hls(1, 2, 0)

def test_91():
    colorsys.rgb_to_hls(0, 2, 0)

def test_101():
    colorsys.rgb_to_hsv(1, 2, 0)

def test_105():
    colorsys.rgb_to_hsv(0, 2, 0)

def test_155():
    colorsys.hsv_to_rgb(-1, 1, 1)

def test_157():
    colorsys.hsv_to_rgb(1, -1, 1)

def test_159():
    colorsys.hsv_to_rgb(1, 1, -1)

def test_162():
    colorsys.hsv_to_rgb(0.5, 0, 0)

def test_163():
    colorsys.hsv_to_rgb(1.5, 0, 0)

def test_164():
    colorsys.hsv_to_rgb(-0.5, 0, 0)

def test_165():
    colorsys.hsv_to_rgb(0.5, 0, 1)

def test_data_complicated_tests_colorsys_4(colorsys):
    colorsys.rgb_to_yiq(-1, 0, 0)

def test_58(colorsys):
    colorsys.rgb_to_yiq(0, -1, 0)

def test_60(colorsys):
    colorsys.rgb_to_yiq(0, 0, -1)

def test_62(colorsys):
    colorsys.rgb_to_yiq(2, 0, 0)

def test_64(colorsys):
    colorsys.rgb_to_yiq(0, 2, 0)

def test_66(colorsys):
    colorsys.rgb_to_yiq(0, 0, 2)

def test_91(colorsys):
    colorsys.rgb_to_hls(0, 0, 0)

def test_101(colorsys):
    colorsys.hsv_to_rgb(0, 0, 0)

def test_105(colorsys):
    colorsys.hsv_to_rgb(0, 0, 1.1)

def test_141(colorsys):
    colorsys.rgb_to_hsv(0, 0, 0)

def test_157(colorsys):
    colorsys.hsv_to_rgb(1, 0.5, 0.5)

def test_159(colorsys):
    colorsys.hsv_to_rgb(0.5, 0.5, 1)

def test_162(colorsys):
    colorsys.hsv_to_rgb(0.5, 0.5, 1.1)

def test_163(colorsys):
    colorsys.hsv_to_rgb(0.5, 0.5, -0.1)

def test_data_complicated_tests_colorsys_5():
    colorsys.rgb_to_yiq(-1, 0, 0)

def test_58():
    colorsys.rgb_to_yiq(0, -1, 0)

def test_60():
    colorsys.rgb_to_yiq(0, 0, -1)

def test_62():
    colorsys.rgb_to_yiq(2, 0, 0)

def test_64():
    colorsys.rgb_to_yiq(0, 2, 0)

def test_66():
    colorsys.rgb_to_yiq(0, 0, 2)

def test_91():
    colorsys.rgb_to_hls(-1, 0, 0)

def test_101():
    colorsys.rgb_to_hls(1, 0, 0)

def test_105():
    colorsys.rgb_to_hls(1, 0, 0)

def test_141():
    colorsys.rgb_to_hsv(-1, 0, 0)

def test_157():
    colorsys.hsv_to_rgb(-1, 0, 1)

def test_159():
    colorsys.hsv_to_rgb(1, 0, -1)

def test_162():
    colorsys.hsv_to_rgb(1, -1, 1)

def test_163():
    colorsys.hsv_to_rgb(1, 1, -1)

def test_164():
    colorsys.hsv_to_rgb(1, 1, 2)

def test_165():
    colorsys.hsv_to_rgb(1, 2, 1)
