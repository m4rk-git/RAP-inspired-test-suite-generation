from data.complicated_tests.packaging_version import *
import pytest
from packaging.version import parse, Version

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

def test_version_public():
    v = Version("1.2.3+abc")
    assert v.public == "1.2.3"

def test_version_base_version():
    v = Version("1!1.2.3dev1+abc")
    assert v.base_version == "1!1.2.3"

def test_version_is_prerelease():
    v = Version("1.2.3a1")
    assert v.is_prerelease is True

def test_version_is_postrelease():
    v = Version("1.2.3.post1")
    assert v.is_postrelease is True

def test_version_is_devrelease():
    v = Version("1.2.3.dev1")
    assert v.is_devrelease is True

def test_version_major_minor_micro():
    v = Version("1.2.3")
    assert v.major == 1
    assert v.minor == 2
    assert v.micro == 3

def test_version_trimmed_release():
    v = _TrimmedRelease("1.0.0")
    assert v.release == (1,)

def test_version_replace():
    v = Version("1.0.0")
    v_new = v.__replace__(release=(2, 0, 0))
    assert v_new == Version("2.0.0")

def test_version_replace_no_change():
    v = Version("1.0.0")
    v_new = v.__replace__()
    assert v_new == v

def test_version_local_version():
    v = Version("1.2.3+abc")
    assert v.local == ("abc",)

def test_version_local_version_numeric():
    v = Version("1.2.3+1.2.3")
    assert v.local == ((1, 2, 3),)

def test_version_local_version_mixed():
    v = Version("1.2.3+abc.1.twelve")
    assert v.local == ("abc", 1, "twelve")

def test_version_local_version_empty():
    v = Version("1.2.3+")
    assert v.local == ()

def test_version_local_version_invalid():
    with pytest.raises(InvalidVersion):
        Version("1.2.3+abc.def")

def test_version_local_version_trailing_zeros():
    v = Version("1.2.3+0.0")
    assert v.local == ((0,),)

def test_version_local_version_no_trailing_zeros():
    v = Version("1.2.3+0.1")
    assert v.local == ((0, 1),)

def test_version_local_version_negative_infinity():
    v = Version("1.2.3+abc")
    assert v._local == ((NegativeInfinity, "abc"),)

def test_version_local_version_infinity():
    v = Version("1.2.3+abc")
    assert v._local == ((NegativeInfinity, "abc"),)

def test_version_local_version_empty_tuple():
    v = Version("1.2.3+")
    assert v._local == ()

def test_version_local_version_single_element():
    v = Version("1.2.3+abc")
    assert v._local == ((NegativeInfinity, "abc"),)

def test_version_local_version_multiple_elements():
    v = Version("1.2.3+abc.def")
    assert v._local == ((NegativeInfinity, "abc"), (NegativeInfinity, "def"))

def test_version_local_version_mixed_types():
    v = Version("1.2.3+abc.123")
    assert v._local == ((NegativeInfinity, "abc"), (123,))

def test_version_local_version_mixed_types_with_trailing_zeros():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_negative_infinity():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_infinity():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_empty_string():
    v = Version("1.2.3+abc.")
    assert v._local == ((NegativeInfinity, "abc"), (NegativeInfinity, ""))

def test_version_local_version_mixed_types_with_single_digit():
    v = Version("1.2.3+abc.1")
    assert v._local == ((NegativeInfinity, "abc"), (1,))

def test_version_local_version_mixed_types_with_multiple_digits():
    v = Version("1.2.3+abc.123")
    assert v._local == ((NegativeInfinity, "abc"), (123,))

def test_version_local_version_mixed_types_with_negative_number():
    v = Version("1.2.3+abc.-123")
    assert v._local == ((NegativeInfinity, "abc"), (-123,))

def test_version_local_version_mixed_types_with_positive_number():
    v = Version("1.2.3+abc.123")
    assert v._local == ((NegativeInfinity, "abc"), (123,))

def test_version_local_version_mixed_types_with_zero():
    v = Version("1.2.3+abc.0")
    assert v._local == ((NegativeInfinity, "abc"), (0,))

def test_version_local_version_mixed_types_with_trailing_zeros_in_number():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_negative_infinity_in_number():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_infinity_in_number():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_empty_string_in_number():
    v = Version("1.2.3+abc.123.")
    assert v._local == ((NegativeInfinity, "abc"), (123, NegativeInfinity))

def test_version_local_version_mixed_types_with_single_digit_in_number():
    v = Version("1.2.3+abc.123.1")
    assert v._local == ((NegativeInfinity, "abc"), (123, 1))

def test_version_local_version_mixed_types_with_multiple_digits_in_number():
    v = Version("1.2.3+abc.123.123")
    assert v._local == ((NegativeInfinity, "abc"), (123, 123))

def test_version_local_version_mixed_types_with_negative_number_in_number():
    v = Version("1.2.3+abc.123.-123")
    assert v._local == ((NegativeInfinity, "abc"), (123, -123))

def test_version_local_version_mixed_types_with_positive_number_in_number():
    v = Version("1.2.3+abc.123.123")
    assert v._local == ((NegativeInfinity, "abc"), (123, 123))

def test_version_local_version_mixed_types_with_zero_in_number():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_trailing_zeros_in_string():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_negative_infinity_in_string():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_infinity_in_string():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_empty_string_in_string():
    v = Version("1.2.3+abc.123.")
    assert v._local == ((NegativeInfinity, "abc"), (123, NegativeInfinity))

def test_version_local_version_mixed_types_with_single_digit_in_string():
    v = Version("1.2.3+abc.123.1")
    assert v._local == ((NegativeInfinity, "abc"), (123, 1))

def test_version_local_version_mixed_types_with_multiple_digits_in_string():
    v = Version("1.2.3+abc.123.123")
    assert v._local == ((NegativeInfinity, "abc"), (123, 123))

def test_version_local_version_mixed_types_with_negative_number_in_string():
    v = Version("1.2.3+abc.123.-123")
    assert v._local == ((NegativeInfinity, "abc"), (123, -123))

def test_version_local_version_mixed_types_with_positive_number_in_string():
    v = Version("1.2.3+abc.123.123")
    assert v._local == ((NegativeInfinity, "abc"), (123, 123))

def test_version_local_version_mixed_types_with_zero_in_string():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_trailing_zeros_in_mixed():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_negative_infinity_in_mixed():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_infinity_in_mixed():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_empty_string_in_mixed():
    v = Version("1.2.3+abc.123.")
    assert v._local == ((NegativeInfinity, "abc"), (123, NegativeInfinity))

def test_version_local_version_mixed_types_with_single_digit_in_mixed():
    v = Version("1.2.3+abc.123.1")
    assert v._local == ((NegativeInfinity, "abc"), (123, 1))

def test_version_local_version_mixed_types_with_multiple_digits_in_mixed():
    v = Version("1.2.3+abc.123.123")
    assert v._local == ((NegativeInfinity, "abc"), (123, 123))

def test_version_local_version_mixed_types_with_negative_number_in_mixed():
    v = Version("1.2.3+abc.123.-123")
    assert v._local == ((NegativeInfinity, "abc"), (123, -123))

def test_version_local_version_mixed_types_with_positive_number_in_mixed():
    v = Version("1.2.3+abc.123.123")
    assert v._local == ((NegativeInfinity, "abc"), (123, 123))

def test_version_local_version_mixed_types_with_zero_in_mixed():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_trailing_zeros_in_mixed_with_negative_infinity():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_negative_infinity_in_mixed_with_negative_infinity():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (123, 0))

def test_version_local_version_mixed_types_with_infinity_in_mixed_with_negative_infinity():
    v = Version("1.2.3+abc.123.0")
    assert v._local == ((NegativeInfinity, "abc"), (12