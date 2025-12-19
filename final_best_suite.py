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
    cleaner.clean('<a href="#">Link</a>')

def test_data_complicated_tests_bleach_sanitizer_2():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('')

def test_data_complicated_tests_bleach_sanitizer_3():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_166():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_182():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_186():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_204():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_218():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_226():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_231():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_232():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_233():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_234():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_236():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_238():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_242():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_244():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_245():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_247():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_249():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_326():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_329():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_340():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_341():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_392():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_393():
    cleaner

def test_data_complicated_tests_bleach_sanitizer_4():
    cleaner = bleach_sanitizer.Cleaner(css_sanitizer=None)
    cleaner.clean("example text")

def test_data_complicated_tests_bleach_sanitizer_5():
    cleaner = bleach_sanitizer.Cleaner()
    return cleaner.clean("")

def test_data_complicated_tests_bleach_sanitizer_6():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<a href="http://example.com">Test</a>')

def test_166():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<a href="http://example.com" title="Test">Test</a>')

def test_182():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('Test')

def test_186():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('Test & <script>alert("XSS")</script>')

def test_204():
    cleaner = bleach_sanitizer.Cleaner(css_sanitizer=bleach_sanitizer.CSSSanitizer())
    cleaner.clean('<style>body{color:red;}</style>')

def test_218():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<svg><rect fill="red"/></svg>')

def test_226():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<svg><rect fill="red"/></svg>')

def test_231():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<svg><a href="http://example.com"/></svg>')

def test_232():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<svg><a href="http://example.com"/></svg>')

def test_233():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<svg><a href="http://example.com"/></svg>')

def test_234():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<svg><a href="http://example.com"/></svg>')

def test_236():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<svg><a href="http://example.com"/></svg>')

def test_238():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<svg><a href="http://example.com"/></svg>')

def test_242():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<svg><a href="http://example.com"/></svg>')

def test_244():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('<svg><a href="http://example.com"/></svg>')

def test_245():
    cleaner
