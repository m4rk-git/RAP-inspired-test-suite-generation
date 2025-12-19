from data.complicated_tests.packaging_version import *
import pytest
from packaging.version import parse, Version, InvalidVersion

def test_parse_valid_version():
    version = parse("1.0.0")
    assert isinstance(version, Version)
    assert version == Version("1.0.0")

def test_parse_invalid_version():
    with pytest.raises(InvalidVersion):
        parse("invalid")

def test_version_comparison():
    v1 = Version("1.0a5")
    v2 = Version("1.0")
    assert v1 < v2
    assert v1 != v2
    assert v1 <= v2
    assert v1 > v2 is False
    assert v1 >= v2 is False

def test_version_attributes():
    version = Version("1.2.3a1")
    assert version.epoch == 0
    assert version.release == (1, 2, 3)
    assert version.pre == ('a', 1)
    assert version.post is None
    assert version.dev is None
    assert version.local is None

def test_version_with_local():
    version = Version("1.2.3+abc")
    assert version.local == ('abc',)

def test_version_with_dev():
    version = Version("1.2.3.dev1")
    assert version.dev == ('dev', 1)

def test_version_with_post():
    version = Version("1.2.3.post1")
    assert version.post == (1,)

def test_version_with_pre_post_dev():
    version = Version("1.2.3a1.post1.dev1")
    assert version.pre == ('a', 1)
    assert version.post == (1,)
    assert version.dev == ('dev', 1)

def test_version_with_epoch():
    version = Version("1!1.2.3")
    assert version.epoch == 1

def test_version_with_trailing_zeros():
    version = Version("1.0.0")
    assert version.release == (1, 0, 0)

def test_version_with_pre_alpha():
    version = Version("1.0a1")
    assert version.pre == ('a', 1)

def test_version_with_pre_beta():
    version = Version("1.0b1")
    assert version.pre == ('b', 1)

def test_version_with_pre_rc():
    version = Version("1.0rc1")
    assert version.pre == ('rc', 1)

def test_version_with_pre_rev():
    version = Version("1.0rev1")
    assert version.pre == ('post', 1)

def test_version_with_pre_r():
    version = Version("1.0r1")
    assert version.pre == ('post', 1)

def test_version_with_post_number():
    version = Version("1.0.post1")
    assert version.post == (1,)

def test_version_with_dev_number():
    version = Version("1.0.dev1")
    assert version.dev == ('dev', 1)

def test_version_with_local_number():
    version = Version("1.0+1")
    assert version.local == (1,)

def test_version_with_local_alpha():
    version = Version("1.0+a")
    assert version.local == ('a',)

def test_version_with_local_alpha_number():
    version = Version("1.0+a1")
    assert version.local == ('a', 1)

def test_version_with_local_number_alpha():
    version = Version("1.0+1a")
    assert version.local == (1, 'a')

def test_version_with_local_number_alpha_number():
    version = Version("1.0+1a1")
    assert version.local == (1, 'a', 1)

def test_version_with_local_number_alpha_number_number():
    version = Version("1.0+1a1b2")
    assert version.local == (1, 'a', 1, 'b', 2)

def test_version_with_local_number_alpha_number_number_number():
    version = Version("1.0+1a1b2c3")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3)

def test_version_with_local_number_alpha_number_number_number_number():
    version = Version("1.0+1a1b2c3d4")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3, 'd', 4)

def test_version_with_local_number_alpha_number_number_number_number_number():
    version = Version("1.0+1a1b2c3d4e5")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5)

def test_version_with_local_number_alpha_number_number_number_number_number_number():
    version = Version("1.0+1a1b2c3d4e5f6")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5, 'f', 6)

def test_version_with_local_number_alpha_number_number_number_number_number_number_number():
    version = Version("1.0+1a1b2c3d4e5f6g7")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5, 'f', 6, 'g', 7)

def test_version_with_local_number_alpha_number_number_number_number_number_number_number_number():
    version = Version("1.0+1a1b2c3d4e5f6g7h8")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5, 'f', 6, 'g', 7, 'h', 8)

def test_version_with_local_number_alpha_number_number_number_number_number_number_number_number_number():
    version = Version("1.0+1a1b2c3d4e5f6g7h8i9")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5, 'f', 6, 'g', 7, 'h', 8, 'i', 9)

def test_version_with_local_number_alpha_number_number_number_number_number_number_number_number_number_number():
    version = Version("1.0+1a1b2c3d4e5f6g7h8i9j10")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5, 'f', 6, 'g', 7, 'h', 8, 'i', 9, 'j', 10)

def test_version_with_local_number_alpha_number_number_number_number_number_number_number_number_number_number_number():
    version = Version("1.0+1a1b2c3d4e5f6g7h8i9j10k11")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5, 'f', 6, 'g', 7, 'h', 8, 'i', 9, 'j', 10, 'k', 11)

def test_version_with_local_number_alpha_number_number_number_number_number_number_number_number_number_number_number_number():
    version = Version("1.0+1a1b2c3d4e5f6g7h8i9j10k11l12")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5, 'f', 6, 'g', 7, 'h', 8, 'i', 9, 'j', 10, 'k', 11, 'l', 12)

def test_version_with_local_number_alpha_number_number_number_number_number_number_number_number_number_number_number_number_number():
    version = Version("1.0+1a1b2c3d4e5f6g7h8i9j10k11l12m13")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5, 'f', 6, 'g', 7, 'h', 8, 'i', 9, 'j', 10, 'k', 11, 'l', 12, 'm', 13)

def test_version_with_local_number_alpha_number_number_number_number_number_number_number_number_number_number_number_number_number_number():
    version = Version("1.0+1a1b2c3d4e5f6g7h8i9j10k11l12m13n14")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5, 'f', 6, 'g', 7, 'h', 8, 'i', 9, 'j', 10, 'k', 11, 'l', 12, 'm', 13, 'n', 14)

def test_version_with_local_number_alpha_number_number_number_number_number_number_number_number_number_number_number_number_number_number_number():
    version = Version("1.0+1a1b2c3d4e5f6g7h8i9j10k11l12m13n14o15")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5, 'f', 6, 'g', 7, 'h', 8, 'i', 9, 'j', 10, 'k', 11, 'l', 12, 'm', 13, 'n', 14, 'o', 15)

def test_version_with_local_number_alpha_number_number_number_number_number_number_number_number_number_number_number_number_number_number_number_number():
    version = Version("1.0+1a1b2c3d4e5f6g7h8i9j10k11l12m13n14o15p16")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5, 'f', 6, 'g', 7, 'h', 8, 'i', 9, 'j', 10, 'k', 11, 'l', 12, 'm', 13, 'n', 14, 'o', 15, 'p', 16)

def test_version_with_local_number_alpha_number_number_number_number_number_number_number_number_number_number_number_number_number_number_number_number_number():
    version = Version("1.0+1a1b2c3d4e5f6g7h8i9j10k11l12m13n14o15p16q17")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5, 'f', 6, 'g', 7, 'h', 8, 'i', 9, 'j', 10, 'k', 11, 'l', 12, 'm', 13, 'n', 14, 'o', 15, 'p', 16, 'q', 17)

def test_version_with_local_number_alpha_number_number_number_number_number_number_number_number_number_number_number_number_number_number_number_number_number_number():
    version = Version("1.0+1a1b2c3d4e5f6g7h8i9j10k11l12m13n14o15p16q17r18")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5, 'f', 6, 'g', 7, 'h', 8, 'i', 9, 'j', 10, 'k', 11, 'l', 12, 'm', 13, 'n', 14, 'o', 15, 'p', 16, 'q', 17, 'r', 18)

def test_version_with_local_number_alpha_number_number_number_number_number_number_number_number_number_number_number_number_number_number_number_number_number_number_number():
    version = Version("1.0+1a1b2c3d4e5f6g7h8i9j10k11l12m13n14o15p16q17r18s19")
    assert version.local == (1, 'a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5, 'f', 6, 'g', 7, 'h', 8, 'i', 9, 'j', 10, 'k', 11, 'l', 12, 'm', 13, 'n', 14, 'o', 15, 'p', 16, 'q', 17, 'r', 18, 's', 19)

def test_version_with_local_number_alpha_number_number_number_number_number_number_number