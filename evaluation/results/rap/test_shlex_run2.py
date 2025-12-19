import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.shlex as shlex
from data.complicated_tests.shlex import *

import sys
from io import StringIO
from collections import deque
import os.path

def test_data_complicated_tests_shlex_1():
    import shlex
    _ = shlex.shlex()

def test_data_complicated_tests_shlex_2():
    lexer = shlex()
    lexer.instream = StringIO('a b c')
    lexer.get_token()

def test_21_25():
    lexer = shlex()
    lexer.instream = StringIO('a b c')
    lexer.get_token()
    lexer.push_token('x')

def test_27_31():
    lexer = shlex()
    lexer.instream = StringIO('a b c')
    lexer.get_token()
    lexer.push_token('x')
    lexer.get_token()

def test_33_35():
    lexer = shlex()
    lexer.instream = StringIO('a b c')
    lexer.get_token()
    lexer.push_token('x')
    lexer.get_token()
    lexer.pop_source()

def test_37_38():
    lexer = shlex()
    lexer.instream = StringIO('a b c')
    lexer.get_token()
    lexer.push_token('x')
    lexer.get_token()
    lexer.pop_source()
    lexer.push_source('a b c')

def test_40_57():
    lexer = shlex()
    lexer.instream = StringIO('a b c')
    lexer.get_token()
    lexer.push_token('x')
    lexer.get_token()
    lexer.pop_source()
    lexer.push_source('a b c')
    lexer.push_token('y')

def test_59():
    lexer = shlex()
    lexer.instream = StringIO('a b c')
    lexer.get_token()
    lexer.push_token('x')
    lexer.get_token()
    lexer.pop_source()
    lexer.push_source('a b c')
    lexer.push_token('y')
    lexer.get_token()

def test_61():
    lexer = shlex()
    lexer.instream = StringIO('a b c')
    lexer.get_token()
    lexer.push_token('x')
    lexer.get_token()
    lexer.pop_source()
    lexer.push_source('a b c')
    lexer.push_token('y')
    lexer.get_token()
    lexer.push_token('z')

def test_63_64():
    lexer = shlex()
    lexer.instream = StringIO('a b c')
    lexer.get_token()
    lexer.push_token('x')
    lexer.get_token()
    lexer.pop_source()
    lexer.push_source('a b c')
    lexer.push_token('y')
    lexer.get_token()
    lexer.push_token('z')
    lexer.instream = StringIO('a b c')

def test_68():
    lexer = shlex

def test_data_complicated_tests_shlex_3():
    lexer = shlex()
    lexer.get_token()

def test_24():
    lexer = shlex()
    lexer.pop_source()

def test_31():
    lexer = shlex()
    lexer.sourcehook("newfile")

def test_38():
    lexer = shlex()
    lexer.get_token()

def test_54():
    lexer = shlex()
    lexer.punctuation_chars = True
    lexer.get_token()

def test_55():
    lexer = shlex()
    lexer.punctuation_chars = '();<>|&'
    lexer.get_token()

def test_59():
    lexer = shlex(shlex())
    lexer.get_token()

def test_61():
    lexer = shlex()
    lexer.wordchars = 'abc'
    lexer.get_token()

def test_63():
    lexer = shlex()
    lexer.wordchars.maketrans(dict.fromkeys('abc'))
    lexer.get_token()

def test_64():
    lexer = shlex()
    lexer.wordchars.translate(lexer.wordchars.maketrans(dict.fromkeys('abc')))
    lexer.get_token()

def test_73():
    lexer = shlex()
    lexer.error_leader()

def test_78():
    lexer = shlex()
    lexer.push_source(StringIO("newstream"), "newfile")

def test_88():
    lexer = shlex()
    lexer.pop_source()

def test_94():
    lexer = shlex()
    lexer.filestack.appendleft(("newfile", StringIO("newstream"), 1))

def test_95():
    lexer = shlex()
    lexer.filestack.appendleft(("newfile", StringIO("newstream"), 1))

def test_97():
    lexer = shlex()
    lexer.instream.close()
    lexer.pop_source()

def test_104():
    lexer = shlex()
    lexer.push_token("token")

def test_110():
    lexer = shlex()
    lexer.sourcehook("newfile")[0]

def test_111():
    lexer = shlex()
    lexer.sourcehook("newfile")[1]

def test_118():
    lexer = shlex()
    lexer.instream.readline()

def test_119():
    lexer = shlex()
    lexer.instream.readline()

def test_121():
    lexer = shlex()
    lexer.instream.readline()

def test_122():
    lexer = shlex()

def test_data_complicated_tests_shlex_4():
    lexer = shlex()
    lexer.get_token()
    
def test_31():
    shlex.instream = StringIO('test')
    lexer = shlex()
    lexer.get_token()
    
def test_38():
    lexer = shlex()
    lexer.state = 'a'
    lexer.get_token()
    
def test_54():
    lexer = shlex()
    lexer.punctuation_chars = 'test'
    lexer.push_token('test')
    
def test_55():
    lexer = shlex()
    lexer.punctuation_chars = True
    lexer.push_token('test')
    
def test_59():
    lexer = shlex()
    lexer._pushback_chars = deque('test')
    lexer.get_token()
    
def test_61():
    lexer = shlex()
    lexer.wordchars = 'test'
    lexer.get_token()
    
def test_63():
    lexer = shlex()
    lexer.wordchars = 'test'
    lexer.pushback = deque('test')
    lexer.get_token()
    
def test_64():
    lexer = shlex()
    lexer.wordchars = 'test'
    lexer.pushback = deque('test')
    lexer.get_token()
    
def test_73():
    lexer = shlex()
    lexer.debug = 1
    lexer.get_token()
    
def test_79():
    lexer = shlex()
    lexer.pushback = deque('test')
    lexer.get_token()
    
def test_85():
    lexer = shlex()
    lexer.filestack = deque([('test', StringIO('test'), 1)])
    lexer.pop_source()
    
def test_86():
    lexer = shlex()
    lexer.filestack = deque([('test', StringIO('test'), 1)])
    lexer.pop_source()
    
def test_88():
    lexer = shlex()
    lexer.debug = 1
    lexer.pop_source()
    
def test_94():
    lexer = shlex()
    lexer.instream = StringIO('test')
    lexer.get_token()
    
def test_95():
    lexer = shlex()
    lexer.instream = StringIO('test')
    lexer.get_token()
    
def test_97():
    lexer = shlex()
    lexer.debug = 1
    lexer.get_token()
    
def test_104():
    lexer = shlex()
    lexer.debug = 1
    lexer.get_token()
    
def test_110():
    lexer = shlex
