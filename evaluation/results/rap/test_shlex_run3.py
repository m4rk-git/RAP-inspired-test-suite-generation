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
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_13():
    lexer = shlex()
    lexer.instream = sys.stdin

def test_15():
    lexer = shlex()
    lexer.instream = sys.stdin

def test_17():
    lexer = shlex()
    lexer.instream = sys.stdin

def test_19():
    lexer = shlex()
    lexer.instream = sys.stdin

def test_21_25():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_27_31():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_33_35():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_37_38():
    lexer = shlex()
    lexer.instream = sys.stdin

def test_40_57():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_59():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_61():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_63_64():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_66_68():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_70():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_72_74():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_76():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_78_86():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_88():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_90():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_92_95():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_97():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_99():
    lexer = shlex()
    lexer.pushback.appendleft('')

def test_101_105():
    lexer = shlex()
    lexer.pushback.append

def test_data_complicated_tests_shlex_2():
    lexer = shlex()
    lexer.push_token('test')

def test_data_complicated_tests_shlex_3(): return shlex().read_token()  

def test_024_25(): return shlex('x').read_token()  

def test_031(): return shlex(' ').read_token()  

def test_038(): return shlex('x').read_token()  

def test_054_55(): return shlex('x')._pushback_chars.append('a')  

def test_059(): return shlex('x')._pushback_chars.append('a')  

def test_061(): return shlex('x')._pushback_chars.append('a')  

def test_063_64(): return shlex('x')._pushback_chars.append('a')  

def test_068(): shlex('x').push_token('a')  

def test_073(): shlex('x').push_token('a')  

def test_078_86(): shlex('x').pop_source()  

def test_088(): shlex('x').pop_source()  

def test_092_95(): shlex('x').pop_source()  

def test_097(): shlex('x').pop_source()  

def test_101_105(): return shlex('x').get_token()  

def test_107(): return shlex('x').get_token()  

def test_109_115(): return shlex('x').get_token()  

def test_117_119(): return shlex('x').get_token()  

def test_121_122(): return shlex('x').get_token()  

def test_124_126(): return shlex('x').get_token()  

def test_128_129(): return shlex('x').get_token()  

def test_132_136(): return shlex('x').get_token()  

def test_138_142(): return shlex('x').get_token()  

def test_144_155(): return shlex('x').get_token()  

def test_157_176(): return shlex('x').get_token()  

def test_178_180(): return shlex('x').get_token()

def test_data_complicated_tests_shlex_4():
    shlex('testfile').get_token()

def test_data_complicated_tests_shlex_5():
    lexer = shlex()
    lexer.punctuation_chars = 'a'

def test_38():
    lexer = shlex()
    lexer.posix = True

def test_54():
    lexer = shlex()
    lexer.push_token('a')

def test_55():
    lexer = shlex()
    if lexer._punctuation_chars:
        pass

def test_59():
    lexer = shlex()
    lexer._pushback_chars.append('a')

def test_61():
    lexer = shlex()
    lexer.wordchars

def test_63():
    lexer = shlex()
    lexer.wordchars.maketrans({})

def test_64():
    lexer = shlex()
    lexer.wordchars.translate({})

def test_73():
    lexer = shlex()
    lexer.source = 'a'

def test_78():
    lexer = shlex()
    lexer.filestack.appendleft((None, None, 1))

def test_80():
    lexer = shlex()
    lexer.infile = 'a'

def test_81():
    lexer = shlex()
    lexer.instream = 'a'

def test_83():
    lexer = shlex()
    lexer.filestack.popleft()

def test_88():
    lexer = shlex()
    lexer.filestack.appendleft(('a', None, 1))

def test_94():
    lexer = shlex()
    lexer.token = 'a'

def test_95():
    lexer = shlex()
    lexer.pushback.appendleft('a')

def test_97():
    lexer = shlex()
    lexer.token = 'a'

def test_102():
    lexer = shlex()
    lexer.get_token()

def test_103():
    lexer = shlex()
    lexer.pushback.appendleft('a')

def test_110():
    lexer = shlex()
    lexer.filestack.appendleft(('a', None, 1))

def test_112():
    lexer = shlex()
    lexer.instream.readline()

def test_115():
    lexer = shlex()
    lexer.filestack.popleft()

def test_118():
    lexer = shlex()
    lexer.filestack.appendleft(('a', None, 1))

def test_119():
    lexer = shlex()
    lexer.filestack.popleft()

def test_121():
    lexer = sh

def test_data_complicated_tests_shlex_6():
    test_input = '1 2 3'
    lexer = shlex(test_input)
    lexer.whitespace_split = True
    return lexer.get_token() == '1'

def test_38():
    lexer = shlex('1 2 3', posix=False)
    lexer.eof = '\n'
    return lexer.eof == '\n'

def test_54():
    lexer = shlex('1 2 3', punctuation_chars='!')
    lexer._pushback_chars.append('!')
    lexer.get_token()
    return lexer.token == '!'

def test_55():
    lexer = shlex('1 2 3', punctuation_chars='!')
    lexer._pushback_chars.append('!')
    lexer.get_token()
    return lexer.state == 'a'

def test_59():
    lexer = shlex('1 2 3', whitespace_split=True)
    lexer.get_token()
    return lexer.token == '1'

def test_61():
    lexer = shlex('1 2 3', whitespace_split=True)
    lexer.get_token()
    return lexer.state == ' '

def test_63():
    lexer = shlex('1 2 3', punctuation_chars='!')
    lexer._pushback_chars.append('!')
    lexer.get_token()
    return lexer.token == '!'

def test_64():
    lexer = shlex('1 2 3', punctuation_chars='!')
    lexer._pushback_chars.append('!')
    lexer.get_token()
    return lexer.state == 'c'

def test_73():
    lexer = shlex('1 2 3', posix=True)
    lexer.get_token()
    return lexer.token == '1'

def test_78():
    lexer = shlex('1 2 3', posix=True)
    lexer.instream = StringIO('1\n2\n3')
    lexer.get_token()
    return lexer.state == ' '

def test_86():
    lexer = shlex('1 2 3', posix=True)
    lexer.instream = StringIO('1\n2\n3')
    lexer.get_token()
    return lexer.state == ' '

def test_88():
    lexer = shlex('1 2 3', posix=True)
    lexer.instream = StringIO('1\n2\n3')
    lexer.get_token()
    return lexer.state == ' '

def test_94():
    lexer = shlex('1 2 3', posix=True)
