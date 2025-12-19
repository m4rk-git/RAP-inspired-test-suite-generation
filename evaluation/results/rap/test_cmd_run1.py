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
    cmd.prompt

def test_47():
    cmd = Cmd()
    cmd.__all__

def test_49():
    cmd = Cmd()
    cmd.prompt = Cmd.PROMPT

def test_50():
    cmd = Cmd()
    cmd.identchars = Cmd.IDENTCHARS

def test_55():
    cmd = Cmd()
    cmd.cmdloop()

def test_67():
    cmd = Cmd()
    cmd.help_doc_header

def test_77():
    cmd = Cmd()
    cmd.onecmd('help')

def test_79():
    cmd = Cmd()
    cmd.preloop()

def test_90():
    cmd = Cmd()
    cmd.stdin = sys.stdin

def test_91():
    cmd = Cmd()
    cmd.stdin = sys.stdin

def test_93():
    cmd = Cmd()
    cmd.stdin = sys.stdin

def test_95():
    cmd = Cmd()
    cmd.stdin = sys.stdin

def test_97():
    cmd = Cmd()
    cmd.stdin = sys.stdin

def test_99():
    cmd = Cmd()
    cmd.stdin = sys.stdin

def test_101():
    cmd = Cmd()
    cmd.cmdloop()

def test_108():
    cmd = Cmd()
    cmd.cmdloop()

def test_115():
    cmd = Cmd()
    cmd.cmdloop()

def test_117():
    cmd = Cmd()
    cmd.cmdloop()

def test_119():
    cmd = Cmd()
    cmd.cmdloop()

def test_121():
    cmd = Cmd()
    cmd.cmdloop()

def test_123():
    cmd = Cmd()
    cmd.cmdloop()

def test_125():
    cmd = Cmd()
    cmd.cmdloop()

def test_133():
    cmd = Cmd()
    cmd.cmdloop()

def test_135():
    cmd = Cmd()
    cmd.cmdloop()

def test_139():
    cmd = Cmd()
    cmd.cmdloop()

def test_141():
    cmd = Cmd()
    cmd.cmdloop()

def test_145():
    cmd = Cmd()
    cmd.cmdloop()

def test_147():
    cmd = Cmd()
    cmd.cmdloop()

def test_151():
    cmd = Cmd()
    cmd.cmdloop()

def test_153():
    cmd = Cmd()

def test_data_complicated_tests_cmd_2():
    cmd.cmdloop()

def test_data_complicated_tests_cmd_3():
    cmd = Cmd()
    cmd.cmdloop()
    assert cmd.cmdqueue == []

def test_95():
    cmd = Cmd()
    cmd.cmdqueue.append('test')
    cmd.cmdloop()
    assert cmd.cmdqueue == []

def test_115():
    cmd = Cmd()
    cmd.cmdqueue.append('test')
    cmd.cmdloop()
    assert cmd.cmdqueue == []

def test_117():
    cmd = Cmd()
    cmd.cmdqueue.append('test')
    cmd.cmdloop()
    assert cmd.cmdqueue == []

def test_119():
    cmd = Cmd()
    cmd.cmdqueue.append('test')
    cmd.cmdloop()
    assert cmd.cmdqueue == []

def test_121():
    cmd = Cmd()
    cmd.cmdqueue.append('test')
    cmd.cmdloop()
    assert cmd.cmdqueue == []

def test_122():
    cmd = Cmd()
    cmd.cmdqueue.append('test')
    cmd.cmdloop()
    assert cmd.cmdqueue == []

def test_124():
    cmd = Cmd()
    cmd.cmdqueue.append('test')
    cmd.cmdloop()
    assert cmd.cmdqueue == []

def test_125():
    cmd = Cmd()
    cmd.cmdqueue.append('test')
    cmd.cmdloop()
    assert cmd.cmdqueue == []

def test_126():
    cmd = Cmd()
    cmd.cmdqueue.append('test')
    cmd.cmdloop()
    assert cmd.cmdqueue == []

def test_127():
    cmd = Cmd()
    cmd.cmdqueue.append('test')
    cmd.cmdloop()
    assert cmd.cmdqueue == []

def test_128():
    cmd = Cmd()
    cmd.cmdqueue.append('test')
    cmd.cmdloop()
    assert cmd.cmdqueue == []

def test_130():
    cmd = Cmd()
    cmd.cmdqueue.append('test')
    cmd.cmdloop()
    assert cmd.cmdqueue == []

def test_132():
    cmd = Cmd()
    cmd.cmdqueue.append('test')
    cmd.cmdloop()
    assert cmd.cmdqueue == []

def test_135():
    cmd = Cmd()
    cmd.cmdqueue.append('test')
    cmd.cmdloop()
    assert cmd.cmdqueue == []

def test_137():
    cmd = Cmd()
    cmd.cmdqueue.append('test')
    cmd.cmdloop()
    assert cmd.cmdqueue == []

def test_139():
    cmd = Cmd()

def test_data_complicated_tests_cmd_4():
    cmd.cmdqueue = ['EOF']
    cmd.cmdloop()

def test_95():
    cmd.stdin = open('input.txt', 'w')
    cmd.stdin.close()
    cmd.cmdloop()

def test_115():
    cmd.use_rawinput = True
    cmd.completekey = 'tab'
    cmd.cmdloop()

def test_117():
    cmd.use_rawinput = True
    cmd.completekey = 'tab'
    cmd.cmdloop()

def test_119():
    cmd.use_rawinput = True
    cmd.completekey = 'tab'
    cmd.cmdloop()

def test_121():
    cmd.use_rawinput = True
    cmd.completekey = 'tab'
    cmd.cmdloop()

def test_122():
    cmd.use_rawinput = True
    cmd.completekey = 'tab'
    cmd.cmdloop()

def test_124():
    cmd.use_rawinput = True
    cmd.completekey = 'tab'
    cmd.cmdloop()

def test_133():
    cmd.use_rawinput = True
    cmd.completekey = 'tab'
    cmd.cmdloop()

def test_135():
    cmd.use_rawinput = True
    cmd.completekey = 'tab'
    cmd.cmdloop()

def test_139():
    cmd.use_rawinput = True
    cmd.completekey = 'tab'
    cmd.cmdloop()

def test_141():
    cmd.use_rawinput = True
    cmd.completekey = 'tab'
    cmd.cmdloop()

def test_145():
    cmd.use_rawinput = True
    cmd.completekey = 'tab'
    cmd.cmdloop()

def test_153():
    cmd.use_rawinput = True
    cmd.completekey = 'tab'
    cmd.cmdloop()

def test_158():
    cmd.use_rawinput = True
    cmd.completekey = 'tab'
    cmd.cmdloop()

def test_166():
    cmd.cmdqueue = ['']
    cmd.cmdloop()

def test_170():
    cmd.cmdqueue = ['']
    cmd.cmdloop()

def test_181():
    cmd.use_rawinput = True
    cmd.completekey = 'tab'
    cmd.cmdqueue = ['']
    cmd.cmdloop()

def test_190():
    cmd.cmdqueue = ['?']
    cmd.cmdloop()

def test_192():
    cmd.cmdqueue

def test_data_complicated_tests_cmd_5():
    cmd = Cmd()
    cmd.cmdloop()

def test_95():
    cmd = Cmd()
    cmd.cmdqueue.append('line')
    cmd.cmdloop()

def test_115():
    cmd = Cmd()
    cmd.lastcmd = 'lastcmd'
    cmd.onecmd('EOF')

def test_117():
    cmd = Cmd()
    cmd.complete('line', 0)

def test_119():
    cmd = Cmd()
    cmd.complete('line', 1)

def test_121_122():
    cmd = Cmd()
    cmd.lastcmd = 'lastcmd'
    cmd.onecmd('')

def test_124_133():
    cmd = Cmd()
    cmd.cmdloop()
    cmd.onecmd('line')

def test_135_139():
    cmd = Cmd()
    cmd.cmdloop()
    cmd.onecmd('!')

def test_141_145():
    cmd = Cmd()
    cmd.cmdloop()
    cmd.onecmd('?')

def test_147_158():
    cmd = Cmd()
    cmd.cmdloop()
    cmd.onecmd('line')

def test_153_158():
    cmd = Cmd()
    cmd.cmdloop()
    cmd.onecmd('!')

def test_166():
    cmd = Cmd()
    cmd.cmdloop()
    cmd.onecmd('!')

def test_170():
    cmd = Cmd()
    cmd.cmdloop()
    cmd.onecmd('!')

def test_181():
    cmd = Cmd()
    cmd.cmdloop()
    cmd.onecmd('!')

def test_190():
    cmd = Cmd()
    cmd.cmdqueue.append('line')
    cmd.cmdqueue.append('line')
    cmd.cmdloop()

def test_192():
    cmd = Cmd()
    cmd.cmdqueue.append('line')
    cmd.cmdqueue.append('line')
    cmd.cmdloop()

def test_194_195():
    cmd = Cmd()
    cmd.cmdqueue.append('line')
    cmd.cmdloop()
    cmd.onecmd('!')

def test_197():
    cmd = Cmd()
    cmd.cmdloop()
    cmd.onecmd('!')

def test_215():
    cmd = Cmd()
    cmd.cmdloop()
    cmd.onecmd('line')

def test_217():
    cmd = Cmd()
    cmd.cmdloop()
    cmd.one
