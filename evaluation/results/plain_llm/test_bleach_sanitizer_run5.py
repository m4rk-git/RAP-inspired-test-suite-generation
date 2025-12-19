from data.complicated_tests.bleach_sanitizer import *
import pytest
from html5lib import parseFragment
from html5lib.serializer import serialize
from html5lib.treewalkers import getTreeWalker
from html5lib.filters.sanitizer import Filter

# Mock CSSSanitizer for testing
class MockCSSSanitizer:
    def sanitize_css(self, css):
        return css

# Test cases
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

def test_cleaner_clean_with_disallowed_tags():
    cleaner = Cleaner(strip=True)
    text = "<div><p>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<p>Hello, <b>World</b>!</p>"

def test_cleaner_clean_with_strip_comments():
    cleaner = Cleaner(strip_comments=False)
    text = "<div><!-- Comment --><p>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><!-- Comment --><p>Hello, <b>World</b>!</p></div>"

def test_cleaner_clean_with_filters():
    class TestFilter(Filter):
        def filter(self, token):
            if token["type"] == "Characters":
                return {"type": "Characters", "data": token["data"].upper()}
            return token

    cleaner = Cleaner(filters=[TestFilter])
    text = "<div><p>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><p>HELLO, <b>WORLD</b>!</p></div>"

def test_cleaner_clean_with_css_sanitizer():
    cleaner = Cleaner(css_sanitizer=MockCSSSanitizer())
    text = "<div><p style='color: red;'>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><p style='color: red;'>Hello, <b>World</b>!</p></div>"

def test_cleaner_clean_with_invisible_characters():
    cleaner = Cleaner()
    text = "<div>Hello, <b>World</b>!\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F</div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div>Hello, <b>World</b>!?????????????????????????</div>"

def test_cleaner_clean_with_unescaped_entities():
    cleaner = Cleaner()
    text = "<div><p>Hello, <b>World</b>! &amp; &lt; &gt; &quot; &#x27;</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><p>Hello, <b>World</b>! &amp; &lt; &gt; &quot; &#x27;</p></div>"

def test_cleaner_clean_with_svg_attributes():
    cleaner = Cleaner()
    text = '<div><svg><a xlink:href="http://example.com"><path d="M10 10 L20 20"></path></a></svg></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><svg><a xlink:href="http://example.com"><path d="M10 10 L20 20"></path></a></svg></div>'

def test_cleaner_clean_with_style_attribute():
    cleaner = Cleaner(css_sanitizer=MockCSSSanitizer())
    text = '<div><p style="color: red;">Hello, <b>World</b>!</p></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><p style="color: red;">Hello, <b>World</b>!</p></div>'

def test_cleaner_clean_with_invalid_style_attribute():
    cleaner = Cleaner(css_sanitizer=MockCSSSanitizer())
    text = '<div><p style="color: red; background: url(http://example.com/image.jpg);">Hello, <b>World</b>!</p></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><p style="color: red;">Hello, <b>World</b>!</p></div>'

def test_cleaner_clean_with_invalid_uri_value():
    cleaner = Cleaner()
    text = '<div><a href="ftp://example.com">Link</a></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><a href="ftp://example.com">Link</a></div>'

def test_cleaner_clean_with_local_href():
    cleaner = Cleaner()
    text = '<div><svg><a xlink:href="http://example.com"><path d="M10 10 L20 20"></path></a></svg></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><svg><a xlink:href="http://example.com"><path d="M10 10 L20 20"></path></a></svg></div>'

def test_cleaner_clean_with_empty_tag():
    cleaner = Cleaner()
    text = '<div><p></p></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><p></p></div>'

def test_cleaner_clean_with_empty_tag_and_attributes():
    cleaner = Cleaner()
    text = '<div><p id="test"></p></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><p id="test"></p></div>'

def test_cleaner_clean_with_empty_tag_and_attributes_and_style():
    cleaner = Cleaner(css_sanitizer=MockCSSSanitizer())
    text = '<div><p id="test" style="color: red;"></p></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><p id="test" style="color: red;"></p></div>'

def test_cleaner_clean_with_empty_tag_and_attributes_and_style_and_class():
    cleaner = Cleaner(css_sanitizer=MockCSSSanitizer())
    text = '<div><p id="test" class="test" style="color: red;"></p></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><p id="test" class="test" style="color: red;"></p></div>'

def test_cleaner_clean_with_empty_tag_and_attributes_and_style_and_class_and_data():
    cleaner = Cleaner(css_sanitizer=MockCSSSanitizer())
    text = '<div><p id="test" class="test" style="color: red;" data-test="test"></p></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><p id="test" class="test" style="color: red;" data-test="test"></p></div>'

def test_cleaner_clean_with_empty_tag_and_attributes_and_style_and_class_and_data_and_title():
    cleaner = Cleaner(css_sanitizer=MockCSSSanitizer())
    text = '<div><p id="test" class="test" style="color: red;" data-test="test" title="test"></p></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><p id="test" class="test" style="color: red;" data-test="test" title="test"></p></div>'

def test_cleaner_clean_with_empty_tag_and_attributes_and_style_and_class_and_data_and_title_and_lang():
    cleaner = Cleaner(css_sanitizer=MockCSSSanitizer())
    text = '<div><p id="test" class="test" style="color: red;" data-test="test" title="test" lang="en"></p></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><p id="test" class="test" style="color: red;" data-test="test" title="test" lang="en"></p></div>'

def test_cleaner_clean_with_empty_tag_and_attributes_and_style_and_class_and_data_and_title_and_lang_and_dir():
    cleaner = Cleaner(css_sanitizer=MockCSSSanitizer())
    text = '<div><p id="test" class="test" style="color: red;" data-test="test" title="test" lang="en" dir="ltr"></p></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><p id="test" class="test" style="color: red;" data-test="test" title="test" lang="en" dir="ltr"></p></div>'

def test_cleaner_clean_with_empty_tag_and_attributes_and_style_and_class_and_data_and_title_and_lang_and_dir_and_xmlns():
    cleaner = Cleaner(css_sanitizer=MockCSSSanitizer())
    text = '<div><p id="test" class="test" style="color: red;" data-test="test" title="test" lang="en" dir="ltr" xmlns="http://www.w3.org/1999/xhtml"></p></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><p id="test" class="test" style="color: red;" data-test="test" title="test" lang="en" dir="ltr" xmlns="http://www.w3.org/1999/xhtml"></p></div>'

def test_cleaner_clean_with_empty_tag_and_attributes_and_style_and_class_and_data_and_title_and_lang_and_dir_and_xmlns_and_xlink():
    cleaner = Cleaner(css_sanitizer=MockCSSSanitizer())
    text = '<div><p id="test" class="test" style="color: red;" data-test="test" title="test" lang="en" dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xlink:href="http://example.com"></p></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><p id="test" class="test" style="color: red;" data-test="test" title="test" lang="en" dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xlink:href="http://example.com"></p></div>'

def test_cleaner_clean_with_empty_tag_and_attributes_and_style_and_class_and_data_and_title_and_lang_and_dir_and_xmlns_and_xlink_and_svg():
    cleaner = Cleaner(css_sanitizer=MockCSSSanitizer())
    text = '<div><p id="test" class="test" style="color: red;" data-test="test" title="test" lang="en" dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xlink:href="http://example.com"><svg><path d="M10 10 L20 20"></path></svg></p></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><p id="test" class="test" style="color: red;" data-test="test" title="test" lang="en" dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xlink:href="http://example.com"><svg><path d="M10 10 L20 20"></path></svg></p></div>'

def test_cleaner_clean_with_empty_tag_and_attributes_and_style_and_class_and_data_and_title_and_lang_and_dir_and_xmlns_and_xlink_and_svg_and_a():
    cleaner = Cleaner(css_sanitizer=MockCSSSanitizer())
    text = '<div><p id="test" class="test" style="color: red;" data-test="test" title="test" lang="en" dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xlink:href="http://example.com"><svg><a xlink:href="http://example.com"><path d="M10 10 L20 20"></path></a></svg></p></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><p id="test" class="test" style="color: red;" data-test="test" title="test" lang="en" dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xlink:href="http://example.com"><svg><a xlink:href="http://example.com"><path d="M10 10 L20 20"></path></a></svg></p></div>'

def test_cleaner_clean_with_empty_tag_and_attributes_and_style_and_class_and_data_and_title_and_lang_and_dir_and_xmlns_and_xlink_and_svg_and_a_and_path():
    cleaner = Cleaner(css_sanitizer=MockCSSSanitizer())
    text = '<div><p id="test" class="test" style="color: red;" data-test="test" title="test" lang="en" dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xlink:href="http://example.com"><svg><a xlink:href="http://example.com"><path d="M10 10 L20 20"></path></a></svg></p></div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div><p id="test" class="test" style="color: red;" data-test="test" title="test" lang="en" dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xlink:href="http://example.com"><svg><a xlink:href="http://example.com"><path d="M10 10 L20 20"></path></a></svg></p></div>'

def test_cleaner_clean_with_empty_tag_and_attributes_and_style_and_class_and_data