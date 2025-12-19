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
    cleaner.clean("")

def test_2():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("abc")

def test_3():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.tags = bleach_sanitizer.ALLOWED_TAGS
    cleaner.clean("")

def test_4():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.attributes = bleach_sanitizer.ALLOWED_ATTRIBUTES
    cleaner.clean("")

def test_5():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.protocols = bleach_sanitizer.ALLOWED_PROTOCOLS
    cleaner.clean("")

def test_6():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.strip = False
    cleaner.clean("abc")

def test_7():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.strip_comments = True
    cleaner.clean("abc")

def test_8():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.strip_comments = False
    cleaner.clean("abc")

def test_9():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.strip_comments = False
    cleaner.clean("abc")
    print(bleach_sanitizer.INVISIBLE_CHARACTERS)

def test_10():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("abc")
    print(bleach_sanitizer.INVISIBLE_CHARACTERS)

def test_11():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("abc")
    print(bleach_sanitizer.INVISIBLE_CHARACTERS_RE)

def test_12():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("abc")
    print(bleach_sanitizer.INVISIBLE_REPLACEMENT_CHAR)

def test_13():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("abc")
    print(bleach_sanitizer.NOCssSanitizerWarning)

def test_14():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("abc")
    bleacher = bleach_sanitizer.NoCssSanitizerWarning()
    bleacher.__init__()

def test_15():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("abc")
    bleacher = bleach_sanitizer.NoCssSanitizerWarning()
    bleacher.__init__()
    print(bleacher)

def test_16():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("abc")
