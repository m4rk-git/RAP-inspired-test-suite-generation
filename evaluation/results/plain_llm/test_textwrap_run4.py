from data.complicated_tests.textwrap import *
import pytest
from io import StringIO

def test_wrap():
    w = TextWrapper(width=10)
    assert w.wrap("Hello, world!") == ["Hello,", "world!"]
    assert w.wrap("This is a test.") == ["This is a", "test."]
    assert w.wrap("This is a test that is too long.") == ["This is a", "test that", "is too", "long."]
    assert w.wrap("This is a test that is too long and has a hyphenated-word.") == ["This is a", "test that", "is too", "long and", "has a", "hyphenated-word."]
    assert w.wrap("This is a test that is too long and has a hyphenated-word.", break_long_words=False) == ["This is a", "test that", "is too long", "and has a", "hyphenated-word."]
    assert w.wrap("This is a test that is too long and has a hyphenated-word.", break_on_hyphens=False) == ["This is a", "test that", "is too long and", "has a hyphenated-word."]
    assert w.wrap("This is a test that is too long and has a hyphenated-word.", break_long_words=False, break_on_hyphens=False) == ["This is a", "test that", "is too long and has a", "hyphenated-word."]
    assert w.wrap("This is a test that is too long and has a hyphenated-word.", width=5) == ["This", "is a", "test", "that", "is too", "long and", "has a", "hyphenated-word."]
    assert w.wrap("This is a test that is too long and has a hyphenated-word.", width=1) == ["T", "h", "i", "s", " ", "i", "s", " ", "a", " ", "t", "e", "s", "t", " ", "t", "h", "a", "t", " ", "i", "s", " ", "t", "o", "o", " ", "l", "o", "n", "g", " ", "a", "n", "d", " ", "h", "a", "s", " ", "a", " ", "h", "y", "p", "h", "e", "n", "-", "a", "t", "e", "d", "-", "w", "o", "r", "d", "."]

def test_fill():
    w = TextWrapper(width=10)
    assert w.fill("Hello, world!") == "Hello, world!"
    assert w.fill("This is a test.") == "This is a\ntest."
    assert w.fill("This is a test that is too long.") == "This is a\ntest that\nis too\nlong."
    assert w.fill("This is a test that is too long and has a hyphenated-word.") == "This is a\ntest that\nis too\nlong and\nhas a\nhyphenated-word."
    assert w.fill("This is a test that is too long and has a hyphenated-word.", break_long_words=False) == "This is a\ntest that\nis too long\nand has a\nhyphenated-word."
    assert w.fill("This is a test that is too long and has a hyphenated-word.", break_on_hyphens=False) == "This is a\ntest that\nis too long and\nhas a hyphenated-word."
    assert w.fill("This is a test that is too long and has a hyphenated-word.", break_long_words=False, break_on_hyphens=False) == "This is a\ntest that\nis too long and has a\nhyphenated-word."
    assert w.fill("This is a test that is too long and has a hyphenated-word.", width=5) == "This\nis a\ntest\nthat\nis too\nlong and\nhas a\nhyphenated-word."
    assert w.fill("This is a test that is too long and has a hyphenated-word.", width=1) == "T\nh\ni\ns\n \ni\ns\n \na\n \nt\ne\ns\nt\n \nt\nh\na\nt\n \ni\ns\n \nt\no\no\n \nl\no\nn\ng\n \na\nn\nd\n \nh\na\ns\n \na\n \nh\ny\np\nh\ne\nn\n-\na\nt\ne\nh\nd\na\nt\ne\n-\nw\no\nr\nd\n."

def test_shorten():
    assert shorten("Hello, world!", width=12) == "Hello, world!"
    assert shorten("Hello, world!", width=11) == "Hello, [...]"

def test_dedent():
    assert dedent("\tfoo\n\tbar") == "foo\nbar"
    assert dedent("  \thello there\n  \t  how are you?") == "hello there\n  how are you?"
    assert dedent("  \thello there\n  \t  how are you?\n") == "hello there\n  how are you?\n"

def test_indent():
    assert indent("foo\nbar", "  ") == "  foo\n  bar"
    assert indent("foo\nbar", "  ", lambda line: line.strip() != "") == "  foo\n  bar"
    assert indent("foo\nbar", "  ", lambda line: line.strip() == "") == "\n  bar"

def test_textwrap_module():
    assert wrap("Hello, world!") == ["Hello,", "world!"]
    assert fill("Hello, world!") == "Hello, world!"
    assert shorten("Hello, world!", width=12) == "Hello, world!"
    assert dedent("\tfoo\n\tbar") == "foo\nbar"
    assert indent("foo\nbar", "  ") == "  foo\n  bar"

def test_textwrap_module_with_kwargs():
    assert wrap("Hello, world!", width=10) == ["Hello,", "world!"]
    assert fill("Hello, world!", width=10) == "Hello, world!"
    assert shorten("Hello, world!", width=12) == "Hello, world!"
    assert dedent("\tfoo\n\tbar") == "foo\nbar"
    assert indent("foo\nbar", "  ") == "  foo\n  bar"

def test_textwrap_module_with_max_lines():
    w = TextWrapper(width=10, max_lines=1)
    assert w.wrap("Hello, world!") == ["Hello, world!"]
    assert w.fill("Hello, world!") == "Hello, world!"
    assert w.shorten("Hello, world!", width=12) == "Hello, world!"
    assert w.dedent("\tfoo\n\tbar") == "foo\nbar"
    assert w.indent("foo\nbar", "  ") == "  foo\n  bar"

def test_textwrap_module_with_placeholder():
    w = TextWrapper(width=10, placeholder='... ')
    assert w.wrap("Hello, world!") == ["Hello, world!"]
    assert w.fill("Hello, world!") == "Hello, world!"
    assert w.shorten("Hello, world!", width=12) == "Hello, world!"
    assert w.dedent("\tfoo\n\tbar") == "foo\nbar"
    assert w.indent("foo\nbar", "  ") == "  foo\n  bar"

def test_textwrap_module_with_tabsize():
    w = TextWrapper(width=10, tabsize=4)
    assert w.wrap("Hello, world!") == ["Hello,", "world!"]
    assert w.fill("Hello, world!") == "Hello, world!"
    assert w.shorten("Hello, world!", width=12) == "Hello, world!"
    assert w.dedent("\tfoo\n\tbar") == "foo\nbar"
    assert w.indent("foo\nbar", "  ") == "  foo\n  bar"

def test_textwrap_module_with_replace_whitespace():
    w = TextWrapper(width=10, replace_whitespace=False)
    assert w.wrap("Hello, world!") == ["Hello, world!"]
    assert w.fill("Hello, world!") == "Hello, world!"
    assert w.shorten("Hello, world!", width=12) == "Hello, world!"
    assert w.dedent("\tfoo\n\tbar") == "foo\nbar"
    assert w.indent("foo\nbar", "  ") == "  foo\n  bar"

def test_textwrap_module_with_expand_tabs():
    w = TextWrapper(width=10, expand_tabs=False)
    assert w.wrap("Hello, world!") == ["Hello, world!"]
    assert w.fill("Hello, world!") == "Hello, world!"
    assert w.shorten("Hello, world!", width=12) == "Hello, world!"
    assert w.dedent("\tfoo\n\tbar") == "foo\nbar"
    assert w.indent("foo\nbar", "  ") == "  foo\n  bar"

def test_textwrap_module_with_fix_sentence_endings():
    w = TextWrapper(width=10, fix_sentence_endings=True)
    assert w.wrap("Hello, world!") == ["Hello,", "world!"]
    assert w.fill("Hello, world!") == "Hello, world!"
    assert w.shorten("Hello, world!", width=12) == "Hello, world!"
    assert w.dedent("\tfoo\n\tbar") == "foo\nbar"
    assert w.indent("foo\nbar", "  ") == "  foo\n  bar"

def test_textwrap_module_with_drop_whitespace():
    w = TextWrapper(width=10, drop_whitespace=False)
    assert w.wrap("Hello, world!") == ["Hello,", "world!"]
    assert w.fill("Hello, world!") == "Hello, world!"
    assert w.shorten("Hello, world!", width=12) == "Hello, world!"
    assert w.dedent("\tfoo\n\tbar") == "foo\nbar"
    assert w.indent("foo\nbar", "  ") == "  foo\n  bar"

def test_textwrap_module_with_initial_indent():
    w = TextWrapper(width=10, initial_indent="  ")
    assert w.wrap("Hello, world!") == ["  Hello,", "  world!"]
    assert w.fill("Hello, world!") == "  Hello,\n  world!"
    assert w.shorten("Hello, world!", width=12) == "Hello, world!"
    assert w.dedent("\tfoo\n\tbar") == "foo\nbar"
    assert w.indent("foo\nbar", "  ") == "  foo\n  bar"

def test_textwrap_module_with_subsequent_indent():
    w = TextWrapper(width=10, subsequent_indent="  ")
    assert w.wrap("Hello, world!") == ["Hello,", "  world!"]
    assert w.fill("Hello, world!") == "Hello,\n  world!"
    assert w.shorten("Hello, world!", width=12) == "Hello, world!"
    assert w.dedent("\tfoo\n\tbar") == "foo\nbar"
    assert w.indent("foo\nbar", "  ") == "  foo\n  bar"

def test_textwrap_module_with_break_long_words():
    w = TextWrapper(width=10, break_long_words=False)
    assert w.wrap("Hello, world!") == ["Hello,", "world!"]
    assert w.fill("Hello, world!") == "Hello, world!"
    assert w.shorten("Hello, world!", width=12) == "Hello, world!"
    assert w.dedent("\tfoo\n\tbar") == "foo\nbar"
    assert w.indent("foo\nbar", "  ") == "  foo\n  bar"

def test_textwrap_module_with_break_on_hyphens():
    w = TextWrapper(width=10, break_on_hyphens=False)
    assert w.wrap("Hello, world!") == ["Hello,", "world!"]
    assert w.fill("Hello, world!") == "Hello, world!"
    assert w.shorten("Hello, world!", width=12) == "Hello, world!"
    assert w.dedent("\tfoo\n\tbar") == "foo\nbar"
    assert w.indent("foo\nbar", "  ") == "  foo\n  bar"

def test_textwrap_module_with_max_lines_and_placeholder():
    w = TextWrapper(width=10, max_lines=1, placeholder='... ')
    assert w.wrap("Hello, world!") == ["Hello, world!"]
    assert w.fill("Hello, world!") == "Hello, world!"
    assert w.shorten("Hello, world!", width=12) == "Hello, world!"
    assert w.dedent("\tfoo\n\tbar") == "foo\nbar"
    assert w.indent("foo\nbar", "  ") == "  foo\n  bar"

def test_textwrap_module_with_max_lines_and_initial_indent():
    w = TextWrapper(width=10, max_lines=1, initial_indent="  ")
    assert w.wrap("Hello, world!") == ["  Hello,", "  world!"]
    assert w.fill("Hello, world!") == "  Hello,\n  world!"
    assert w.shorten("Hello, world!", width=12) == "Hello, world!"
    assert w.dedent("\tfoo\n\tbar") == "foo\nbar"
    assert w.indent("foo\nbar", "  ") == "  foo\n  bar"

def test_textwrap_module_with_max_lines_and_subsequent_indent():
    w = TextWrapper(width=10, max_lines=1, subsequent_indent="  ")
    assert w.wrap("Hello, world!") == ["Hello,", "  world!"]
    assert w.fill("Hello, world!") == "Hello,\n  world!"
    assert w.shorten("Hello, world!", width=12) == "Hello, world!"
    assert w.dedent("\tfoo\n\tbar") == "foo\nbar"
    assert w.indent("foo\nbar", "  ") == "  foo\n