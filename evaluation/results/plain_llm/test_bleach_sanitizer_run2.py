from data.complicated_tests.bleach_sanitizer import *
import pytest
from html5lib import parseFragment
from html5lib.serializer import serialize
from html5lib.treewalkers import getTreeWalker
from html5lib.filters.sanitizer import Filter
from html5lib.constants import namespaces

def test_cleaner_init():
    cleaner = Cleaner()
    assert cleaner.tags == ALLOWED_TAGS
    assert cleaner.attributes == ALLOWED_ATTRIBUTES
    assert cleaner.protocols == ALLOWED_PROTOCOLS
    assert cleaner.strip is False
    assert cleaner.strip_comments is True
    assert cleaner.filters == []
    assert cleaner.css_sanitizer is None

def test_cleaner_clean():
    cleaner = Cleaner()
    text = "<div><p>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><p>Hello, <b>World</b>!</p></div>"

def test_cleaner_clean_with_strip():
    cleaner = Cleaner(strip=True)
    text = "<div><p>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<p>Hello, <b>World</b>!</p>"

def test_cleaner_clean_with_strip_comments():
    cleaner = Cleaner(strip_comments=True)
    text = "<div><!-- Comment --><p>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><p>Hello, <b>World</b>!</p></div>"

def test_cleaner_clean_with_filters():
    class TestFilter(Filter):
        def filter(self, token):
            if token["type"] == "Characters":
                token["data"] = token["data"].upper()
            return token

    cleaner = Cleaner(filters=[TestFilter])
    text = "<div><p>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><p>HELLO, <b>WORLD</b>!</p></div>"

def test_cleaner_clean_with_css_sanitizer():
    class TestCSSSanitizer:
        def sanitize_css(self, css):
            return css.replace("color", "background-color")

    cleaner = Cleaner(css_sanitizer=TestCSSSanitizer())
    text = "<div style='color: red;'>Hello, <b>World</b>!</div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div style='background-color: red;'>Hello, <b>World</b>!</div>"

def test_cleaner_clean_with_invisible_characters():
    cleaner = Cleaner()
    text = "<div><p>Hello, <b>World</b>!\x00\x01\x02\x03\x04\x05\x06\x07\x08\x0b\x0c\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><p>Hello, <b>World</b>!????????????????????????</p></div>"

def test_cleaner_clean_with_invalid_html():
    cleaner = Cleaner()
    text = "<div><p>Hello, <b>World</b>!><script>alert('XSS')</script></p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><p>Hello, <b>World</b>!</p></div>"

def test_cleaner_clean_with_allowed_protocols():
    cleaner = Cleaner(allowed_protocols={"http", "https"})
    text = "<div><a href='http://example.com'>Example</a></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><a href='http://example.com'>Example</a></div>"

def test_cleaner_clean_with_disallowed_protocols():
    cleaner = Cleaner(allowed_protocols={"http", "https"})
    text = "<div><a href='ftp://example.com'>Example</a></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><a href=''>Example</a></div>"

def test_cleaner_clean_with_svg_attributes():
    cleaner = Cleaner()
    text = "<svg><rect fill='red' stroke='blue' stroke-width='2' x='0' y='0' width='100' height='100'/></svg>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<svg><rect fill='red' stroke='blue' stroke-width='2' x='0' y='0' width='100' height='100'/></svg>"

def test_cleaner_clean_with_svg_local_href():
    cleaner = Cleaner()
    text = "<svg><a xlink:href='#local'>Local</a></svg>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<svg><a xlink:href='#local'>Local</a></svg>"

def test_cleaner_clean_with_svg_non_local_href():
    cleaner = Cleaner()
    text = "<svg><a xlink:href='http://example.com'>Example</a></svg>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<svg><a xlink:href=''>Example</a></svg>"

def test_cleaner_clean_with_style_attribute():
    cleaner = Cleaner()
    text = "<div style='color: red;'>Hello, <b>World</b>!</div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div style='color: red;'>Hello, <b>World</b>!</div>"

def test_cleaner_clean_with_no_css_sanitizer():
    cleaner = Cleaner()
    text = "<div style='color: red;'>Hello, <b>World</b>!</div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div style='color: red;'>Hello, <b>World</b>!</div>"

def test_cleaner_clean_with_callable_attributes():
    cleaner = Cleaner(attributes=lambda tag, attr, value: True)
    text = "<div><p>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><p>Hello, <b>World</b>!</p></div>"

def test_cleaner_clean_with_list_attributes():
    cleaner = Cleaner(attributes=["href"])
    text = "<div><a href='http://example.com'>Example</a></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><a href='http://example.com'>Example</a></div>"

def test_cleaner_clean_with_dict_attributes():
    cleaner = Cleaner(attributes={"a": ["href"]})
    text = "<div><a href='http://example.com'>Example</a></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><a href='http://example.com'>Example</a></div>"

def test_cleaner_clean_with_star_attributes():
    cleaner = Cleaner(attributes={"*": ["href"]})
    text = "<div><a href='http://example.com'>Example</a></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><a href='http://example.com'>Example</a></div>"

def test_cleaner_clean_with_no_allowed_tags():
    cleaner = Cleaner(tags=set())
    text = "<div><p>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == ""

def test_cleaner_clean_with_no_allowed_attributes():
    cleaner = Cleaner(attributes={})
    text = "<div><a href='http://example.com'>Example</a></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><a href=''>Example</a></div>"

def test_cleaner_clean_with_no_allowed_protocols():
    cleaner = Cleaner(allowed_protocols=set())
    text = "<div><a href='http://example.com'>Example</a></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><a href=''>Example</a></div>"

def test_cleaner_clean_with_no_filters():
    cleaner = Cleaner(filters=None)
    text = "<div><p>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><p>Hello, <b>World</b>!</p></div>"

def test_cleaner_clean_with_no_css_sanitizer():
    cleaner = Cleaner(css_sanitizer=None)
    text = "<div style='color: red;'>Hello, <b>World</b>!</div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div style='color: red;'>Hello, <b>World</b>!</div>"

def test_cleaner_clean_with_no_allowed_tags_and_attributes():
    cleaner = Cleaner(tags=set(), attributes={})
    text = "<div><a href='http://example.com'>Example</a></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == ""

def test_cleaner_clean_with_no_allowed_tags_and_protocols():
    cleaner = Cleaner(tags=set(), allowed_protocols=set())
    text = "<div><a href='http://example.com'>Example</a></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == ""

def test_cleaner_clean_with_no_allowed_tags_and_filters():
    cleaner = Cleaner(tags=set(), filters=None)
    text = "<div><p>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == ""

def test_cleaner_clean_with_no_allowed_tags_and_css_sanitizer():
    cleaner = Cleaner(tags=set(), css_sanitizer=None)
    text = "<div style='color: red;'>Hello, <b>World</b>!</div>"
    sanitized = cleaner.clean(text)
    assert sanitized == ""

def test_cleaner_clean_with_no_allowed_attributes_and_protocols():
    cleaner = Cleaner(attributes={}, allowed_protocols=set())
    text = "<div><a href='http://example.com'>Example</a></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><a href=''>Example</a></div>"

def test_cleaner_clean_with_no_allowed_attributes_and_filters():
    cleaner = Cleaner(attributes={}, filters=None)
    text = "<div><p>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><p>Hello, <b>World</b>!</p></div>"

def test_cleaner_clean_with_no_allowed_attributes_and_css_sanitizer():
    cleaner = Cleaner(attributes={}, css_sanitizer=None)
    text = "<div style='color: red;'>Hello, <b>World</b>!</div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div style='color: red;'>Hello, <b>World</b>!</div>"

def test_cleaner_clean_with_no_allowed_protocols_and_filters():
    cleaner = Cleaner(allowed_protocols=set(), filters=None)
    text = "<div><a href='http://example.com'>Example</a></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><a href=''>Example</a></div>"

def test_cleaner_clean_with_no_allowed_protocols_and_css_sanitizer():
    cleaner = Cleaner(allowed_protocols=set(), css_sanitizer=None)
    text = "<div style='color: red;'>Hello, <b>World</b>!</div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div style='color: red;'>Hello, <b>World</b>!</div>"

def test_cleaner_clean_with_no_filters_and_css_sanitizer():
    cleaner = Cleaner(filters=None, css_sanitizer=None)
    text = "<div style='color: red;'>Hello, <b>World</b>!</div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div style='color: red;'>Hello, <b>World</b>!</div>"

def test_cleaner_clean_with_no_allowed_tags_and_attributes_and_protocols():
    cleaner = Cleaner(tags=set(), attributes={}, allowed_protocols=set())
    text = "<div><a href='http://example.com'>Example</a></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == ""

def test_cleaner_clean_with_no_allowed_tags_and_attributes_and_filters():
    cleaner = Cleaner(tags=set(), attributes={}, filters=None)
    text = "<div><p>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == ""

def test_cleaner_clean_with_no_allowed_tags_and_attributes_and_css_sanitizer():
    cleaner = Cleaner(tags=set(), attributes={}, css_sanitizer=None)
    text = "<div style='color: red;'>Hello, <b>World</b>!</div>"
    sanitized = cleaner.clean(text)
    assert sanitized == ""

def test_cleaner_clean_with_no_allowed_tags_and_protocols_and_filters():
    cleaner = Cleaner(tags=set(), allowed_protocols=set(), filters=None)
    text = "<div><a href='http://example.com'>Example</a></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == ""

def test_cleaner_clean_with_no_allowed_tags_and_protocols_and_css_sanitizer():
    cleaner = Cleaner(tags=set(), allowed_protocols=set(), css_sanitizer=None)
    text = "<div style='color: red;'>Hello, <b>World</b>!</div>"
    sanitized = cleaner.clean(text)
    assert sanitized == ""

def test_cleaner_clean_with_no_allowed_tags_and_filters_and_css_sanitizer():
    cleaner = Cleaner(tags=set(), filters=None, css_sanitizer=None)
    text = "<div style='color: red;'>Hello, <b>World</b>!</div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div style='color: red;'>Hello, <b>World</b>!</div>"

def test_cleaner_clean_with_no_allowed_attributes_and_protocols_and_filters():
    cleaner = Cleaner(attributes={}, allowed_protocols=set(), filters=None)
    text = "<div><a href='http://example.com'>Example</a></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><a href=''>Example</a></div>"

def test_cleaner_clean_with_no_allowed_attributes_and_protocols_and_css_sanitizer():
    cleaner = Cleaner(attributes={}, allowed_protocols=set(), css_sanitizer=None)