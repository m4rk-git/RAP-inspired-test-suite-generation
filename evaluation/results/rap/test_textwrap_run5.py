import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.textwrap as textwrap
from data.complicated_tests.textwrap import *

import re

def test_data_complicated_tests_textwrap_1():
    textwrap.TextWrapper() # should trigger line 8
    
def test_2():
    textwrap._whitespace # should trigger line 15
    
def test_3():
    textwrap.TextWrapper(width=10) # should trigger line 66
    
def test_4():
    textwrap.TextWrapper().wordsep_re # should trigger line 74
    
def test_5():
    textwrap.TextWrapper().wordsep_simple_re # should trigger line 102
    
def test_6():
    textwrap.TextWrapper().unicode_whitespace_trans # should trigger line 66
    
def test_7():
    textwrap.TextWrapper().sentence_end_re # should trigger line 112
    
def test_8():
    textwrap.TextWrapper().width = 10 # should trigger line 126
    
def test_9():
    textwrap.TextWrapper().wordsep_re.split('test') # should trigger line 172
    
def test_10():
    textwrap.TextWrapper().wordsep_re.split('test', 1) # should trigger line 172
    
def test_11():
    textwrap.TextWrapper().wordsep_re.match('test') # should trigger line 174
    
def test_12():
    textwrap.TextWrapper().wordsep_re.match('test', 1, 2) # should trigger line 174
    
def test_13():
    textwrap.TextWrapper().wordsep_re.match('test', re.IGNORECASE) # should trigger line 174
    
def test_14():
    textwrap.TextWrapper().wordsep_re.findall('test') # should trigger line 175
    
def test_15():
    textwrap.TextWrapper().wordsep_re.findall('test', 1) # should trigger line 175
    
def test_16():
    textwrap.TextWrapper().wordsep_re.findall('test', re.IGNORECASE) # should trigger line 175
    
def test_17():
    textwrap.TextWrapper().wordsep_re.finditer('test') # should trigger line 177
    
def test_18():
    textwrap.TextWrapper().wordsep_re.finditer('test', 1, 2) # should trigger line 177
    
def test_19():
    textwrap.TextWrapper().wordsep_re.finditer('test', re.IGNORECASE) # should trigger line 177
