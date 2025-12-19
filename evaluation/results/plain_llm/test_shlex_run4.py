from data.complicated_tests.shlex import *
import pytest
from io import StringIO

def test_shlex_init():
    lexer = shlex()
    assert lexer.instream == sys.stdin
    assert lexer.infile is None
    assert lexer.posix is False
    assert lexer.commenters == '#'
    assert lexer.wordchars == 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
    assert lexer.whitespace == ' \t\r\n'
    assert lexer.whitespace_split is False
    assert lexer.quotes == '\'"'
    assert lexer.escape == '\\'
    assert lexer.escapedquotes == '"'
    assert lexer.state == ' '
    assert lexer.pushback == deque()
    assert lexer.lineno == 1
    assert lexer.debug == 0
    assert lexer.token == ''
    assert lexer.filestack == deque()
    assert lexer.source is None
    assert lexer._punctuation_chars == ''

def test_shlex_push_token():
    lexer = shlex()
    lexer.push_token('test')
    assert lexer.pushback == deque(['test'])

def test_shlex_push_source():
    lexer = shlex()
    lexer.push_source(StringIO('test'))
    assert lexer.filestack == deque()
    assert lexer.infile is None
    assert lexer.instream.getvalue() == 'test'
    assert lexer.lineno == 1

def test_shlex_pop_source():
    lexer = shlex()
    lexer.push_source(StringIO('test'))
    lexer.pop_source()
    assert lexer.filestack == deque()
    assert lexer.infile is None
    assert lexer.instream == sys.stdin
    assert lexer.lineno == 1

def test_shlex_get_token():
    lexer = shlex(StringIO('test'))
    assert lexer.get_token() == 'test'

def test_shlex_read_token():
    lexer = shlex(StringIO('test'))
    assert lexer.read_token() == 'test'

def test_shlex_sourcehook():
    lexer = shlex()
    lexer.sourcehook('test')
    assert lexer.sourcehook('test') == ('test', open('test', 'r'))

def test_shlex_error_leader():
    lexer = shlex()
    assert lexer.error_leader() == "\"\", line 1: "

def test_shlex_iter():
    lexer = shlex(StringIO('test'))
    assert list(lexer) == ['test']

def test_split():
    assert split('test') == ['test']
    assert split('test test') == ['test', 'test']
    assert split('test#test') == ['test']
    assert split('test#test', comments=True) == ['test', 'test']

def test_join():
    assert join(['test']) == 'test'
    assert join(['test', 'test']) == 'test test'

def test_quote():
    assert quote('test') == 'test'
    assert quote('test test') == "'test test'"
    assert quote('test"test') == "'test\"test'"
    assert quote('test\'test') == "'test\\'test'"

def test_print_tokens():
    lexer = shlex(StringIO('test'))
    _print_tokens(lexer)
    assert lexer.get_token() == 'test'

if __name__ == '__main__':
    pytest.main()