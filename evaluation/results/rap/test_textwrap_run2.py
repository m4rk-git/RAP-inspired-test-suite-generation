import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.textwrap as textwrap
from data.complicated_tests.textwrap import *

import re

def test_data_complicated_tests_textwrap_1():
    textwrap.TextWrapper._munge_whitespace("")

def test_10():
    textwrap.TextWrapper._split("")

def test_15():
    textwrap.TextWrapper._fix_sentence_endings([""])

def test_17():
    textwrap.TextWrapper._handle_long_word([], [], 0, 0)

def test_66():
    textwrap.TextWrapper._wrap_chunks([""])

def test_74():
    textwrap.TextWrapper.wordsep_re.split("")

def test_76():
    textwrap.TextWrapper.wordsep_re.split("")

def test_96():
    textwrap.TextWrapper._split_chunks("")

def test_102():
    textwrap.TextWrapper.fill("")

def test_107():
    textwrap.TextWrapper.wrap("")

def test_112():
    textwrap.TextWrapper.fill("")

def test_126():
    textwrap.TextWrapper.__init__(width=70)

def test_137():
    textwrap.TextWrapper.__init__(width=70)

def test_143():
    textwrap.TextWrapper._munge_whitespace("\t")

def test_150():
    textwrap.TextWrapper._wrap_chunks([""])

def test_154():
    textwrap.TextWrapper._wrap_chunks([""])

def test_157():
    textwrap.TextWrapper._wrap_chunks(["", ""])

def test_172():
    textwrap.TextWrapper._split([""])

def test_173():
    textwrap.TextWrapper._split([""])

def test_175():
    textwrap.TextWrapper._split_chunks("")

def test_177():
    textwrap.TextWrapper._split_chunks("")

def test_179():
    textwrap.TextWrapper._handle_long_word([""], [], 0, 0)

def test_207():
    textwrap.TextWrapper.__init__(width=70)

def test_208():
    textwrap.TextWrapper.__init__(width=70)

def test_210():
    textwrap.TextWrapper._handle_long_word([""], [], 0, 0)

def test_214():
    textwrap.TextWrapper._handle_long_word([""], [], 0, 0)

def test_217():
    textwrap.TextWrapper._handle_long_word([""], [], 0, 0)

def test_220():
    textwrap.TextWrapper._
