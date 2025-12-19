import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.colorsys as colorsys
from data.complicated_tests.colorsys import *


def test_data_complicated_tests_colorsys_1():
    colorsys.rgb_to_yiq(1, 0, 0)

def test_29():
    colorsys.ONE_THIRD

def test_31():
    colorsys.ONE_SIXTH

def test_40():
    colorsys.rgb_to_yiq(1, 0, 0)

def test_44():
    colorsys.rgb_to_yiq(1, 0, 0)

def test_46():
    colorsys.rgb_to_yiq(1, 0, 0)

def test_51():
    colorsys.yiq_to_rgb(0.5, 0.5, 0.5)

def test_53():
    colorsys.yiq_to_rgb(0.5, 0.5, 0.5)

def test_55():
    colorsys.rgb_to_hls(1, 0, 0)

def test_60():
    colorsys.rgb_to_hls(1, 0, 0)

def test_65():
    colorsys.rgb_to_hls(1, 0, 0)

def test_75():
    colorsys.rgb_to_hsv(1, 0, 0)

def test_84():
    colorsys.rgb_to_hsv(1, 0, 0)

def test_93():
    colorsys.rgb_to_hsv(1, 0, 0)

def test_95():
    colorsys.rgb_to_hls(1, 0, 0)

def test_97():
    colorsys.rgb_to_hls(1, 0, 0)

def test_99():
    colorsys.hls_to_rgb(0.5, 0.5, 0.5)

def test_103():
    colorsys.hls_to_rgb(0.5, 0.5, 0.5)

def test_105():
    colorsys.hsv_to_rgb(0.5, 0.5, 1)

def test_107():
    colorsys.hsv_to_rgb(0.5, 0.5, 1)

def test_109():
    colorsys.rgb_to_hsv(1, 0, 0)

def test_113():
    colorsys.rgb_to_hsv(1, 0, 0)

def test_117():
    colorsys.rgb

def test_data_complicated_tests_colorsys_2():
    colorsys.rgb_to_yiq(0, 0, 0)

def test_58():
    colorsys.rgb_to_yiq(-0.1, 0, 0)

def test_60():
    colorsys.rgb_to_yiq(0, -0.1, 0)

def test_64():
    colorsys.rgb_to_yiq(0, 0, -0.1)

def test_66():
    colorsys.rgb_to_yiq(1.1, 0, 0)

def test_82():
    colorsys.rgb_to_hls(0, 0, 0)

def test_86():
    colorsys.rgb_to_hls(0.5, 0.5, 0)

def test_92():
    colorsys.rgb_to_hsv(0, 0, 0)

def test_93():
    colorsys.rgb_to_hsv(0.5, 0, 0)

def test_95():
    colorsys.rgb_to_hsv(0, 0.5, 0)

def test_101():
    colorsys.hls_to_rgb(0, 0, 0)

def test_105():
    colorsys.hsv_to_rgb(0, 0, 0)

def test_112():
    colorsys.rgb_to_yiq(1, 1, 0)

def test_131():
    colorsys.rgb_to_hsv(0.5, 0.5, 0)

def test_138():
    colorsys.rgb_to_hsv(0, 0.5, 0)

def test_139():
    colorsys.rgb_to_hsv(0.5, 0, 0)

def test_141():
    colorsys.rgb_to_hsv(0, 0, 0.5)

def test_147():
    colorsys.hsv_to_rgb(0, 0, 0)

def test_155():
    colorsys.hsv_to_rgb(0.5, 0, 0)

def test_157():
    colorsys.hsv_to_rgb(0, 0.5, 0)

def test_159():
    colorsys.hsv_to_rgb(0, 0, 0.5)

def test_162():
    colorsys
