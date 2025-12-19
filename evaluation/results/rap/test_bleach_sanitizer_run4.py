import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.bleach_sanitizer as bleach_sanitizer
from data.complicated_tests.bleach_sanitizer import *

from itertools import chain
import re
import warnings
from xml.sax.saxutils import unescape
from bleach import html5lib_shim
from bleach import parse_shim

def test_data_complicated_tests_bleach_sanitizer_1():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('')

def test_data_complicated_tests_bleach_sanitizer_2():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u0000")

def test_166():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u000a")

def test_182():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"")

def test_186():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u000a")

def test_191():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u0000")

def test_192():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u000a")

def test_203():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u0000")

def test_204():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u000a")

def test_206():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u0000")

def test_217():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u0000")

def test_218():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u000a")

def test_220():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u0000")

def test_222():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u0000")

def test_223():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u000a")

def test_224():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u0000")

def test_226():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u000a")

def test_228():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u0000")

def test_229():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean(u"\u000a")

def test_231():
    cleaner = bleach_sanitizer.Cleaner

def test_data_complicated_tests_bleach_sanitizer_3():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://test'>Test</a>")

def test_166():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://test'>Test</a>")

def test_182():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://test'>Test</a>")

def test_186():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://test'>Test</a>")

def test_204():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://test'>Test</a>")

def test_218():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://test'>Test</a>")

def test_223():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://test'>Test</a>")

def test_224():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://test'>Test</a>")

def test_226():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://test'>Test</a>")

def test_228():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://test'>Test</a>")

def test_229():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://test'>Test</a>")

def test_231():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://test'>Test</a>")

def test_232():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://test'>Test</a>")

def test_234():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://test'>Test</a>")

def test_236():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://test'>Test</a>")

def test_238():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean

def test_data_complicated_tests_bleach_sanitizer_4():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_166():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_182():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_186():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_204():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_218():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_226():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_231():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_232():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_233():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_236():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_238():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_242():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_244():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_245():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_247():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_249():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_326():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<div>test</div>')

def test_329():
    cleaner = bleach

def test_data_complicated_tests_bleach_sanitizer_5():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<a href="http://example.com">Link</a>')

def test_166():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<style>body { background-color: red; }')

def test_182():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<img src="http://example.com" alt="Image">')

def test_186():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<script>alert("XSS")</script>')

def test_204():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<img src="http://example.com" alt="Image">')

def test_218():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<svg><rect x="0" y="0" width="100" height="100"/></svg>')

def test_226():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<a href="javascript:alert('')">Link</a>')

def test_231_234():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<a href="http://example.com">Link</a>')

def test_236():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<a href="mailto:example@example.com">Link</a>')

def test_238():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<a href="tel:+1234567890">Link</a>')

def test_242():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<a href="http://example.com">Link</a>')

def test_244_245():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<a href="http://example.com">Link</a>')

def test_247():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<a href="http://example.com">Link</a>')

def test_249():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<a href="http://example.com">Link</a>')

def test_326():
    cleaner = bleach_sanitizer
