import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.cmd as cmd
from data.complicated_tests.cmd import *

import sys
import readline
import readline
import readline
from inspect import cleandoc

def test_data_complicated_tests_cmd_1():
    cmd = Cmd()
    cmd.cmdloop()

def test_data_complicated_tests_cmd_2():
    cmd = Cmd()
    cmd.cmdloop()

def test_1():
    cmd = Cmd()
    cmd.completedefault()

def test_2():
    cmd = Cmd()
    cmd.complete_help()

def test_3():
    cmd = Cmd()
    cmd.complete('a', 0)

def test_4():
    cmd = Cmd()
    cmd.do_help('a')

def test_5():
    cmd = Cmd()
    cmd.onecmd('a')

def test_6():
    cmd = Cmd()
    cmd.parse('a')

def test_7():
    cmd = Cmd()
    cmd.postcmd('a', 'b')

def test_8():
    cmd = Cmd()
    cmd.preloop()

def test_9():
    cmd = Cmd()
    cmd.print_topics('a', ['a'], 15, 80)

def test_10():
    cmd = Cmd()
    cmd.precmd('a')

def test_11():
    cmd = Cmd()
    cmd.prompt('a')

def test_12():
    cmd = Cmd()
    cmd.stdout.write('a')

def test_13():
    cmd = Cmd()
    cmd.stdin.readline()

def test_14():
    cmd = Cmd()
    cmd.stdin.read()

def test_15():
    cmd = Cmd()
    cmd.stdoud.write('a')

def test_16():
    cmd = Cmd()
    cmd.do_default('a')

def test_17():
    cmd = Cmd()
    cmd.completedefault('a', 'b', 'c')

def test_18():
    cmd = Cmd()
    cmd.columnize(['a'])

def test_19():
    cmd = Cmd()
    cmd.get_names()

def test_20():
    cmd = Cmd()
    cmd.completenames('a', 'b')

def test_21():
    cmd = Cmd()
    cmd.complete('a', 1)

def test_data_complicated_tests_cmd_3():
    cmd = Cmd()
    cmd.prompt = ''

def test_95():
    cmd = Cmd()
    cmd.stdio = sys.stdin

def test_115():
    cmd = Cmd()
    cmd.lastcmd = 'EOF'

def test_117():
    cmd = Cmd()
    cmd.stdout = sys.stdout

def test_119():
    cmd = Cmd()
    cmd.stdin = sys.stdin

def test_121_122():
    cmd = Cmd()
    cmd.stdin = sys.stdin
    import readline
    readline.parse_and_bind('tab: complete')

def test_124_133():
    cmd = Cmd()
    cmd.cmdloop()

def test_135_139():
    cmd = Cmd()
    cmd.cmdloop('intro')

def test_141_145():
    cmd = Cmd()
    cmd.cmdqueue.append('line')

def test_147_151():
    cmd = Cmd()
    cmd.postcmd(True, 'line')

def test_153_158():
    cmd = Cmd()
    cmd.preloop()

def test_181():
    cmd = Cmd()
    cmd.prompt = ''

def test_190():
    cmd = Cmd()
    cmd.cmdqueue.append('line')

def test_192():
    cmd = Cmd()
    cmd.prompt = ''

def test_194_195():
    cmd = Cmd()
    cmd.lastcmd = 'EOF'

def test_197():
    cmd = Cmd()
    cmd.prompt = ''

def test_215():
    cmd = Cmd()
    cmd.prompt = ''

def test_217():
    cmd = Cmd()
    cmd.prompt = ''

def test_220():
    cmd = Cmd()
    cmd.prompt = ''

def test_222():
    cmd = Cmd()
    cmd.prompt = ''

def test_227():
    cmd = Cmd()
    cmd.prompt = ''

def test_236_237():
    cmd = Cmd()
    cmd.prompt = ''

def test_275_277():
    cmd = Cmd()
    cmd.prompt = ''

def test_279_282():
    cmd = Cmd()
    cmd.prompt = ''

def test_298():
    cmd = Cmd()
    cmd.prompt = ''

def test_300():
    cmd = Cmd

def test_data_complicated_tests_cmd_4():
    cmd.cmdqueue.append('EOF')
    cmd.cmdloop()

def test_95():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_115():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_117():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_119():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_121_122():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_124_133():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_135_139():
    cmd.cmdqueue.append('EOF')
    cmd.cmdloop()

def test_141_145():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_147_151():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_153_158():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_181():
    cmd.cmdqueue.append('EOF')
    cmd.cmdloop()

def test_190():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_192():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_194_195():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_197():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_215():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_217():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_220():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_222():
    cmd.stdin = open('test.txt', 'r')
    cmd.cmdloop()

def test_227():
    cmd.stdin = open('test.txt', 'r')
    cmd

def test_data_complicated_tests_cmd_5():
    class MockCmd(Cmd):
        def __init__(self):
            super().__init__()
            self.prompt = "Mock> "
            self.identchars = "abc"
            self.ruler = "*"
            self.lastcmd = ""
            self.intro = "Mock introduction"
            self.doc_leader = ""
            self.doc_header = "Documented commands:"
            self.misc_header = "Miscellaneous help topics:"
            self.undoc_header = "Undocumented commands:"
            self.nohelp = "No help for %s"
            self.use_rawinput = 0
            self.stdin = sys.stdin
            self.stdout = sys.stdout
            self.cmdqueue = []
            self.completekey = 'tab'
    mock_cmd = MockCmd()
    mock_cmd.cmdloop()
