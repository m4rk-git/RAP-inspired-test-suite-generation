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
        assert self.cmd.parseline('EOF') == (None, None, 'EOF')
        assert self.cmd.parseline('') == (None, None, '')

    def test_onecmd(self):
        self.cmd.do_help = lambda arg: self.cmd.stdout.write('Help!')
        assert self.cmd.onecmd('help') == 'Help!'
        assert self.cmd.onecmd('!ls') == 'Help!'
        assert self.cmd.onecmd('EOF') == None
        assert self.cmd.onecmd('') == None

    def test_emptyline(self):
        self.cmd.lastcmd = 'help'
        assert self.cmd.emptyline() == 'Help!'
        self.cmd.lastcmd = ''
        assert self.cmd.emptyline() == None

    def test_default(self):
        self.cmd.stdout.write = lambda x: None
        assert self.cmd.default('unknown') == None

    def test_complete(self):
        self.cmd.complete = lambda text, state: ['cmd1', 'cmd2'][state] if state < 2 else None
        assert self.cmd.complete('c', 0) == 'cmd1'
        assert self.cmd.complete('c', 1) == 'cmd2'
        assert self.cmd.complete('c', 2) == None

    def test_completenames(self):
        self.cmd.get_names = lambda: ['do_cmd1', 'do_cmd2', 'help_topic1']
        assert self.cmd.completenames('cmd') == ['cmd1', 'cmd2']
        assert self.cmd.completenames('topic') == ['topic1']

    def test_complete_help(self):
        self.cmd.completenames = lambda text, *args: ['cmd1', 'topic1']
        assert self.cmd.complete_help('cmd') == ['cmd1']
        assert self.cmd.complete_help('topic') == ['topic1']

    def test_do_help(self):
        self.cmd.help_topic1 = lambda: self.cmd.stdout.write('Topic1 Help!')
        self.cmd.do_help('topic1')
        assert self.cmd.stdout.getvalue() == 'Topic1 Help!\n'

    def test_print_topics(self):
        self.cmd.stdout.write = lambda x: None
        self.cmd.print_topics('Header', ['cmd1', 'cmd2'], 10, 20)
        assert self.cmd.stdout.getvalue() == 'Header\n========\ncmd1  cmd2\n\n'

    def test_columnize(self):
        self.cmd.stdout.write = lambda x: None
        self.cmd.columnize(['cmd1', 'cmd2', 'cmd3', 'cmd4'])
        assert self.cmd.stdout.getvalue() == 'cmd1  cmd2\ncmd3  cmd4\n'