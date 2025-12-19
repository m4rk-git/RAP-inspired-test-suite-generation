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
    lex = shlex()
    lex.push_token('test')

def test_data_complicated_tests_shlex_2():
    lexer = shlex()
    lexer.debug = 2

def test_24_25():
    lexer = shlex()
    lexer.eof = 'EOF'

def test_31():
    lexer = shlex()
    lexer.instream = None

def test_38():
    lexer = shlex()
    lexer.instream = StringIO('test')

def test_54_55():
    lexer = shlex()
    lexer.debug = 1

def test_59():
    lexer = shlex()
    lexer.pushback.append('test')

def test_61():
    lexer = shlex()
    lexer.instream = StringIO('test')

def test_63_64():
    lexer = shlex()
    lexer.pushback.append('test')

def test_68():
    lexer = shlex()
    lexer.instream = StringIO('test')

def test_73():
    lexer = shlex()
    lexer.instream = StringIO('test')

def test_78_86():
    lexer = shlex()
    lexer.filestack.append((None, None, 1))

def test_88():
    lexer = shlex()
    lexer.instream = StringIO('test')

def test_92_95():
    lexer = shlex()
    lexer.filestack.append((None, StringIO('test'), 1))

def test_97():
    lexer = shlex()
    lexer.instream = StringIO('test')

def test_101_105():
    lexer = shlex()
    lexer.pushback.append('test')

def test_107():
    lexer = shlex()
    lexer.instream = StringIO('test')

def test_109_115():
    lexer = shlex()
    lexer.filestack.append((None, StringIO('test'), 1))

def test_117_119():
    lexer = shlex()
    lexer.filestack.append((None, StringIO('test'), 1))

def test_121_122():
    lexer = shlex()
    lexer.instream = StringIO('test')

def test_124_126():
    lexer = shlex()
    lexer.instream = StringIO('test')

def test_128_129():
    lexer = shlex()
    lexer.instream = StringIO('test')

def test_132_136():
    lexer = shlex()

def test_data_complicated_tests_shlex_3():
    lexer = shlex()
    lexer.infile = "test.txt"
    lexer.instream = StringIO("hello world\n")
    lexer.get_token()

def test_24_25():
    lexer = shlex()
    lexer.infile = "test.txt"
    lexer.instream = StringIO("hello world\n")
    lexer.push_token("token")
    lexer.get_token()

def test_31():
    lexer = shlex()
    lexer.infile = "test.txt"
    lexer.instream = StringIO("hello world\n")
    lexer.whitespace_split = True
    lexer.get_token()

def test_38():
    lexer = shlex()
    lexer.infile = "test.txt"
    lexer.instream = StringIO("hello world\n")
    lexer.posix = True
    lexer.get_token()

def test_54_55():
    lexer = shlex()
    lexer.infile = "test.txt"
    lexer.instream = StringIO("hello world\n")
    lexer.punctuation_chars = True
    lexer.get_token()

def test_59():
    lexer = shlex()
    lexer.infile = "test.txt"
    lexer.instream = StringIO("hello world\n")
    lexer.pushback.append("token")
    lexer.get_token()

def test_61():
    lexer = shlex()
    lexer.infile = "test.txt"
    lexer.instream = StringIO("hello world\n")
    lexer.state = 'a'
    lexer.get_token()

def test_63_64():
    lexer = shlex()
    lexer.infile = "test.txt"
    lexer.instream = StringIO("hello world\n")
    lexer.wordchars = 'abc'
    lexer.get_token()

def test_68():
    lexer = shlex()
    lexer.infile = "test.txt"
    lexer.instream = StringIO("hello world\n")
    lexer.debug = 1
    lexer.get_token()

def test_73():
    lexer = shlex()
    lexer.infile = "test.txt"
    lexer.instream = StringIO("hello world\n")
    lexer._pushback_chars.append("token")
    lexer.get_token()

def test_78_86():
    lexer = shlex()
    lexer.infile = "test.txt"
    lexer.instream = StringIO("hello world\n")
    lexer.filestack.appendleft(("test.txt", lexer.instream, 1))
    lexer.pop_source()
    
def test_88():
    lexer
