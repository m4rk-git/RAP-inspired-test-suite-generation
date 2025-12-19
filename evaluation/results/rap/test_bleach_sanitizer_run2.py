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
    cleaner.clean("<a href='http://example.com'>Test</a>")

def test_2():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean('')

def test_3():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("&")

def test_5():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://example.com' title='Test'>Test</a>")

def test_7():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://example.com'>Test</a>")

def test_8():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://example.com'>Test</a>")

def test_12():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a>Test</a>")

def test_31():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://example.com'>Test</a>")

def test_38():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://example.com'>Test</a>")

def test_41():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://example.com'>Test</a>")

def test_46():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://example.com'>Test</a>")

def test_50():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://example.com'>Test</a>")

def test_53():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://example.com'>Test</a>")

def test_54():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://example.com'>Test</a>")

def test_57():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://example.com'>Test</a>")

def test_86():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='http://example.com'>Test</a>")

def test_124():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner

def test_data_complicated_tests_bleach_sanitizer_2():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.parser.parseFragment("")

def test_166():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_182():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.parser.parseFragment("")

def test_186():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_204():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_218():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_226():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_231():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_232():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_234():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_236():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_238():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_242():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_244():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_245():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_247():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_249():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_326():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_340():
    from bleach.sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("")

def test_392():
    from bleach.sanitizer import Cleaner

def test_data_complicated_tests_bleach_sanitizer_3():
    from bleach_sanitizer import Cleaner, NoCssSanitizerWarning
    cleaner = Cleaner()
    with warnings.catch_warnings(record=True) as w:
        cleaner.clean("test")
        assert len(w) == 1
        assert issubclass(w[-1].category, NoCssSanitizerWarning)

def test_166():
    from bleach_sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("<a href='http://example.com'>test</a>")

def test_182():
    from bleach_sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("<a href='#'>test</a>")

def test_186():
    from bleach_sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("<a href='example.com'>test</a>")

def test_204():
    from bleach_sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("<style>test</style>")

def test_218():
    from bleach_sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("<a href='https://example.com'>test</a>")

def test_226():
    from bleach_sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("<a href='http://example.com'>test</a>")

def test_231():
    from bleach_sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("<a href='http://example.com'>test</a>")

def test_232():
    from bleach_sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("<a href='http://example.com'>test</a>")

def test_233():
    from bleach_sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("<a href='http://example.com'>test</a>")

def test_234():
    from bleach_sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("<a href='http://example.com'>test</a>")

def test_236():
    from bleach_sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("<a href='http://example.com'>test</a>")

def test_238():
    from bleach_sanitizer import Cleaner
    cleaner = Cleaner()
    cleaner.clean("<a href='http://example.com'>test</a>")

def test_242():
    from bleach_sanitizer import Cleaner
