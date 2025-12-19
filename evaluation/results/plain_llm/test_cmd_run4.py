from data.complicated_tests.cmd import *
import pytest
from io import StringIO

# Mocking input and output for testing
def mock_input(*args):
    return args

def mock_output():
    return StringIO()

# Test cases
def test_cmdloop():
    cmd = Cmd()
    cmd.cmdloop = mock_input('EOF')
    cmd.cmdqueue = []
    cmd.stdin = mock_input('EOF')
    cmd.stdout = mock_output()
    cmd.cmdloop()
    assert cmd.stdout.getvalue() == ''

def test_parseline():
    cmd = Cmd()
    assert cmd.parseline('help') == ('help', '', 'help')
    assert cmd.parseline('!ls') == ('shell', 'ls', '!ls')
    assert cmd.parseline('foo bar') == ('foo', 'bar', 'foo bar')
    assert cmd.parseline('') == (None, None, '')

def test_onecmd():
    cmd = Cmd()
    cmd.do_help = mock_input('EOF')
    cmd.do_shell = mock_input('EOF')
    cmd.do_foo = mock_input('EOF')
    assert cmd.onecmd('help') == 'EOF'
    assert cmd.onecmd('!ls') == 'EOF'
    assert cmd.onecmd('foo bar') == 'EOF'
    assert cmd.onecmd('') == 'EOF'

def test_emptyline():
    cmd = Cmd()
    cmd.lastcmd = 'foo bar'
    cmd.onecmd = mock_input('EOF')
    assert cmd.emptyline() == 'EOF'

def test_default():
    cmd = Cmd()
    cmd.stdout = mock_output()
    cmd.default('foo bar')
    assert cmd.stdout.getvalue() == '*** Unknown syntax: foo bar\n'

def test_complete():
    cmd = Cmd()
    cmd.completedefault = mock_input('EOF')
    cmd.complete = mock_input('EOF')
    cmd.completenames = mock_input('EOF')
    assert cmd.complete('foo', 0) == 'EOF'
    assert cmd.complete('foo', 1) == 'EOF'
    assert cmd.complete('foo', 2) == 'EOF'

def test_get_names():
    cmd = Cmd()
    assert cmd.get_names() == ['Cmd', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'cmdloop', 'completedefault', 'complete', 'completenames', 'completenames', 'completedefault', 'complete_help', 'default', 'do_help', 'emptyline', 'get_names', 'onecmd', 'postcmd', 'postloop', 'precmd', 'preloop', 'parseline', 'print_topics', 'ruler', 'identchars', 'intro', 'doc_leader', 'doc_header', 'misc_header', 'undoc_header', 'nohelp', 'use_rawinput', 'cmdqueue', 'lastcmd', 'prompt']

def test_complete_help():
    cmd = Cmd()
    cmd.complete_help = mock_input('EOF')
    assert cmd.complete_help('foo') == 'EOF'

def test_print_topics():
    cmd = Cmd()
    cmd.stdout = mock_output()
    cmd.print_topics('header', ['foo', 'bar'], 10, 20)
    assert cmd.stdout.getvalue() == 'header\n==\nfoo  bar\n\n'

def test_columnize():
    cmd = Cmd()
    cmd.stdout = mock_output()
    cmd.columnize(['foo', 'bar', 'baz'])
    assert cmd.stdout.getvalue() == 'foo  bar  baz\n'