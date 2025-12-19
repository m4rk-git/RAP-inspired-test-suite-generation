import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.textwrap as textwrap
from data.complicated_tests.textwrap import *

import re

def test_data_complicated_tests_textwrap_1():
    textwrap.dedent(textwrap.dedent("\tfoo\n\tbar"))

def test_10():
    textwrap.dedent(textwrap.dedent("  \thello there\n  \t  how are you?"))

def test_15():
    textwrap.dedent(textwrap.dedent("Hello there.\n  This is indented."))

def test_17():
    textwrap.dedent(textwrap.dedent("Hello there.\n  This is indented."))

def test_66():
    textwrap.TextWrapper().wordsep_re

def test_74_78():
    textwrap.TextWrapper().wordsep_re.compile("")

def test_96():
    textwrap.TextWrapper().unicode_whitespace_trans

def test_102_103():
    textwrap.TextWrapper().unicode_whitespace_trans['\t']

def test_107():
    textwrap.TextWrapper().sentence_end_re.search("Hello there.")

def test_112():
    textwrap.dedent("Hello there.\n  This is indented.")

def test_126_137():
    textwrap.TextWrapper().width = -1

def test_143():
    textwrap.TextWrapper().width = 0

def test_150_154():
    textwrap.TextWrapper().width = -1

def test_157():
    textwrap.TextWrapper().width = 0

def test_172_173():
    textwrap.TextWrapper().wordsep_re.split("Hello there.")

def test_175_177():
    textwrap.TextWrapper().wordsep_re.split("Hello there.")

def test_179():
    textwrap.TextWrapper().wordsep_re.split("Hello there.")

def test_188_193():
    textwrap.TextWrapper().sentence_end_re.search("Hello there.")

def test_195():
    textwrap.TextWrapper().sentence_end_re.search("Hello there.")

def test_197():
    textwrap.TextWrapper().sentence_end_re.search("Hello there.")

def test_207_208():
    textwrap.TextWrapper().break_long_words = False

def test_210():
    textwrap.TextWrapper().break_long_words = False

def test_214_217():
    textwrap.TextWrapper().break_long
