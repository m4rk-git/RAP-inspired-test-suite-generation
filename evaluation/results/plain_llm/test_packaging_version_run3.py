from data.complicated_tests.packaging_version import *
import pytest
from packaging.version import parse

def test_parse_valid_version():
    version = parse("1.0.0")
    assert version.release == (1, 0, 0)
    assert version.epoch == 0
    assert version.pre is None
    assert version.post is None
    assert version.dev is None
    assert version.local is None

def test_parse_version_with_pre():
    version = parse("1.0.0a1")
    assert version.release == (1, 0, 0)
    assert version.epoch == 0
    assert version.pre == ('a', 1)
    assert version.post is None
    assert version.dev is None
    assert version.local is None

def test_parse_version_with_post():
    version = parse("1.0.0.post1")
    assert version.release == (1, 0, 0)
    assert version.epoch == 0
    assert version.pre is None
    assert version.post == ('post', 1)
    assert version.dev is None
    assert version.local is None

def test_parse_version_with_dev():
    version = parse("1.0.0.dev1")
    assert version.release == (1, 0, 0)
    assert version.epoch == 0
    assert version.pre is None
    assert version.post is None
    assert version.dev == ('dev', 1)
    assert version.local is None

def test_parse_version_with_local():
    version = parse("1.0.0+local.1")
    assert version.release == (1, 0, 0)
    assert version.epoch == 0
    assert version.pre is None
    assert version.post is None
    assert version.dev is None
    assert version.local == ('local', 1)

def test_parse_version_with_epoch():
    version = parse("1!1.0.0")
    assert version.release == (1, 0, 0)
    assert version.epoch == 1
    assert version.pre is None
    assert version.post is None
    assert version.dev is None
    assert version.local is None

def test_parse_version_with_pre_post_dev():
    version = parse("1.0.0a1.post1.dev1")
    assert version.release == (1, 0, 0)
    assert version.epoch == 0
    assert version.pre == ('a', 1)
    assert version.post == ('post', 1)
    assert version.dev == ('dev', 1)
    assert version.local is None

def test_parse_version_with_local_pre_post_dev():
    version = parse("1.0.0+local.1a1.post1.dev1")
    assert version.release == (1, 0, 0)
    assert version.epoch == 0
    assert version.pre == ('a', 1)
    assert version.post == ('post', 1)
    assert version.dev == ('dev', 1)
    assert version.local == ('local', 1)

def test_parse_version_with_trailing_zeros():
    version = parse("1.0.0")
    assert version.release == (1, 0, 0)
    version = parse("1.0.00")
    assert version.release == (1, 0, 0)
    version = parse("1.0.000")
    assert version.release == (1, 0, 0)

def test_parse_version_with_invalid_input():
    with pytest.raises(InvalidVersion):
        parse("invalid")
    with pytest.raises(InvalidVersion):
        parse("1.0.0a")
    with pytest.raises(InvalidVersion):
        parse("1.0.0.post")
    with pytest.raises(InvalidVersion):
        parse("1.0.0.dev")
    with pytest.raises(InvalidVersion):
        parse("1.0.0+local")
    with pytest.raises(InvalidVersion):
        parse("1.0.0+local.")
    with pytest.raises(InvalidVersion):
        parse("1.0.0+local.a")
    with pytest.raises(InvalidVersion):
        parse("1!1.0.0a")
    with pytest.raises(InvalidVersion):
        parse("1!1.0.0.post")
    with pytest.raises(InvalidVersion):
        parse("1!1.0.0.dev")
    with pytest.raises(InvalidVersion):
        parse("1!1.0.0+local")
    with pytest.raises(InvalidVersion):
        parse("1!1.0.0+local.")
    with pytest.raises(InvalidVersion):
        parse("1!1.0.0+local.a")

def test_version_comparison():
    v1 = Version("1.0.0")
    v2 = Version("1.0.1")
    v3 = Version("1.1.0")
    v4 = Version("1.0.0a1")
    v5 = Version("1.0.0.post1")
    v6 = Version("1.0.0.dev1")
    v7 = Version("1.0.0+local.1")
    v8 = Version("1!1.0.0")
    v9 = Version("1!1.0.0a1")
    v10 = Version("1!1.0.0.post1")
    v11 = Version("1!1.0.0.dev1")
    v12 = Version("1!1.0.0+local.1")

    assert v1 < v2
    assert v1 < v3
    assert v1 < v4
    assert v1 < v5
    assert v1 < v6
    assert v1 < v7
    assert v1 < v8
    assert v1 < v9
    assert v1 < v10
    assert v1 < v11
    assert v1 < v12

    assert v2 > v1
    assert v3 > v1
    assert v4 > v1
    assert v5 > v1
    assert v6 > v1
    assert v7 > v1
    assert v8 > v1
    assert v9 > v1
    assert v10 > v1
    assert v11 > v1
    assert v12 > v1

    assert v1 == v1
    assert v2 == v2
    assert v3 == v3
    assert v4 == v4
    assert v5 == v5
    assert v6 == v6
    assert v7 == v7
    assert v8 == v8
    assert v9 == v9
    assert v10 == v10
    assert v11 == v11
    assert v12 == v12

    assert v1 <= v1
    assert v2 <= v2
    assert v3 <= v3
    assert v4 <= v4
    assert v5 <= v5
    assert v6 <= v6
    assert v7 <= v7
    assert v8 <= v8
    assert v9 <= v9
    assert v10 <= v10
    assert v11 <= v11
    assert v12 <= v12

    assert v2 >= v2
    assert v3 >= v3
    assert v4 >= v4
    assert v5 >= v5
    assert v6 >= v6
    assert v7 >= v7
    assert v8 >= v8
    assert v9 >= v9
    assert v10 >= v10
    assert v11 >= v11
    assert v12 >= v12

    assert v1 != v2
    assert v1 != v3
    assert v1 != v4
    assert v1 != v5
    assert v1 != v6
    assert v1 != v7
    assert v1 != v8
    assert v1 != v9
    assert v1 != v10
    assert v1 != v11
    assert v1 != v12

    assert v2 != v1
    assert v3 != v1
    assert v4 != v1
    assert v5 != v1
    assert v6 != v1
    assert v7 != v1
    assert v8 != v1
    assert v9 != v1
    assert v10 != v1
    assert v11 != v1
    assert v12 != v1

def test_version_replace():
    version = Version("1.0.0")
    assert version.replace() == version
    assert version.replace(epoch=1) == Version("1!1.0.0")
    assert version.replace(release=(2, 0, 0)) == Version("2.0.0")
    assert version.replace(pre=('a', 1)) == Version("1.0.0a1")
    assert version.replace(post=1) == Version("1.0.0.post1")
    assert version.replace(dev=1) == Version("1.0.0.dev1")
    assert version.replace(local='local.1') == Version("1.0.0+local.1")
    assert version.replace(epoch=1, release=(2, 0, 0), pre=('a', 1), post=1, dev=1, local='local.1') == Version("1!2.0.0a1.post1.dev1+local.1")

def test_version_replace_invalid():
    version = Version("1.0.0")
    with pytest.raises(InvalidVersion):
        version.replace(epoch=-1)
    with pytest.raises(InvalidVersion):
        version.replace(release=(1, 0))
    with pytest.raises(InvalidVersion):
        version.replace(pre=('a', 'b'))
    with pytest.raises(InvalidVersion):
        version.replace(post='1')
    with pytest.raises(InvalidVersion):
        version.replace(dev='1')
    with pytest.raises(InvalidVersion):
        version.replace(local='local.')
    with pytest.raises(InvalidVersion):
        version.replace(local='local.a')

def test_version_trimmed_release():
    version = _TrimmedRelease("1.0.0")
    assert version.release == (1,)
    version = _TrimmedRelease("0.0")
    assert version.release == (0,)
    version = _TrimmedRelease("1.0.00")
    assert version.release == (1,)
    version = _TrimmedRelease("1.0.000")
    assert version.release == (1,)
    version = _TrimmedRelease("1.0.0a1")
    assert version.release == (1, 0, 0)
    version = _TrimmedRelease("1.0.0.post1")
    assert version.release == (1, 0, 0)
    version = _TrimmedRelease("1.0.0.dev1")
    assert version.release == (1, 0, 0)
    version = _TrimmedRelease("1.0.0+local.1")
    assert version.release == (1, 0, 0)
    version = _TrimmedRelease("1!1.0.0")
    assert version.release == (1, 0, 0)
    version = _TrimmedRelease("1!1.0.0a1")
    assert version.release == (1, 0, 0)
    version = _TrimmedRelease("1!1.0.0.post1")
    assert version.release == (1, 0, 0)
    version = _TrimmedRelease("1!1.0.0.dev1")
    assert version.release == (1, 0, 0)
    version = _TrimmedRelease("1!1.0.0+local.1")
    assert version.release == (1, 0, 0)