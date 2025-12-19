import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.colorsys as colorsys
from data.complicated_tests.colorsys import *


def test_data_complicated_tests_colorsys_1():
    code = (
        "import colorsys\n"
        "colorsys.rgb_to_yiq(1.0, 0.0, 1.0)\n"
        "colorsys.yiq_to_rgb(0.8571428571428572, 0.4999999999999999, 0.0)\n"
        "colorsys.rgb_to_hls(1.0, 1.0, 0.0)\n"
        "colorsys.hls_to_rgb(0.16666666666666666, 0.5, 1.0)\n"
        "colorsys.rgb_to_hsv(1.0, 0.0, 1.0)\n"
        "colorsys.hsv_to_rgb(0.16666666666666666, 0.8333333333333334, 1.0)\n"
    )
    with open("temp.py", "w") as f:
        f.write(code)
    exec(open("temp.py").read())

def test_data_complicated_tests_colorsys_2():
    colorsys.rgb_to_yiq(1.0, 1.0, 1.0)

def test_02():
    colorsys.yiq_to_rgb(1.0, 1.0, 1.0)

def test_03():
    colorsys.rgb_to_hls(1.0, 1.0, 1.0)

def test_04():
    colorsys.hls_to_rgb(1.0, 1.0, 1.0)

def test_05():
    colorsys.rgb_to_hsv(1.0, 1.0, 1.0)

def test_06():
    colorsys.hsv_to_rgb(1.0, 1.0, 1.0)

def test_07():
    colorsys.rgb_to_yiq(0.0, 0.0, 0.0)

def test_08():
    colorsys.yiq_to_rgb(0.0, 0.0, 0.0)

def test_09():
    colorsys.rgb_to_hls(0.0, 0.0, 0.0)

def test_10():
    colorsys.hls_to_rgb(0.0, 0.0, 0.0)

def test_11():
    colorsys.rgb_to_hsv(0.0, 0.0, 0.0)

def test_12():
    colorsys.hsv_to_rgb(0.0, 0.0, 0.0)

def test_data_complicated_tests_colorsys_3():
    colorsys.rgb_to_yiq(-0.1, 0.5, 0.2)

def test_58():
    colorsys.rgb_to_yiq(0.5, -0.1, 0.2)

def test_60():
    colorsys.rgb_to_yiq(0.5, 0.2, -0.1)

def test_64():
    colorsys.rgb_to_hls(-0.1, 0.5, 0.2)

def test_83_84():
    colorsys.rgb_to_hls(0.5, 0.5, 0.5)

def test_86_93():
    colorsys.rgb_to_hls(0.5, 0.5, 0.5)

def test_95_97():
    colorsys.rgb_to_hls(0.5, 0.5, 0.5)

def test_103():
    colorsys.hls_to_rgb(0.5, 1.1, 0.5)

def test_116():
    colorsys.hls_to_rgb(0.5, 0.5, 1.5)

def test_132_139():
    colorsys.rgb_to_hsv(-0.1, 0.5, 0.2)

def test_141_143():
    colorsys.rgb_to_hsv(0.5, 0.5, 0.5)

def test_156_165():
    colorsys.hsv_to_rgb(0.5, 0.5, 1.5)

def test_data_complicated_tests_colorsys_4():
    colorsys.rgb_to_yiq(0.0, -0.1, 0.0)

def test_58():
    colorsys.rgb_to_yiq(0.0, 0.0, -0.1)

def test_60():
    colorsys.rgb_to_yiq(0.0, 0.0, 1.1)

def test_64():
    colorsys.hls_to_rgb(0.0, 0.5, 1.1)

def test_86():
    colorsys.rgb_to_hls(1.1, 0.5, 0.5)

def test_91():
    colorsys.rgb_to_hls(0.5, 0.5, 1.1)

def test_95():
    colorsys.rgb_to_hls(0.5, 1.1, 0.5)

def test_137():
    colorsys.rgb_to_hsv(0.0, -0.1, 0.0)

def test_141():
    colorsys.rgb_to_hsv(0.0, 0.0, -0.1)

def test_157():
    colorsys.hsv_to_rgb(0.0, 0.5, 1.1)

def test_159():
    colorsys.hsv_to_rgb(0.5, 0.5, 1.1)

def test_162():
    colorsys.hsv_to_rgb(0.5, -0.1, 0.5)

def test_163():
    colorsys.hsv_to_rgb(0.5, 0.0, -0.1)

def test_164():
    colorsys.hsv_to_rgb(0.5, 0.5, -0.1)

def test_165():
    colorsys.hsv_to_rgb(0.5, 0.5, 1.1)

def test_data_complicated_tests_colorsys_5():
    assert colorsys.rgb_to_yiq(0, 0, -0.1) == (0, 0, 0)

def test_58():
    assert colorsys.rgb_to_yiq(0, 0, -0.1) == (0, 0, 0)

def test_60():
    assert colorsys.rgb_to_yiq(0, 0, 1.1) == (1, 0, 0)

def test_64():
    assert colorsys.rgb_to_yiq(0, 0, 1.1) == (1, 0, 0)

def test_84():
    assert colorsys.rgb_to_hls(0, 0, 0) == (0, 0, 0)

def test_137():
    assert colorsys.rgb_to_hsv(0, 0, 0) == (0, 0, 0)

def test_141():
    assert colorsys.rgb_to_hsv(0, 0, 0) == (0, 0, 0)

def test_157():
    assert colorsys.hsv_to_rgb(1, 1, 1) == (1, 0, 0)

def test_159():
    assert colorsys.hsv_to_rgb(1, 1, 1) == (1, 0, 0)

def test_162():
    assert colorsys.hsv_to_rgb(0.5, 0.5, 0.5) == (0.5, 0.5, 0.0)

def test_163():
    assert colorsys.hsv_to_rgb(0.5, 0.5, 0.5) == (0.5, 0.5, 0.0)

def test_164():
    assert colorsys.hsv_to_rgb(0.5, 0.5, 0.5) == (0.5, 0.0, 0.5)

def test_165():
    assert colorsys.hsv_to_rgb(0.5, 0.5, 0.5) == (0.5, 0.0, 0.5)

def test_data_complicated_tests_colorsys_6():
    return colorsys.rgb_to_yiq(-0.1, 0.5, 0.2)

def test_58():
    return colorsys.rgb_to_yiq(0.4, -0.3, 0.2)

def test_60():
    return colorsys.rgb_to_yiq(0.4, 0.5, -0.3)

def test_64():
    return colorsys.rgb_to_hsv(0.4, -0.3, 0.2)

def test_84():
    return colorsys.rgb_to_hls(0.4, -0.3, 0.2)

def test_137():
    return colorsys.rgb_to_hsv(0.4, 0.5, -0.3)

def test_141():
    return colorsys.rgb_to_hsv(0.4, -0.3, 0.2)

def test_157():
    return colorsys.rgb_to_yiq(-0.1, 0.5, 0.2)

def test_159():
    return colorsys.rgb_to_yiq(0.4, -0.3, 0.2)

def test_162():
    return colorsys.rgb_to_yiq(0.4, 0.5, -0.3)

def test_163():
    return colorsys.rgb_to_yiq(0.4, -0.3, 0.2)

def test_164():
    return colorsys.rgb_to_yiq(0.4, 0.5, -0.3)

def test_165():
    return colorsys.rgb_to_yiq(0.4, -0.3, 0.2)
