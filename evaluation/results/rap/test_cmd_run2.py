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
    cmd.__all__ = ["Cmd"]

def test_47():
    cmd = Cmd()
    cmd.PROMPT = "(Cmd) "

def test_49_50():
    cmd = Cmd()
    cmd.identchars = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                      'abcdefghijklmnopqrstuvwxyz'
                      '0123456789'
                      '_')

def test_55():
    cmd = Cmd()
    cmd.prompt = Cmd.PROMPT

def test_67_77():
    cmd = Cmd()
    cmd.cmdloop()

def test_79():
    cmd = Cmd()
    cmd.cmdqueue.append("test")

def test_90_91():
    cmd = Cmd()
    cmd.stdin = sys.stdin

def test_93_95():
    cmd = Cmd()
    cmd.stdout = sys.stdout

def test_97_99():
    cmd = Cmd()
    cmd.completekey = 'tab'

def test_101():
    cmd = Cmd()
    cmd.completekey = 'tab'

def test_108_115():
    cmd = Cmd()
    cmd.completedefault()

def test_117():
    cmd = Cmd()
    cmd.complete('cmd', 0)

def test_119():
    cmd = Cmd()
    cmd.complete('cmd', 1)

def test_121_133():
    cmd = Cmd()
    cmd.completenames()

def test_135_139():
    cmd = Cmd()
    cmd.get_names()

def test_141_145():
    cmd = Cmd()
    cmd.default("test")

def test_147_151():
    cmd = Cmd()
    cmd.emptyline()

def test_153_158():
    cmd = Cmd()
    cmd.onecmd("test")

def test_161():
    cmd = Cmd()
    cmd.onecmd("")

def test_166():
    cmd = Cmd()
    cmd.precmd("test")

def test_168():
    cmd = Cmd()
    cmd.postcmd(False, "test")

def test_170():
    cmd = Cmd()
    cmd.postcmd(None, "test")

def test_172():
    cmd = Cmd()
    cmd.postcmd(True, "test")

def test_174():
    cmd = Cmd()
    cmd
