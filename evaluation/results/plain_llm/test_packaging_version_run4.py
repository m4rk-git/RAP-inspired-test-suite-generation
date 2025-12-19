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
    v = Version("1.2.3a1")
    assert v.epoch == 0
    assert v.release == (1, 2, 3)
    assert v.pre == ('a', 1)
    assert v.post is None
    assert v.dev is None
    assert v.local is None
    assert v.public == '1.2.3'
    assert v.base_version == '1.2.3'
    assert v.is_prerelease is True
    assert v.is_postrelease is False
    assert v.is_devrelease is False
    assert v.major == 1
    assert v.minor == 2
    assert v.micro == 3

def test_version_local():
    v = Version("1.2.3+abc")
    assert v.local == ('abc',)

def test_version_pre_post_dev():
    v = Version("1.2.3a1")
    assert v.pre == ('a', 1)
    assert v.post is None
    assert v.dev is None

    v = Version("1.2.3.post1")
    assert v.pre is None
    assert v.post == (1,)
    assert v.dev is None

    v = Version("1.2.3.dev1")
    assert v.pre is None
    assert v.post is None
    assert v.dev == (1,)

def test_version_trailing_zeros():
    v = Version("1.0.0")
    assert v.release == (1, 0, 0)
    v = Version("1.0")
    assert v.release == (1, 0)

def test_version_local_comparison():
    v1 = Version("1.0+abc")
    v2 = Version("1.0+def")
    assert v1 < v2
    assert v1 != v2
    assert v1 <= v2
    assert v1 > v2 is False
    assert v1 >= v2 is False

    v1 = Version("1.0+abc")
    v2 = Version("1.0+abc")
    assert v1 == v2
    assert v1 <= v2
    assert v1 >= v2

def test_version_pre_post_dev_comparison():
    v1 = Version("1.0a1")
    v2 = Version("1.0a2")
    assert v1 < v2
    assert v1 != v2
    assert v1 <= v2
    assert v1 > v2 is False
    assert v1 >= v2 is False

    v1 = Version("1.0a1")
    v2 = Version("1.0a1")
    assert v1 == v2
    assert v1 <= v2
    assert v1 >= v2

    v1 = Version("1.0a1")
    v2 = Version("1.0b1")
    assert v1 < v2
    assert v1 != v2
    assert v1 <= v2
    assert v1 > v2 is False
    assert v1 >= v2 is False

    v1 = Version("1.0b1")
    v2 = Version("1.0rc1")
    assert v1 < v2
    assert v1 != v2
    assert v1 <= v2
    assert v1 > v2 is False
    assert v1 >= v2 is False

    v1 = Version("1.0rc1")
    v2 = Version("1.0")
    assert v1 < v2
    assert v1 != v2
    assert v1 <= v2
    assert v1 > v2 is False
    assert v1 >= v2 is False

    v1 = Version("1.0")
    v2 = Version("1.0.dev1")
    assert v1 < v2
    assert v1 != v2
    assert v1 <= v2
    assert v1 > v2 is False
    assert v1 >= v2 is False

    v1 = Version("1.0.dev1")
    v2 = Version("1.0.dev2")
    assert v1 < v2
    assert v1 != v2
    assert v1 <= v2
    assert v1 > v2 is False
    assert v1 >= v2 is False

def test_version_epoch_comparison():
    v1 = Version("1!1.0")
    v2 = Version("2!1.0")
    assert v1 < v2
    assert v1 != v2
    assert v1 <= v2
    assert v1 > v2 is False
    assert v1 >= v2 is False

    v1 = Version("1!1.0")
    v2 = Version("1!1.0")
    assert v1 == v2
    assert v1 <= v2
    assert v1 >= v2

def test_version_replace():
    v = Version("1.0a5")
    v_new = v.__replace__(pre=('b', 1))
    assert v_new == Version("1.0b1")
    assert v_new != v

    v_new = v.__replace__(post=1)
    assert v_new == Version("1.0.post1")
    assert v_new != v

    v_new = v.__replace__(dev=1)
    assert v_new == Version("1.0.dev1")
    assert v_new != v

    v_new = v.__replace__(local=('abc',))
    assert v_new == Version("1.0a5+abc")
    assert v_new != v

    v_new = v.__replace__(epoch=1)
    assert v_new == Version("1!1.0a5")
    assert v_new != v

    v_new = v.__replace__(release=(1, 1))
    assert v_new == Version("1.1a5")
    assert v_new != v

def test_version_replace_no_change():
    v = Version("1.0a5")
    v_new = v.__replace__()
    assert v_new == v
    assert v_new is v

def test_version_replace_invalid():
    with pytest.raises(InvalidVersion):
        v = Version("1.0a5")
        v.__replace__(pre=('x', 1))

    with pytest.raises(InvalidVersion):
        v = Version("1.0a5")
        v.__replace__(post='a')

    with pytest.raises(InvalidVersion):
        v = Version("1.0a5")
        v.__replace__(dev='a')

    with pytest.raises(InvalidVersion):
        v = Version("1.0a5")
        v.__replace__(local='abc')

    with pytest.raises(InvalidVersion):
        v = Version("1.0a5")
        v.__replace__(epoch=-1)

    with pytest.raises(InvalidVersion):
        v = Version("1.0a5")
        v.__replace__(release=(1,))

def test_version_replace_none():
    v = Version("1.0a5")
    v_new = v.__replace__(pre=None)
    assert v_new == Version("1.0")
    assert v_new != v

    v_new = v.__replace__(post=None)
    assert v_new == Version("1.0")
    assert v_new != v

    v_new = v.__replace__(dev=None)
    assert v_new == Version("1.0")
    assert v_new != v

    v_new = v.__replace__(local=None)
    assert v_new == Version("1.0")
    assert v_new != v

    v_new = v.__replace__(epoch=None)
    assert v_new == Version("1.0a5")
    assert v_new != v

    v_new = v.__replace__(release=None)
    assert v_new == Version("1.0a5")
    assert v_new != v

def test_version_replace_empty():
    v = Version("1.0a5")
    v_new = v.__replace__(pre=())
    assert v_new == Version("1.0")
    assert v_new != v

    v_new = v.__replace__(post=())
    assert v_new == Version("1.0")
    assert v_new != v

    v_new = v.__replace__(dev=())
    assert v_new == Version("1.0")
    assert v_new != v

    v_new = v.__replace__(local=())
    assert v_new == Version("1.0")
    assert v_new != v

    v_new = v.__replace__(epoch=())
    assert v_new == Version("1.0a5")
    assert v_new != v

    v_new = v.__replace__(release=())
    assert v_new == Version("1.0a5")
    assert v_new != v

def test_version_replace_empty_string():
    v = Version("1.0a5")
    v_new = v.__replace__(local=('abc', ''))
    assert v_new == Version("1.0a5+abc")
    assert v_new != v

def test_version_replace_empty_tuple():
    v = Version("1.0a5")
    v_new = v.__replace__(local=())
    assert v_new == Version("1.0")
    assert v_new != v

def test_version_replace_empty_string_tuple():
    v = Version("1.0a5")
    v_new = v.__replace__(local=('abc', ''))
    assert v_new == Version("1.0a5+abc")
    assert v_new != v

def test_version_replace_empty_string_tuple_empty_string():
    v = Version("1.0a5")
    v_new = v.__replace__(local=('abc', '', ''))
    assert v_new == Version("1.0a5+abc")
    assert v_new != v

def test_version_replace_empty_string_tuple_empty_string_empty_string():
    v = Version("1.0a5")
    v_new = v.__replace__(local=('abc', '', '', ''))
    assert v_new == Version("1.0a5+abc")
    assert v_new != v

def test_version_replace_empty_string_tuple_empty_string_empty_string_empty_string():
    v = Version("1.0a5")
    v_new = v.__replace__(local=('abc', '', '', '', ''))
    assert v_new == Version("1.0a5+abc")
    assert v_new != v

def test_version_replace_empty_string_tuple_empty_string_empty_string_empty_string_empty_string():
    v = Version("1.0a5")
    v_new = v.__replace__(local=('abc', '', '', '', '', ''))
    assert v_new == Version("1.0a5+abc")
    assert v_new != v

def test_version_replace_empty_string_tuple_empty_string_empty_string_empty_string_empty_string_empty_string():
    v = Version("1.0a5")
    v_new = v.__replace__(local=('abc', '', '', '', '', '', ''))
    assert v_new == Version("1.0a5+abc")
    assert v_new != v

def test_version_replace_empty_string_tuple_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string():
    v = Version("1.0a5")
    v_new = v.__replace__(local=('abc', '', '', '', '', '', '', ''))
    assert v_new == Version("1.0a5+abc")
    assert v_new != v

def test_version_replace_empty_string_tuple_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string():
    v = Version("1.0a5")
    v_new = v.__replace__(local=('abc', '', '', '', '', '', '', '', ''))
    assert v_new == Version("1.0a5+abc")
    assert v_new != v

def test_version_replace_empty_string_tuple_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string():
    v = Version("1.0a5")
    v_new = v.__replace__(local=('abc', '', '', '', '', '', '', '', '', ''))
    assert v_new == Version("1.0a5+abc")
    assert v_new != v

def test_version_replace_empty_string_tuple_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string():
    v = Version("1.0a5")
    v_new = v.__replace__(local=('abc', '', '', '', '', '', '', '', '', '', ''))
    assert v_new == Version("1.0a5+abc")
    assert v_new != v

def test_version_replace_empty_string_tuple_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string():
    v = Version("1.0a5")
    v_new = v.__replace__(local=('abc', '', '', '', '', '', '', '', '', '', '', ''))
    assert v_new == Version("1.0a5+abc")
    assert v_new != v

def test_version_replace_empty_string_tuple_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string():
    v = Version("1.0a5")
    v_new = v.__replace__(local=('abc', '', '', '', '', '', '', '', '', '', '', '', ''))
    assert v_new == Version("1.0a5+abc")
    assert v_new != v

def test_version_replace_empty_string_tuple_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string_empty_string():
    v = Version("1.0a5")
    v_new = v.__replace__(local=('abc', '', '', '', '', '', '', '', '', '', '', '', '', ''))
    assert v_new == Version("1.0a5+abc")
    assert v_new != v

def test_version_replace_empty_string_tuple_empty_string