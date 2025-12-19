from data.complicated_tests.colorsys import *
import pytest
import numpy as np

# Test cases for rgb_to_yiq
def test_rgb_to_yiq():
    assert np.allclose(rgb_to_yiq(1.0, 0.0, 0.0), (0.30, 0.74, 0.48))
    assert np.allclose(rgb_to_yiq(0.0, 1.0, 0.0), (0.59, 0.74, -0.27))
    assert np.allclose(rgb_to_yiq(0.0, 0.0, 1.0), (0.11, -0.48, 0.41))
    assert np.allclose(rgb_to_yiq(0.5, 0.5, 0.5), (0.43, 0.0, 0.0))

# Test cases for yiq_to_rgb
def test_yiq_to_rgb():
    assert np.allclose(yiq_to_rgb(0.30, 0.74, 0.48), (1.0, 0.0, 0.0))
    assert np.allclose(yiq_to_rgb(0.59, 0.74, -0.27), (0.0, 1.0, 0.0))
    assert np.allclose(yiq_to_rgb(0.11, -0.48, 0.41), (0.0, 0.0, 1.0))
    assert np.allclose(yiq_to_rgb(0.43, 0.0, 0.0), (0.5, 0.5, 0.5))

# Test cases for rgb_to_hls
def test_rgb_to_hls():
    assert np.allclose(rgb_to_hls(1.0, 0.0, 0.0), (0.0, 0.5, 1.0))
    assert np.allclose(rgb_to_hls(0.0, 1.0, 0.0), (0.3333333333333333, 0.5, 1.0))
    assert np.allclose(rgb_to_hls(0.0, 0.0, 1.0), (0.6666666666666666, 0.5, 1.0))
    assert np.allclose(rgb_to_hls(0.5, 0.5, 0.5), (0.0, 0.0, 0.5))

# Test cases for hls_to_rgb
def test_hls_to_rgb():
    assert np.allclose(hls_to_rgb(0.0, 0.5, 1.0), (1.0, 0.0, 0.0))
    assert np.allclose(hls_to_rgb(0.3333333333333333, 0.5, 1.0), (0.0, 1.0, 0.0))
    assert np.allclose(hls_to_rgb(0.6666666666666666, 0.5, 1.0), (0.0, 0.0, 1.0))
    assert np.allclose(hls_to_rgb(0.0, 0.0, 0.5), (0.5, 0.5, 0.5))

# Test cases for rgb_to_hsv
def test_rgb_to_hsv():
    assert np.allclose(rgb_to_hsv(1.0, 0.0, 0.0), (0.0, 1.0, 1.0))
    assert np.allclose(rgb_to_hsv(0.0, 1.0, 0.0), (0.3333333333333333, 1.0, 1.0))
    assert np.allclose(rgb_to_hsv(0.0, 0.0, 1.0), (0.6666666666666666, 1.0, 1.0))
    assert np.allclose(rgb_to_hsv(0.5, 0.5, 0.5), (0.0, 0.0, 0.5))

# Test cases for hsv_to_rgb
def test_hsv_to_rgb():
    assert np.allclose(hsv_to_rgb(0.0, 1.0, 1.0), (1.0, 0.0, 0.0))
    assert np.allclose(hsv_to_rgb(0.3333333333333333, 1.0, 1.0), (0.0, 1.0, 0.0))
    assert np.allclose(hsv_to_rgb(0.6666666666666666, 1.0, 1.0), (0.0, 0.0, 1.0))
    assert np.allclose(hsv_to_rgb(0.0, 0.0, 0.5), (0.5, 0.5, 0.5))

# Test cases for edge cases
def test_edge_cases():
    assert np.allclose(rgb_to_yiq(0.0, 0.0, 0.0), (0.0, 0.0, 0.0))
    assert np.allclose(rgb_to_yiq(1.0, 1.0, 1.0), (1.0, 0.0, 0.0))
    assert np.allclose(rgb_to_hls(0.0, 0.0, 0.0), (0.0, 0.0, 0.0))
    assert np.allclose(rgb_to_hls(1.0, 1.0, 1.0), (0.0, 1.0, 1.0))
    assert np.allclose(rgb_to_hsv(0.0, 0.0, 0.0), (0.0, 0.0, 0.0))
    assert np.allclose(rgb_to_hsv(1.0, 1.0, 1.0), (0.0, 0.0, 1.0))

    assert np.allclose(yiq_to_rgb(0.0, 0.0, 0.0), (0.0, 0.0, 0.0))
    assert np.allclose(yiq_to_rgb(1.0, 0.0, 0.0), (1.0, 1.0, 1.0))
    assert np.allclose(hls_to_rgb(0.0, 0.0, 0.0), (0.0, 0.0, 0.0))
    assert np.allclose(hls_to_rgb(0.0, 1.0, 1.0), (1.0, 1.0, 1.0))
    assert np.allclose(hsv_to_rgb(0.0, 0.0, 0.0), (0.0, 0.0, 0.0))
    assert np.allclose(hsv_to_rgb(0.0, 0.0, 1.0), (1.0, 1.0, 1.0))

if __name__ == "__main__":
    pytest.main()