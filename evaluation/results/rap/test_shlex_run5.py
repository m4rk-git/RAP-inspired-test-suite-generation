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
    lexer.get_token()  

def test_shlex_skip_whitespace():  
    lexer = shlex()  
    lexer.state = ' '  
    lexer.whitespace = ' \t\r\n'  
    lexer.read_token()  

def test_shlex_pushback_token():  
    lexer = shlex()  
    lexer.pushback.append('test')  
    lexer.get_token()  

def test_shlex_push_source():  
    lexer = shlex()  
    lexer.push_source(StringIO('test'))  

def test_shlex_pop_source():  
    lexer = shlex()  
    lexer.filestack.append((None, StringIO('test'), 1))  
    lexer.pop_source()  

def test_shlex_read_token():  
    lexer = shlex()  
    lexer.instream = StringIO('test')  
    lexer.read_token()  

def test_shlex_read_token_escape():  
    lexer = shlex()  
    lexer.instream = StringIO('\\t')  
    lexer.state = 'a'  
    lexer.wordchars = ' \t'  
    lexer.read_token()  

def test_shlex_read_token_quote():  
    lexer = shlex()  
    lexer.instream = StringIO('"test"')  
    lexer.state = '"'  
    lexer.read_token()  

def test_shlex_read_token_punctuation():  
    lexer = shlex()  
    lexer.instream = StringIO('test;')  
    lexer.state = 'a'  
    lexer.punctuation_chars = ';'  
    lexer.read_token()  

def test_shlex_state_none():  
    lexer = shlex()  
    lexer.state = None  
    lexer.instream = StringIO('')  
    lexer.read_token()  

def test_shlex_state_a():  
    lexer = shlex()  
    lexer.state = 'a'  
    lexer.instream = StringIO('test')  
    lexer.read_token()  

def test_shlex_state_c():  
    lexer = shlex()  
    lexer.state = 'c'  
    lexer.instream = StringIO('test;')  
    lexer.read_token()  

def test_shlex_state_q():  
    lexer = shlex()  
    lexer.state = '"'  
    lexer.instream = StringIO('test"')  
    lexer.read_token()  

def test_shlex_handle_inclusion():  
    lexer = shlex()  
    lexer.source = '"'  
    lexer.sourcehook('"test"')  
    lexer.get_token()

def test_data_complicated_tests_shlex_2():
    lexer = shlex('token1 token2 token3')
    lexer.get_token()
    lexer.get_token()
    lexer.get_token()

def test_lexer_push_token():
    lexer = shlex()
    lexer.push_token('token1')
    assert lexer.pushback == deque(['token1'])

def test_lexer_push_source():
    lexer = shlex()
    lexer.push_source(StringIO('token1 token2 token3'), 'input.txt')
    assert lexer.filestack == deque([('input.txt', lexer.instream, lexer.lineno)])

def test_lexer_pop_source():
    lexer = shlex()
    lexer.push_source(StringIO('token1 token2 token3'), 'input.txt')
    lexer.pop_source()
    assert lexer.filestack == deque()

def test_lexer_read_token():
    lexer = shlex('token1 token2 token3')
    token = lexer.read_token()
    assert token == 'token1'

def test_lexer_error_leader():
    lexer = shlex()
    lexer.infile = 'input.txt'
    lexer.lineno = 5
    leader = lexer.error_leader()
    assert leader == '"input.txt", line 5: '

def test_lexer_sourcehook():
    lexer = shlex('"path/to/file"')
    spec = lexer.sourcehook('"path/to/file"')
    assert spec == ('path/to/file', open('path/to/file', "r"))

def test_lexer_iterator():
    lexer = shlex('token1 token2 token3')
    for token in lexer:
        pass

def test_lexer_split():
    tokens = split('token1 token2 token3')
    assert tokens == ['token1', 'token2', 'token3']

def test_lexer_join():
    command = join(['command1', 'command2', 'command3'])
    assert command == 'command1 command2 command3'

def test_lexer_quote():
    escaped = quote('token1"token2')
    assert escaped == "'token1\"token2'"

def test_lexer_print_tokens():
    lexer = shlex('token1 token2 token3')
    _print_tokens(lexer)

def test_data_complicated_tests_shlex_3():
    lex = shlex()
    lex.punctuation_chars = '()'
    lex.get_token()

def test_data_complicated_tests_shlex_4():
    lexer = shlex()
    lexer.wordchars += '~-./*?='

def test_59():
    lexer = shlex()
    lexer.state = 'a'
    lexer.pushback.append('a')

def test_61():
    lexer = shlex()
    lexer.pushback.append('a')

def test_63_64():
    lexer = shlex()
    lexer._pushback_chars.append('a')
    lexer._pushback_chars.append('b')
    lexer.wordchars += '~-./*?='
    t = lexer.wordchars.maketrans(dict.fromkeys('ab'))
    lexer.wordchars = lexer.wordchars.translate(t)

def test_73():
    lexer = shlex()
    lexer.debug = 1

def test_79():
    lexer = shlex()
    lexer.instream.close()

def test_85_86():
    lexer = shlex()
    lexer.filestack.appendleft(('a', 'b', 1))

def test_88():
    lexer = shlex()
    lexer.infile = 'a'

def test_95():
    lexer = shlex()
    lexer.infile = 'a'
    lexer.instream.close()
    lexer.filestack.popleft()

def test_104():
    lexer = shlex()
    lexer.token = 'a'

def test_110_115():
    lexer = shlex()
    lexer.push_source(StringIO('a'), 'a')
    lexer.sourcehook('a')

def test_121_122():
    lexer = shlex()
    lexer.filestack.appendleft(('a', 'b', 1))
    lexer.pop_source()
    lexer.pop_source()

def test_125_126():
    lexer = shlex()
    lexer.instream.read(1)

def test_128():
    lexer = shlex()
    lexer.instream.read(1)

def test_136():
    lexer = shlex()
    lexer.instream.read(1)

def test_140():
    lexer = shlex()
    lexer.infile = 'a'

def test_142():
    lexer = shlex()
    lexer.infile = 'a'

def test_149_150():
    lexer = shlex()
    lexer.instream.read(1)

def test_152_155():
    lexer = shlex()
