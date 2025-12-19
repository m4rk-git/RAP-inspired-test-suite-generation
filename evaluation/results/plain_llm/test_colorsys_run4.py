from data.complicated_tests.colorsys import *
import pytest
import numpy as np

def test_rgb_to_yiq():
    assert rgb_to_yiq(0, 0, 0) == (0, 0, 0)
    assert rgb_to_yiq(1, 1, 1) == (1, 0, 0)
    assert rgb_to_yiq(0.5, 0.5, 0.5) == (0.5, 0, 0)
    assert rgb_to_yiq(1, 0, 0) == (0.3, 0.74, 0)
    assert rgb_to_yiq(0, 1, 0) == (0.59, 0, 0.41)
    assert rgb_to_yiq(0, 0, 1) == (0.11, 0, 0.74)

def test_yiq_to_rgb():
    assert yiq_to_rgb(0, 0, 0) == (0, 0, 0)
    assert yiq_to_rgb(1, 0, 0) == (1, 0, 0)
    assert yiq_to_rgb(0.5, 0, 0) == (0.5, 0.5, 0.5)
    assert yiq_to_rgb(0.3, 0.74, 0) == (1, 0, 0)
    assert yiq_to_rgb(0.59, 0, 0.41) == (0, 1, 0)
    assert yiq_to_rgb(0.11, 0, 0.74) == (0, 0, 1)

def test_rgb_to_hls():
    assert rgb_to_hls(0, 0, 0) == (0, 0, 0)
    assert rgb_to_hls(1, 1, 1) == (0, 1, 1)
    assert rgb_to_hls(0.5, 0.5, 0.5) == (0.3333333333333333, 0.5, 0.5)
    assert rgb_to_hls(1, 0, 0) == (0, 0.5, 1)
    assert rgb_to_hls(0, 1, 0) == (0.3333333333333333, 0.5, 1)
    assert rgb_to_hls(0, 0, 1) == (0.6666666666666666, 0.5, 1)

def test_hls_to_rgb():
    assert hls_to_rgb(0, 0, 0) == (0, 0, 0)
    assert hls_to_rgb(0, 1, 1) == (1, 1, 1)
    assert hls_to_rgb(0.3333333333333333, 0.5, 0.5) == (0.5, 0.5, 0.5)
    assert hls_to_rgb(0, 0.5, 1) == (1, 0, 0)
    assert hls_to_rgb(0.3333333333333333, 0.5, 1) == (0, 1, 0)
    assert hls_to_rgb(0.6666666666666666, 0.5, 1) == (0, 0, 1)

def test_rgb_to_hsv():
    assert rgb_to_hsv(0, 0, 0) == (0, 0, 0)
    assert rgb_to_hsv(1, 1, 1) == (0, 0, 1)
    assert rgb_to_hsv(0.5, 0.5, 0.5) == (0.3333333333333333, 0, 0.5)
    assert rgb_to_hsv(1, 0, 0) == (0, 1, 1)
    assert rgb_to_hsv(0, 1, 0) == (0.3333333333333333, 1, 1)
    assert rgb_to_hsv(0, 0, 1) == (0.6666666666666666, 1, 1)

def test_hsv_to_rgb():
    assert hsv_to_rgb(0, 0, 0) == (0, 0, 0)
    assert hsv_to_rgb(0, 0, 1) == (1, 1, 1)
    assert hsv_to_rgb(0.3333333333333333, 0, 0.5) == (0.5, 0.5, 0.5)
    assert hsv_to_rgb(0, 1, 1) == (1, 0, 0)
    assert hsv_to_rgb(0.3333333333333333, 1, 1) == (0, 1, 0)
    assert hsv_to_rgb(0.6666666666666666, 1, 1) == (0, 0, 1)

def test_edge_cases():
    assert rgb_to_yiq(1.1, 0, 0) == (1, 0, 0)
    assert rgb_to_yiq(0, 1.1, 0) == (0.59, 0, 0.41)
    assert rgb_to_yiq(0, 0, 1.1) == (0.11, 0, 0.74)
    assert rgb_to_yiq(-0.1, 0, 0) == (0, 0, 0)
    assert rgb_to_yiq(0, -0.1, 0) == (0, 0, 0)
    assert rgb_to_yiq(0, 0, -0.1) == (0, 0, 0)

    assert yiq_to_rgb(1, 0, 0) == (1, 0, 0)
    assert yiq_to_rgb(0.5, 0, 0) == (0.5, 0.5, 0.5)
    assert yiq_to_rgb(0.3, 0.74, 0) == (1, 0, 0)
    assert yiq_to_rgb(0.59, 0, 0.41) == (0, 1, 0)
    assert yiq_to_rgb(0.11, 0, 0.74) == (0, 0, 1)

    assert rgb_to_hls(1.1, 0, 0) == (0, 0.5, 1)
    assert rgb_to_hls(0, 1.1, 0) == (0.3333333333333333, 0.5, 1)
    assert rgb_to_hls(0, 0, 1.1) == (0.6666666666666666, 0.5, 1)
    assert rgb_to_hls(-0.1, 0, 0) == (0, 0, 0)
    assert rgb_to_hls(0, -0.1, 0) == (0, 0, 0)
    assert rgb_to_hls(0, 0, -0.1) == (0, 0, 0)

    assert hls_to_rgb(0, 0, 0) == (0, 0, 0)
    assert hls_to_rgb(0, 1, 1) == (1, 1, 1)
    assert hls_to_rgb(0.3333333333333333, 0.5, 0.5) == (0.5, 0.5, 0.5)
    assert hls_to_rgb(0, 0.5, 1) == (1, 0, 0)
    assert hls_to_rgb(0.3333333333333333, 0.5, 1) == (0, 1, 0)
    assert hls_to_rgb(0.6666666666666666, 0.5, 1) == (0, 0, 1)

    assert rgb_to_hsv(1.1, 0, 0) == (0, 1, 1)
    assert rgb_to_hsv(0, 1.1, 0) == (0.3333333333333333, 1, 1)
    assert rgb_to_hsv(0, 0, 1.1) == (0.6666666666666666, 1, 1)
    assert rgb_to_hsv(-0.1, 0, 0) == (0, 0, 0)
    assert rgb_to_hsv(0, -0.1, 0) == (0, 0, 0)
    assert rgb_to_hsv(0, 0, -0.1) == (0, 0, 0)

    assert hsv_to_rgb(0, 0, 0) == (0, 0, 0)
    assert hsv_to_rgb(0, 0, 1) == (1, 1, 1)
    assert hsv_to_rgb(0.3333333333333333, 0, 0.5) == (0.5, 0.5, 0.5)
    assert hsv_to_rgb(0, 1, 1) == (1, 0, 0)
    assert hsv_to_rgb(0.3333333333333333, 1, 1) == (0, 1, 0)
    assert hsv_to_rgb(0.6666666666666666, 1, 1) == (0, 0, 1)

if __name__ == "__main__":
    pytest.main()