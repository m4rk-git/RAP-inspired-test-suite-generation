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
    import io
    lexer = shlex(io.StringIO('a b c'), posix=True)
    next(lexer)

def test_data_complicated_tests_shlex_2():
    import io
    lexer = shlex.StringIO('test')
    lexer.get_token()

def test_27_28():
    lexer = shlex.StringIO('test')
    lexer.sourcehook('file')

def test_33():
    lexer = shlex.StringIO('test')
    lexer.push_token('token')

def test_54_55():
    lexer = shlex.StringIO('test')
    lexer.eof

def test_59():
    lexer = shlex.StringIO('test')
    lexer._punctuation_chars = '()'

def test_61():
    lexer = shlex.StringIO('test')
    lexer.wordchars += '()'

def test_63_64():
    lexer = shlex.StringIO('test')
    lexer.wordchars.maketrans(dict.fromkeys('()'))

def test_72_74():
    lexer = shlex.StringIO('test')
    lexer.pushback.appendleft('token')

def test_78_86():
    lexer = shlex.StringIO('test')
    lexer.pop_source()

def test_88():
    lexer = shlex.StringIO('test')
    lexer.filestack

def test_92_95():
    lexer = shlex.StringIO('test')
    lexer.sourcehook('file')

def test_97():
    lexer = shlex.StringIO('test')
    lexer.split()

def test_102_105():
    lexer = shlex.StringIO('test')
    lexer.get_token()

def test_110_115():
    lexer = shlex.StringIO('test')
    lexer.push_source(lexer)

def test_118_119():
    lexer = shlex.StringIO('test')
    lexer.pop_source()

def test_121_122():
    lexer = shlex.StringIO('test')
    lexer.filestack

def test_125_126():
    lexer = shlex.StringIO('test')
    lexer.pushback.appendleft('token')

def test_128():
    lexer = shlex.StringIO('test')
    lexer.get_token()

def test_136():
    lexer = shlex.StringIO('test')
    lexer.push_token('token')

def test_140():
    lexer = shlex.StringIO('test')
    lexer.get_token()

def test_142():
    lexer = shlex

def test_data_complicated_tests_shlex_3():
    shlex().__init__()

def test_27_28():
    shlex(None, None, True, True)

def test_33():
    shlex(None, None, True, False)

def test_54_55():
    shlex(None, None, True).push_token('test')

def test_59():
    shlex(None, None, True).push_source('test')

def test_61():
    shlex(None, None, True).pop_source()

def test_63_64():
    shlex(None, None, True).get_token()

def test_72_74():
    shlex(None, None, True).read_token()

def test_78_86():
    shlex(None, None, True).sourcehook('"test"')

def test_88():
    shlex(None, None, True).error_leader()

def test_92_95():
    shlex(None, None, True).__iter__()

def test_97():
    shlex(None, None, True).__next__()

def test_102_105():
    shlex(None, None, True).get_token()

def test_110_115():
    shlex(None, None, True).push_source('test')

def test_118_119():
    shlex(None, None, True).pop_source()

def test_121_122():
    shlex(None, None, True).get_token()

def test_125_126():
    shlex(None, None, True).read_token()

def test_128():
    shlex(None, None, True).state

def test_136():
    shlex(None, None, True).push_token('test')

def test_140():
    shlex(None, None, True).read_token()

def test_142():
    shlex(None, None, True).push_token('test')

def test_145_146():
    shlex(None, None, True).get_token()

def test_149_150():
    shlex(None, None, True).read_token()

def test_152_155():
    shlex(None, None, True).read_token()

def test_157():
    shlex(None, None, True).state

def test_data_complicated_tests_shlex_4():
    shlex().get_token()

def test_73():
    shlex().push_token('test')

def test_85_86():
    x = shlex()
    x.read_token()
    x.instream.read()

def test_88():
    shlex().push_source('test')

def test_94_95():
    x = shlex()
    x.read_token()
    x.instream.read(1)

def test_97():
    x = shlex()
    x.read_token()
    x.infile = 'test'

def test_102_105():
    x = shlex()
    x.get_token()
    x.pushback.appendleft('test')

def test_110_115():
    x = shlex()
    x.push_source('test')
    x.get_token()
    x.sourcehook('test')

def test_118_119():
    x = shlex()
    x.push_source('test')
    x.get_token()
    x.infile = 'test'

def test_121_122():
    x = shlex()
    x.push_source('test')
    x.get_token()
    x.instream.read(1)

def test_125_126():
    x = shlex()
    x.push_source('test')
    x.get_token()
    x.instream.read()

def test_128():
    shlex().push_token(None)

def test_136():
    x = shlex()
    x.push_source('test')
    x.get_token()
    x.infile = 'test'

def test_140():
    x = shlex()
    x.push_source('test')
    x.get_token()
    x.instream.read(1)

def test_142():
    x = shlex()
    x.push_source('test')
    x.get_token()
    x.instream.read()

def test_145_146():
    x = shlex()
    x.push_source('test')
    x.get_token()
    x.instream.read(1)

def test_149_150():
    x = shlex()
    x.push_source('test')
    x.get_token()
    x.instream.read()

def test_152_155():
    x = shlex()
    x.push_source('test')
    x.get_token()
    x.instream
