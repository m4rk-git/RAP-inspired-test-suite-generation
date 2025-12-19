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

def test_version_properties():
    v = Version("1.2.3a1")
    assert v.epoch == 0
    assert v.release == (1, 2, 3)
    assert v.pre == ('a', 1)
    assert v.post is None
    assert v.dev is None
    assert v.local is None
    assert v.public == '1.2.3'
    assert v.base_version == '1.2.3'

def test_version_local():
    v = Version("1.0+abc")
    assert v.local == ('abc',)

    v = Version("1.0+abc.1")
    assert v.local == ('abc', 1)

    v = Version("1.0+abc.1.twelve")
    assert v.local == ('abc', 1, 'twelve')

def test_version_pre_post_dev():
    v = Version("1.0a1")
    assert v.pre == ('a', 1)
    assert v.post is None
    assert v.dev is None

    v = Version("1.0.post1")
    assert v.pre is None
    assert v.post == ('post', 1)
    assert v.dev is None

    v = Version("1.0.dev1")
    assert v.pre is None
    assert v.post is None
    assert v.dev == ('dev', 1)

def test_version_trailing_zeros():
    v = Version("1.0.0")
    assert v.release == (1, 0, 0)

    v = Version("1.0")
    assert v.release == (1, 0)

    v = Version("1")
    assert v.release == (1,)

def test_version_trimmed_release():
    v = _TrimmedRelease("1.0.0")
    assert v.release == (1,)

    v = _TrimmedRelease("0.0")
    assert v.release == (0,)

def test_version_invalid_local():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc.def")

def test_version_invalid_pre_post_dev():
    with pytest.raises(InvalidVersion):
        Version("1.0.a1")

    with pytest.raises(InvalidVersion):
        Version("1.0.post1")

    with pytest.raises(InvalidVersion):
        Version("1.0.dev1")

def test_version_invalid_epoch():
    with pytest.raises(InvalidVersion):
        Version("1!1.2.3dev1+abc")

def test_version_invalid_release():
    with pytest.raises(InvalidVersion):
        Version("1.2.3.4")

def test_version_invalid_pre():
    with pytest.raises(InvalidVersion):
        Version("1.2.3a")

def test_version_invalid_post():
    with pytest.raises(InvalidVersion):
        Version("1.2.3.post")

def test_version_invalid_dev():
    with pytest.raises(InvalidVersion):
        Version("1.2.3.dev")

def test_version_invalid_local_separator():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc-def")

def test_version_invalid_local_number():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc.1.2")

def test_version_invalid_local_alpha():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc.1.def")

def test_version_invalid_local_empty():
    with pytest.raises(InvalidVersion):
        Version("1.0+")

def test_version_invalid_local_trailing_dot():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc.")

def test_version_invalid_local_trailing_digit():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc1")

def test_version_invalid_local_trailing_alpha():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc1a")

def test_version_invalid_local_trailing_space():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc ")

def test_version_invalid_local_leading_space():
    with pytest.raises(InvalidVersion):
        Version("1.0+ abc")

def test_version_invalid_local_leading_dot():
    with pytest.raises(InvalidVersion):
        Version("1.0+.abc")

def test_version_invalid_local_leading_digit():
    with pytest.raises(InvalidVersion):
        Version("1.0+1abc")

def test_version_invalid_local_leading_alpha():
    with pytest.raises(InvalidVersion):
        Version("1.0+a1abc")

def test_version_invalid_local_leading_plus():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc+")

def test_version_invalid_local_leading_dash():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc-")

def test_version_invalid_local_leading_underscore():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc_")

def test_version_invalid_local_leading_slash():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc/")

def test_version_invalid_local_leading_backslash():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc\\")

def test_version_invalid_local_leading_colon():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc:")

def test_version_invalid_local_leading_semicolon():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc;")

def test_version_invalid_local_leading_comma():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc,")

def test_version_invalid_local_leading_exclamation():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc!")

def test_version_invalid_local_leading_question():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc?")

def test_version_invalid_local_leading_at():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc@")

def test_version_invalid_local_leading_hash():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc#")

def test_version_invalid_local_leading_dollar():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc$")

def test_version_invalid_local_leading_percent():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc%")

def test_version_invalid_local_leading_caret():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc^")

def test_version_invalid_local_leading_ampersand():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc&")

def test_version_invalid_local_leading_star():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc*")

def test_version_invalid_local_leading_plus_sign():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc+")

def test_version_invalid_local_leading_equal_sign():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc=")

def test_version_invalid_local_leading_space_in_number():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc.1 2")

def test_version_invalid_local_leading_space_in_alpha():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc.1 a")

def test_version_invalid_local_leading_space_in_plus():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc.1 +")

def test_version_invalid_local_leading_space_in_dash():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc.1 -")

def test_version_invalid_local_leading_space_in_underscore():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc.1 _")

def test_version_invalid_local_leading_space_in_slash():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc.1 /")

def test_version_invalid_local_leading_space_in_backslash():
    with pytest.raises(InvalidVersion):
        Version("1.0+abc.1 \\")