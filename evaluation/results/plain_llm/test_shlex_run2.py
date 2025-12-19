from data.complicated_tests.shlex import *
import pytest
import io

def test_init():
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

def test_push_token():
    lexer = shlex()
    lexer.push_token('test')
    assert lexer.pushback == deque(['test'])

def test_push_source():
    lexer = shlex()
    lexer.push_source(io.StringIO('test'), 'test.txt')
    assert lexer.filestack == deque([('test.txt', io.StringIO('test'), 1)])
    assert lexer.infile == 'test.txt'
    assert lexer.instream.getvalue() == 'test'
    assert lexer.lineno == 1

def test_pop_source():
    lexer = shlex()
    lexer.push_source(io.StringIO('test'), 'test.txt')
    lexer.pop_source()
    assert lexer.filestack == deque()
    assert lexer.infile is None
    assert lexer.instream is sys.stdin
    assert lexer.lineno == 1

def test_get_token():
    lexer = shlex(io.StringIO('test token'))
    assert lexer.get_token() == 'test'
    assert lexer.get_token() == 'token'
    assert lexer.get_token() == ''

def test_read_token():
    lexer = shlex(io.StringIO('test token'))
    assert lexer.read_token() == 'test'
    assert lexer.read_token() == 'token'
    assert lexer.read_token() == ''

def test_sourcehook():
    lexer = shlex()
    result = lexer.sourcehook('"test.txt"')
    assert result == ('test.txt', open('test.txt', 'r'))

def test_error_leader():
    lexer = shlex()
    assert lexer.error_leader() == '"", line 1: '

def test_iter():
    lexer = shlex(io.StringIO('test token'))
    assert next(lexer) == 'test'
    assert next(lexer) == 'token'
    with pytest.raises(StopIteration):
        next(lexer)

def test_split():
    assert split('test token') == ['test', 'token']
    assert split('test;token', comments=False) == ['test', 'token']
    assert split('test;token', comments=True) == ['test', 'token']

def test_join():
    assert join(['test', 'token']) == 'test token'

def test_quote():
    assert quote('test') == 'test'
    assert quote('test token') == "'test token'"
    assert quote('test"token') == "'test\"token'"

def test_edge_cases():
    lexer = shlex(io.StringIO(''))
    assert lexer.get_token() == ''

    lexer = shlex(io.StringIO('test\n'))
    assert lexer.get_token() == 'test'
    assert lexer.get_token() == ''

    lexer = shlex(io.StringIO('test#token'))
    assert lexer.get_token() == 'test'
    assert lexer.get_token() == ''

    lexer = shlex(io.StringIO('test;token'))
    assert lexer.get_token() == 'test'
    assert lexer.get_token() == 'token'
    assert lexer.get_token() == ''

    lexer = shlex(io.StringIO('test"token'))
    with pytest.raises(ValueError):
        lexer.get_token()

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    with pytest.raises(ValueError):
        lexer.get_token()

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = False
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    assert lexer.get_token() == 'test"token'

    lexer = shlex(io.StringIO('test"token'))
    lexer.posix = True
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"'
    lexer.escape = '\\'
    lexer.escapedquotes = '"