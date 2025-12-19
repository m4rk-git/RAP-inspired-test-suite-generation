from data.complicated_tests.cmd import *
import pytest
from io import StringIO

class TestCmd:
    def setup_method(self):
        self.cmd = Cmd()
        self.cmd.stdin = StringIO()
        self.cmd.stdout = StringIO()

    def test_parseline(self):
        assert self.cmd.parseline('help') == ('help', '', 'help')
        assert self.cmd.parseline('!ls') == ('shell', 'ls', '!ls')
        assert self.cmd.parseline('foo bar') == ('foo', 'bar', 'foo bar')
        assert self.cmd.parseline('') == (None, None, '')
        assert self.cmd.parseline('EOF') == (None, None, 'EOF')

    def test_onecmd(self):
        self.cmd.do_help = lambda arg: self.cmd.stdout.write('Help called')
        assert self.cmd.onecmd('help') == 'Help called'
        assert self.cmd.onecmd('!ls') == 'Help called'
        assert self.cmd.onecmd('foo bar') == 'Help called'
        assert self.cmd.onecmd('') == 'Help called'
        assert self.cmd.onecmd('EOF') == 'Help called'

    def test_emptyline(self):
        self.cmd.lastcmd = 'foo bar'
        assert self.cmd.emptyline() == 'foo bar'

    def test_default(self):
        self.cmd.default = lambda line: self.cmd.stdout.write('Default called')
        assert self.cmd.default('foo bar') == 'Default called'

    def test_complete(self):
        self.cmd.complete = lambda text, state: ['foo', 'bar'][state] if state < 2 else None
        assert self.cmd.complete('f', 0) == 'foo'
        assert self.cmd.complete('f', 1) == 'bar'
        assert self.cmd.complete('f', 2) is None

    def test_do_help(self):
        self.cmd.do_help = lambda arg: self.cmd.stdout.write('Help called')
        self.cmd.do_help('foo')
        assert self.cmd.stdout.getvalue() == 'Help called'

    def test_print_topics(self):
        self.cmd.print_topics('Header', ['foo', 'bar'], 10, 20)
        assert self.cmd.stdout.getvalue() == 'Header\n==\nfoo  bar\n\n'

    def test_columnize(self):
        self.cmd.columnize(['foo', 'bar', 'baz'])
        assert self.cmd.stdout.getvalue() == 'foo  bar  baz\n'