import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.textwrap as textwrap
from data.complicated_tests.textwrap import *

import re

def test_data_complicated_tests_textwrap_1():
    text = " " * 100
    w = textwrap.TextWrapper(width=10)
    w._munge_whitespace(text)

def test_10():
    text = " " * 100
    w = textwrap.TextWrapper(width=10)
    print(w.initial_indent)

def test_15():
    text = " " * 100
    w = textwrap.TextWrapper(width=10)
    print(w.subsequent_indent)

def test_17():
    text = " " * 100
    w = textwrap.TextWrapper(width=10)
    w._split(text)

def test_66():
    text = " " * 100
    w = textwrap.TextWrapper(width=10)
    w._wrap_chunks(['a', 'b', 'c'])

def test_74():
    text = " " * 100
    w = textwrap.TextWrapper(width=10)
    print(w.wordsep_re)

def test_78():
    text = " " * 100
    w = textwrap.TextWrapper(width=10)
    print(w.wordsep_simple_re)

def test_96():
    text = " " * 100
    w = textwrap.TextWrapper(width=10)
    w._fix_sentence_endings(['.', '?', '!', '', 'etc'])

def test_102():
    text = " " * 100
    w = textwrap.TextWrapper(width=10)
    w._handle_long_word(['a' * 100], [], 0, 10)

def test_103():
    text = " " * 100
    w = textwrap.TextWrapper(width=10)
    w._handle_long_word(['a' * 100], ['a'], 9, 10)

def test_107():
    text = " " * 100
    w = textwrap.TextWrapper(width=10)
    print(w.sentence_end_re)

def test_112():
    text = " " * 100
    w = textwrap.TextWrapper(width=10)
    w.__init__(width=10, initial_indent="", subsequent_indent="")

def test_126():
    text = "x" * 10
