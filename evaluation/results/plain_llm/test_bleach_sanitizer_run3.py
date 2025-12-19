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
    text = "<div><script>alert('xss');</script></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div></div>"

def test_cleaner_clean_with_allowed_tags():
    cleaner = Cleaner(tags={"div", "span"})
    text = "<div><script>alert('xss');</script></div><span>safe</span>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div></div><span>safe</span>"

def test_cleaner_clean_with_allowed_attributes():
    cleaner = Cleaner(attributes={"a": ["href"]})
    text = "<a href='http://example.com'>link</a><a href='javascript:alert(1)'>link</a>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<a href='http://example.com'>link</a><a>link</a>"

def test_cleaner_clean_with_allowed_protocols():
    cleaner = Cleaner(protocols={"http"})
    text = "<a href='http://example.com'>link</a><a href='https://example.com'>link</a>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<a href='http://example.com'>link</a><a>link</a>"

def test_cleaner_clean_with_strip():
    cleaner = Cleaner(strip=True)
    text = "<div><script>alert('xss');</script></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == ""

def test_cleaner_clean_with_strip_comments():
    cleaner = Cleaner(strip_comments=True)
    text = "<div><!-- comment --></div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div></div>"

def test_cleaner_clean_with_filters():
    class MyFilter(Filter):
        def filter(self, token):
            if token["type"] == "Characters":
                return {"type": "Characters", "data": token["data"].upper()}
            return token

    cleaner = Cleaner(filters=[MyFilter])
    text = "<div>hello world</div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div>HELLO WORLD</div>"

def test_cleaner_clean_with_css_sanitizer():
    class MyCSSSanitizer:
        def sanitize_css(self, css):
            return css.replace("color:", "background-color:")

    cleaner = Cleaner(css_sanitizer=MyCSSSanitizer())
    text = "<div style='color:red;'>red</div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div style='background-color:red;'>red</div>"

def test_cleaner_clean_with_invisible_characters():
    cleaner = Cleaner()
    text = "<div>hello\u0000world</div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div>hello?world</div>"

def test_cleaner_clean_with_unescaped_entities():
    cleaner = Cleaner()
    text = "<div>&amp;</div>"
    sanitized = cleaner.clean(text)
    assert sanitized == "<div>&amp;</div>"

def test_cleaner_clean_with_svg_attributes():
    cleaner = Cleaner()
    text = '<svg><a xlink:href="http://example.com">link</a></svg>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<svg><a xlink:href="http://example.com">link</a></svg>'

def test_cleaner_clean_with_svg_local_href():
    cleaner = Cleaner()
    text = '<svg><a href="http://example.com">link</a></svg>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<svg><a href="http://example.com">link</a></svg>'

def test_cleaner_clean_with_style_attribute():
    cleaner = Cleaner()
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div style="color:red;">red</div>'

def test_cleaner_clean_with_style_attribute_and_css_sanitizer():
    class MyCSSSanitizer:
        def sanitize_css(self, css):
            return css.replace("color:", "background-color:")

    cleaner = Cleaner(css_sanitizer=MyCSSSanitizer())
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div style="background-color:red;">red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer():
    cleaner = Cleaner()
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div style="color:red;">red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_allowed():
    cleaner = Cleaner(attributes={"div": ["style"]})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div style="color:red;">red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed():
    cleaner = Cleaner()
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div style="">red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed():
    cleaner = Cleaner(attributes={"div": []})
    text = '<div style="color:red;">red</div>'
    sanitized = cleaner.clean(text)
    assert sanitized == '<div>red</div>'

def test_cleaner_clean_with_style_attribute_and_no_css_sanitizer_and_style_not_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no_style_allowed_and_no