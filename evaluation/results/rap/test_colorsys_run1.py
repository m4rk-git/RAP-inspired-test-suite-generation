import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.colorsys as colorsys
from data.complicated_tests.colorsys import *


def test_data_complicated_tests_colorsys_1():
    # Test line: 24
    __all__ = ["rgb_to_yiq","yiq_to_rgb","rgb_to_hls","hls_to_rgb","rgb_to_hsv","hsv_to_rgb"]
    
    # Test line: 29
    ONE_THIRD = 1.0/3.0
    
    # Test line: 40
    def rgb_to_yiq(r, g, b):
        y = 0.30*r + 0.59*g + 0.11*b
        i = 0.74*(r-y) - 0.27*(b-y)
        q = 0.48*(r-y) + 0.41*(b-y)
        return (y, i, q)
    
    # Test line: 46
    def yiq_to_rgb(y, i, q):
        r = y + 0.9468822170900693*i + 0.6235565819861433*q
        g = y - 0.27478764629897834*i - 0.6356910791873801*q
        b = y - 1.1085450346420322*i + 1.7090069284064666*q
        if r < 0.0:
            r = 0.0
        if g < 0.0:
            g = 0.0
        if b < 0.0:
            b = 0.0
        if r > 1.0:
            r = 1.0
        if g > 1.0:
            g = 1.0
        if b > 1.0:
            b = 1.0
        return (r, g, b)
    
    # Test line: 55
    def rgb_to_hls(r, g, b):
        maxc = max(r, g, b)
        minc = min(r, g, b)
        sumc = (maxc+minc)
        rangec = (maxc-minc)

def test_data_complicated_tests_colorsys_2():
    colorsys.rgb_to_yiq(1, 0, 0)
def test_44():
    colorsys.rgb_to_yiq(1, 0, 0)
def test_51():
    colorsys.yiq_to_rgb(1, 0, 0)
def test_53():
    colorsys.yiq_to_rgb(1, 0, 0)
def test_55():
    colorsys.rgb_to_hls(1, 0, 0)
def test_67():
    colorsys.rgb_to_hls(1, 0, 0)
def test_76():
    colorsys.rgb_to_hsv(1, 0, 0)
def test_84():
    colorsys.rgb_to_hsv(1, 0, 0)
def test_86():
    colorsys.hls_to_rgb(1, 0, 1)
def test_93():
    colorsys.hls_to_rgb(1, 1, 0)
def test_95():
    colorsys.rgb_to_hls(1, 1, 0)
def test_97():
    colorsys.rgb_to_hls(1, 1, 1)
def test_100():
    colorsys.hsv_to_rgb(0, 0, 0)
def test_103():
    colorsys.hsv_to_rgb(1, 1, 1)
def test_105():
    colorsys.hsv_to_rgb(1, 0, 0)
def test_107():
    colorsys.hsv_to_rgb(1, 0, 1)
def test_110():
    colorsys._v(0, 1, 0)
def test_117():
    colorsys._v(0, 1, 0.5)
def test_126():
    colorsys.rgb_to_hsv(1, 0, 0)
def test_139():
    colorsys.rgb_to_hsv(1, 0, 0)
def test_141():
    colorsys.hsv_to_rgb(0, 0, 0)
def test_143():
    colorsys.hsv_to_rgb(1, 1, 0)
def test_146():
    colorsys.hsv_to_rgb(0, 1, 1)

def test_data_complicated_tests_colorsys_3():
    colorsys.rgb_to_yiq(0.0, 0.0, 0.0)

def test_58():
    colorsys.rgb_to_yiq(1.0, 1.0, 1.0)

def test_60():
    colorsys.rgb_to_yiq(1.0, 0.0, 0.0)

def test_62():
    colorsys.rgb_to_yiq(0.0, 1.0, 0.0)

def test_64():
    colorsys.rgb_to_yiq(0.0, 0.0, 1.0)

def test_66():
    colorsys.rgb_to_yiq(-0.1, 0.0, 0.0)

def test_86():
    colorsys.rgb_to_hls(0.5, 0.5, 0.5)

def test_92():
    colorsys.rgb_to_hls(1.0, 0.0, 0.0)

def test_93():
    colorsys.rgb_to_hls(0.0, 1.0, 0.0)

def test_95():
    colorsys.rgb_to_hls(0.0, 0.0, 1.0)

def test_105():
    colorsys.rgb_to_hsv(0.5, 0.5, 0.5)

def test_131():
    colorsys.rgb_to_hsv(1.0, 0.0, 0.0)

def test_138():
    colorsys.rgb_to_hsv(0.0, 1.0, 0.0)

def test_139():
    colorsys.rgb_to_hsv(0.0, 0.0, 1.0)

def test_141():
    colorsys.rgb_to_hsv(0.5, 0.5, 0.5)

def test_156():
    colorsys.hsv_to_rgb(1.5, 0.5, 0.5)

def test_165():
    colorsys.hsv_to_rgb(0.5, 0.5, 0.5)

def test_data_complicated_tests_colorsys_4():
    colorsys.rgb_to_yiq(-1, 0, 0)

def test_58():
    colorsys.rgb_to_yiq(0, -1, 0)

def test_60():
    colorsys.rgb_to_yiq(0, 0, -1)

def test_62():
    colorsys.rgb_to_yiq(1, 0, 0)

def test_64():
    colorsys.rgb_to_yiq(0, 1, 0)

def test_66():
    colorsys.rgb_to_yiq(0, 0, 1)

def test_86():
    colorsys.rgb_to_hls(1, 1, 1)

def test_100_103():
    assert colorsys.hls_to_rgb(0.5, 0.5, 0.5) == (0.5, 0.5, 0.5)

def test_105_107():
    assert colorsys.hls_to_rgb(0, 0, 0) == (0, 0, 0)

def test_114():
    colorsys._v(0, 1, 0.5)

def test_117():
    colorsys._v(0, 1, 1.5)

def test_157():
    colorsys.hsv_to_rgb(0, 0, 0)

def test_159():
    colorsys.hsv_to_rgb(1, 0, 1)

def test_162_165():
    assert colorsys.hsv_to_rgb(0.5, 0.5, 0.5) == (0.5, 0.5, 0.5)

def test_data_complicated_tests_colorsys_5():
    colorsys.rgb_to_yiq(0.1, 0.2, -0.1)  # A value less than 0 to trigger line 56

def test_58():
    colorsys.rgb_to_yiq(0.1, 0.2, -0.1)  # A value less than 0 to trigger line 58

def test_60():
    colorsys.rgb_to_yiq(0.1, 0.2, -0.1)  # A value less than 0 to trigger line 60

def test_62():
    colorsys.rgb_to_yiq(0.1, 0.2, -0.1)  # A value less than 0 to trigger line 62

def test_64():
    colorsys.rgb_to_yiq(0.1, 0.2, -0.1)  # A value less than 0 to trigger line 64

def test_66():
    colorsys.rgb_to_yiq(0.1, 0.2, -0.1)  # A value less than 0 to trigger line 66

def test_86():
    colorsys.rgb_to_hsl(-0.1, 0.2, 0.3)  # A value less than 0 to trigger line 86

def test_105():
    colorsys.hls_to_rgb(0.4, 0.3, 1.2)  # A value greater than 1 to trigger line 105

def test_157():
    colorsys.hsv_to_rgb(0.4, -0.2, 0.3)  # A value less than 0 to trigger line 157

def test_159():
    colorsys.hsv_to_rgb(0.4, 1.2, 0.3)  # A value greater than 1 to trigger line 159

def test_162():
    colorsys.hsv_to_rgb(0.4, 0.2, -0.1)  # A value less than 0 to trigger line 162

def test_163():
    colorsys.hsv_to_rgb(0.4, 0.2, 1.2)  # A value greater
