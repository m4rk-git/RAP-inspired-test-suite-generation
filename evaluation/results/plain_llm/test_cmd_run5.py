from data.complicated_tests.cmd import *
import pytest
from io import StringIO

class TestCmd:
    def setup_method(self):
        self.cmd = Cmd()
        self.cmd.stdin = StringIO()
        self.cmd.stdout = StringIO()

    def test_parseline(self):
        assert self.cmd.parseline('') == (None, None, '')
        assert self.cmd.parseline('EOF') == (None, None, 'EOF')
        assert self.cmd.parseline('!') == (None, None, '!')
        assert self.cmd.parseline('!ls') == ('shell', 'ls', '!ls')
        assert self.cmd.parseline('?') == ('help', '', '?')
        assert self.cmd.parseline('help') == ('help', '', 'help')
        assert self.cmd.parseline('help foo') == ('help', 'foo', 'help foo')

    def test_onecmd(self):
        self.cmd.do_help = lambda arg: self.cmd.stdout.write('Help!')
        assert self.cmd.onecmd('help') == 'Help!'
        assert self.cmd.onecmd('!ls') == 'shell ls'
        assert self.cmd.onecmd('EOF') == ''

    def test_emptyline(self):
        self.cmd.lastcmd = 'foo'
        assert self.cmd.emptyline() == 'foo'

    def test_default(self):
        self.cmd.default('foo') == '*** Unknown syntax: foo\n'

    def test_completenames(self):
        self.cmd.do_foo = lambda arg: None
        assert self.cmd.completenames('foo') == ['foo']
        assert self.cmd.completenames('bar') == []

    def test_complete(self):
        self.cmd.do_foo = lambda arg: None
        self.cmd.complete_foo = lambda text, line, begidx, endidx: ['foo1', 'foo2']
        assert self.cmd.complete('foo', 0) == 'foo1'
        assert self.cmd.complete('foo', 1) == 'foo2'
        assert self.cmd.complete('foo', 2) is None

    def test_do_help(self):
        self.cmd.do_foo = lambda arg: None
        self.cmd.help_foo = lambda: self.cmd.stdout.write('Foo help')
        assert self.cmd.onecmd('help foo') == 'Foo help'

    def test_print_topics(self):
        self.cmd.stdout = StringIO()
        self.cmd.print_topics('Header', ['foo', 'bar', 'baz'], 10, 80)
        assert self.cmd.stdout.getvalue() == 'Header\n========\nfoo  bar  baz\n\n'

    def test_columnize(self):
        self.cmd.stdout = StringIO()
        self.cmd.columnize(['foo', 'bar', 'baz', 'qux'])
        assert self.cmd.stdout.getvalue() == 'foo  bar  baz  qux\n'