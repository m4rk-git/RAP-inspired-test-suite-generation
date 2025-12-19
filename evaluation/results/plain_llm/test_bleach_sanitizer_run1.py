from data.complicated_tests.bleach_sanitizer import *
import pytest
from html5lib import parseFragment
from html5lib.serializer import serialize
from html5lib.treewalkers import getTreeWalker
from html5lib.filters.sanitizer import Filter

# Mock CSSSanitizer class for testing
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

def test_cleaner_clean_with_comments():
    cleaner = Cleaner(strip_comments=True)
    text = "<div><!-- Comment --><p>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><p>Hello, <b>World</b>!</p></div>"

def test_cleaner_clean_with_css_sanitizer():
    css_sanitizer = MockCSSSanitizer()
    cleaner = Cleaner(css_sanitizer=css_sanitizer)
    text = "<div><p style='color: red;'>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><p style='color: red;'>Hello, <b>World</b>!</p></div>"

def test_cleaner_clean_with_no_css_sanitizer():
    cleaner = Cleaner()
    text = "<div><p style='color: red;'>Hello, <b>World</b>!</p></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><p>Hello, <b>World</b>!</p></div>"

def test_cleaner_clean_with_invisible_characters():
    cleaner = Cleaner()
    text = "<div><p>Hello, <b>World</b>!</p></div>" + INVISIBLE_CHARACTERS
    sanitized = cleaner.clean(text)
    assert sanitized == "<div><p>Hello, <b>World</b>!</p></div>?"

def test_cleaner_clean_with_svg_attributes():
    cleaner = Cleaner()
    text = '<svg><rect fill="url(#pattern)"/></svg>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<svg><rect fill=" "/></svg>'

def test_cleaner_clean_with_svg_local_href():
    cleaner = Cleaner()
    text = '<svg><a xlink:href="local#id"/></svg>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<svg><a xlink:href=" "/></svg>'

def test_cleaner_clean_with_invalid_uri():
    cleaner = Cleaner()
    text = '<a href="javascript:alert(1)"></a>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<a></a>'

def test_cleaner_clean_with_empty_string():
    cleaner = Cleaner()
    text = ""
    sanitized = cleaner.clean(text)
    assert sanitized == ""

def test_cleaner_clean_with_non_text_type():
    cleaner = Cleaner()
    with pytest.raises(TypeError):
        cleaner.clean(123)

# Test BleachSanitizerFilter
def test_bleach_sanitizer_filter_init():
    filter = BleachSanitizerFilter(source=None)
    assert filter.allowed_tags == frozenset(ALLOWED_TAGS)
    assert filter.allowed_protocols == frozenset(ALLOWED_PROTOCOLS)
    assert filter.strip_disallowed_tags is False
    assert filter.strip_html_comments is True

def test_bleach_sanitizer_filter_sanitize_token():
    filter = BleachSanitizerFilter(source=None)
    token = {"type": "StartTag", "name": "div", "data": {}}
    sanitized = filter.sanitize_token(token)
    assert sanitized == token

def test_bleach_sanitizer_filter_sanitize_token_with_disallowed_tag():
    filter = BleachSanitizerFilter(source=None, strip_disallowed_tags=True)
    token = {"type": "StartTag", "name": "div", "data": {}}
    sanitized = filter.sanitize_token(token)
    assert sanitized is None

def test_bleach_sanitizer_filter_sanitize_token_with_comment():
    filter = BleachSanitizerFilter(source=None, strip_html_comments=True)
    token = {"type": "Comment", "data": "Comment"}
    sanitized = filter.sanitize_token(token)
    assert sanitized is None

def test_bleach_sanitizer_filter_sanitize_token_with_characters():
    filter = BleachSanitizerFilter(source=None)
    token = {"type": "Characters", "data": "Hello, World!"}
    sanitized = filter.sanitize_token(token)
    assert sanitized == token

def test_bleach_sanitizer_filter_sanitize_token_with_characters_with_invisible_characters():
    filter = BleachSanitizerFilter(source=None)
    token = {"type": "Characters", "data": "Hello, World!" + INVISIBLE_CHARACTERS}
    sanitized = filter.sanitize_token(token)
    assert sanitized == {"type": "Characters", "data": "Hello, World??"}

def test_bleach_sanitizer_filter_sanitize_token_with_svg_attributes():
    filter = BleachSanitizerFilter(source=None)
    token = {"type": "StartTag", "name": "rect", "data": {("http://www.w3.org/2000/svg", "fill"): "url(#pattern)"}}  # noqa: E501
    sanitized = filter.sanitize_token(token)
    assert sanitized == {"type": "StartTag", "name": "rect", "data": {("http://www.w3.org/2000/svg", "fill"): " "}}  # noqa: E501

def test_bleach_sanitizer_filter_sanitize_token_with_svg_local_href():
    filter = BleachSanitizerFilter(source=None)
    token = {"type": "StartTag", "name": "a", "data": {("http://www.w3.org/1999/xlink", "href"): "local#id"}}  # noqa: E501
    sanitized = filter.sanitize_token(token)
    assert sanitized == {"type": "StartTag", "name": "a", "data": {("http://www.w3.org/1999/xlink", "href"): " "}}  # noqa: E501

def test_bleach_sanitizer_filter_sanitize_token_with_invalid_uri():
    filter = BleachSanitizerFilter(source=None)
    token = {"type": "StartTag", "name": "a", "data": {("http://www.w3.org/1999/xlink", "href"): "javascript:alert(1)"}}  # noqa: E501
    sanitized = filter.sanitize_token(token)
    assert sanitized == {"type": "StartTag", "name": "a", "data": {}}

def test_bleach_sanitizer_filter_sanitize_token_with_empty_string():
    filter = BleachSanitizerFilter(source=None)
    token = {"type": "Characters", "data": ""}
    sanitized = filter.sanitize_token(token)
    assert sanitized == token

def test_bleach_sanitizer_filter_sanitize_token_with_non_text_type():
    filter = BleachSanitizerFilter(source=None)
    with pytest.raises(TypeError):
        filter.sanitize_token(123)

# Test attribute_filter_factory
def test_attribute_filter_factory_callable():
    def attr_filter(tag, attr, value):
        return True

    filter = attribute_filter_factory(attr_filter)
    assert filter("div", "class", "foo") is True

def test_attribute_filter_factory_list():
    filter = attribute_filter_factory(["class", "id"])
    assert filter("div", "class", "foo") is True
    assert filter("div", "id", "bar") is True
    assert filter("div", "style", "color: red") is False

def test_attribute_filter_factory_dict():
    filter = attribute_filter_factory({"div": ["class", "id"], "*": ["style"]})
    assert filter("div", "class", "foo") is True
    assert filter("div", "id", "bar") is True
    assert filter("div", "style", "color: red") is True
    assert filter("span", "class", "foo") is False
    assert filter("span", "id", "bar") is False
    assert filter("span", "style", "color: red") is True

def test_attribute_filter_factory_dict_with_callable():
    def attr_filter(tag, attr, value):
        return attr == "class"

    filter = attribute_filter_factory({"div": attr_filter, "*": ["style"]})
    assert filter("div", "class", "foo") is True
    assert filter("div", "id", "bar") is False
    assert filter("div", "style", "color: red") is True
    assert filter("span", "class", "foo") is True
    assert filter("span", "id", "bar") is False
    assert filter("span", "style", "color: red") is True

# Test sanitize_uri_value
def test_sanitize_uri_value():
    filter = BleachSanitizerFilter(source=None)
    assert filter.sanitize_uri_value("http://example.com", frozenset(ALLOWED_PROTOCOLS)) == "http://example.com"
    assert filter.sanitize_uri_value("https://example.com", frozenset(ALLOWED_PROTOCOLS)) == "https://example.com"
    assert filter.sanitize_uri_value("mailto:example@example.com", frozenset(ALLOWED_PROTOCOLS)) == "mailto:example@example.com"
    assert filter.sanitize_uri_value("javascript:alert(1)", frozenset(ALLOWED_PROTOCOLS)) is None
    assert filter.sanitize_uri_value("ftp://example.com", frozenset(ALLOWED_PROTOCOLS)) is None
    assert filter.sanitize_uri_value("example.com", frozenset(ALLOWED_PROTOCOLS)) is None
    assert filter.sanitize_uri_value("#anchor", frozenset(ALLOWED_PROTOCOLS)) == "#anchor"
    assert filter.sanitize_uri_value("myprotocol://example.com", frozenset(["myprotocol"])) == "myprotocol://example.com"
    assert filter.sanitize_uri_value("http://example.com/path?query=value", frozenset(ALLOWED_PROTOCOLS)) == "http://example.com/path?query=value"
    assert filter.sanitize_uri_value("http://example.com/path?query=value#anchor", frozenset(ALLOWED_PROTOCOLS)) == "http://example.com/path?query=value#anchor"
    assert filter.sanitize_uri_value("http://example.com/path?query=value#anchor&other=value", frozenset(ALLOWED_PROTOCOLS)) == "http://example.com/path?query=value#anchor&other=value"
    assert filter.sanitize_uri_value("http://example.com/path?query=value#anchor&other=value&more=value", frozenset(ALLOWED_PROTOCOLS)) == "http://example.com/path?query=value#anchor&other=value&more=value"
    assert filter.sanitize_uri_value("http://example.com/path?query=value#anchor&other=value&more=value&even=more", frozenset(ALLOWED_PROTOCOLS)) == "http://example.com/path?query=value#anchor&other=value&more=value&even=more"
    assert filter.sanitize_uri_value("http://example.com/path?query=value#anchor&other=value&more=value&even=more&even=more", frozenset(ALLOWED_PROTOCOLS)) == "http://example.com/path?query=value#anchor&other=value&more=value&even=more&even=more"
    assert filter.sanitize_uri_value("http://example.com/path?query=value#anchor&other=value&more=value&even=more&even=more&even=more", frozenset(ALLOWED_PROTOCOLS)) == "http://example.com/path?query=value#anchor&other=value&more=value&even=more&even=more&even=more"
    assert filter.sanitize_uri_value("http://example.com/path?query=value#anchor&other=value&more=value&even=more&even=more&even=more&even=more", frozenset(ALLOWED_PROTOCOLS)) == "http://example.com/path?query=value#anchor&other=value&more=value&even=more&even=more&even=more&even=more"
    assert filter.sanitize_uri_value("http://example.com/path?query=value#anchor&other=value&more=value&even=more&even=more&even=more&even=more&even=more", frozenset(ALLOWED_PROTOCOLS)) == "http://example.com/path?query=value#anchor&other=value&more=value&even=more&even=more&even=more&even=more&even=more"
    assert filter.sanitize_uri_value("http://example.com/path?query=value#anchor&other=value&more=value&even=more&even=more&even=more&even=more&even=more&even=more", frozenset(ALLOWED_PROTOCOLS)) == "http://example.com/path?query=value#anchor&other=value&more=value&even=more&even=more&even=more&even=more&even=more&even=more"
    assert filter.sanitize_uri_value("http://example.com/path?query=value#anchor&other=value&more=value&even=more&even=more&even=more&even=more&even=more&even=more&even=more", frozenset(ALLOWED_PROTOCOLS)) == "http://example.com/path?query=value#anchor&other=value&more=value&even=more&even=more&even=more&even=more&even=more&even=more&even=more"
    assert filter.sanitize_uri_value("http://example.com