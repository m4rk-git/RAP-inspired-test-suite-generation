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
    cmd.cmdqueue.append("EOF")

def test_95():
    cmd.stdin = open('test_input.txt', 'r')
    cmd.cmdloop()

def test_115():
    cmd.completekey = 'tab'
    cmd.stdin = open('test_input.txt', 'r')
    cmd.cmdloop()

def test_117():
    cmd.completekey = 'tab'
    cmd.stdin = open('test_input.txt', 'r')
    cmd.cmdloop()

def test_119():
    cmd.completekey = 'tab'
    cmd.stdin = open('test_input.txt', 'r')
    cmd.cmdloop()

def test_121():
    cmd.completekey = 'tab'
    cmd.stdin = open('test_input.txt', 'r')
    cmd.cmdloop()

def test_122():
    cmd.completekey = 'tab'
    cmd.stdin = open('test_input.txt', 'r')
    cmd.cmdloop()

def test_124():
    cmd.completekey = 'tab'
    cmd.stdin = open('test_input.txt', 'r')
    cmd.cmdloop()

def test_125():
    cmd.completekey = 'tab'
    cmd.stdin = open('test_input.txt', 'r')
    cmd.cmdloop()

def test_126():
    cmd.completekey = 'tab'
    cmd.stdin = open('test_input.txt', 'r')
    cmd.cmdloop()

def test_127():
    cmd.completekey = 'tab'
    cmd.stdin = open('test_input.txt', 'r')
    cmd.cmdloop()

def test_128():
    cmd.completekey = 'tab'
    cmd.stdin = open('test_input.txt', 'r')
    cmd.cmdloop()

def test_129():
    cmd.completekey = 'tab'
    cmd.stdin = open('test_input.txt', 'r')
    cmd.cmdloop()

def test_131():
    cmd.completekey = 'tab'
    cmd.stdin = open('test_input.txt', 'r')
    cmd.cmdloop()

def test_133():
    cmd.completekey = 'tab'
    cmd.stdin = open('test_input.txt', 'r')
    cmd.cmdloop()

def test_135():
    cmd.completekey = 'tab'
    cmd.stdin = open('test_input.txt', 'r')
    cmd.cmdloop()

def test_139():
    cmd.completekey = 'tab'

def test_data_complicated_tests_cmd_3():
    cmd.cmdqueue.append('EOF') 
    cmd.cmdloop()
    
def test_95():
    cmd.cmdqueue.append('help') 
    cmd.cmdloop()
    
def test_115():
    cmd.prompt = ''
    cmd.cmdloop()
    
def test_117():
    cmd.prompt = ''
    cmd.cmdqueue.append('EOF') 
    cmd.cmdloop()
    
def test_119():
    cmd.prompt = ''
    cmd.cmdqueue.append('help') 
    cmd.cmdloop()
    
def test_121():
    cmd.completekey = ''
    cmd.cmdloop()
    
def test_122():
    cmd.completekey = ''
    cmd.cmdqueue.append('EOF') 
    cmd.cmdloop()
    
def test_124():
    cmd.completekey = ''
    cmd.cmdqueue.append('help') 
    cmd.cmdloop()
    
def test_125():
    cmd.completekey = ''
    cmd.cmdqueue.append('EOF') 
    cmd.cmdloop()
    
def test_126():
    cmd.completekey = ''
    cmd.cmdqueue.append('help') 
    cmd.cmdloop()
    
def test_127():
    cmd.completekey = ''
    cmd.cmdqueue.append('EOF') 
    cmd.cmdloop()
    
def test_128():
    cmd.completekey = ''
    cmd.cmdqueue.append('help') 
    cmd.cmdloop()
    
def test_129():
    cmd.completekey = ''
    cmd.cmdqueue.append('EOF') 
    cmd.cmdloop()
    
def test_130():
    cmd.completekey = ''
    cmd.cmdqueue.append('help') 
    cmd.cmdloop()
    
def test_132():
    cmd.completekey = ''
    cmd.cmdqueue.append('EOF') 
    cmd.cmdloop()
    
def test_133():
    cmd.completekey = ''
    cmd.cmdqueue.append('help') 
    cmd.cmdloop()
    
def test_135():
    cmd.prompt = ''
    cmd.cmdqueue.append('EOF') 
    cmd.cmdloop()
    
def test_136():
    cmd.prompt = ''
    cmd.cmdqueue.append('help') 
    cmd.cmdloop()
    
def test_137():
    cmd.prompt = ''
    cmd.cmdqueue.append('EOF') 
    cmd.cmdloop()
    
def test_138():
    cmd.prompt = ''
    cmd.cmdqueue.append('help')

def test_data_complicated_tests_cmd_4():
    cmd = Cmd()
    cmd.cmdqueue.append('EOF')

def test_95():
    cmd = Cmd()
    cmd.stdin = open('/dev/null', 'r')

def test_115():
    class MyCmd(Cmd):
        def do_foo(self):
            pass
    cmd = MyCmd()
    cmd.onecmd('foo bar')

def test_117():
    class MyCmd(Cmd):
        def complete_foo(self, text, line, begidx, endidx):
            pass
    cmd = MyCmd()
    cmd.complete('foo', 0)

def test_119():
    class MyCmd(Cmd):
        def complete_foo(self, text, line, begidx, endidx):
            pass
    cmd = MyCmd()
    cmd.complete('foo', 0)

def test_121_122():
    class MyCmd(Cmd):
        def do_shell(self, arg):
            pass
    cmd = MyCmd()
    cmd.onecmd('!')

def test_124_133():
    cmd = Cmd()
    cmd.cmdloop('intro')

def test_135_139():
    cmd = Cmd()
    cmd.cmdloop()

def test_141_145():
    cmd = Cmd()
    cmd.cmdloop('intro')

def test_147_151():
    class MyCmd(Cmd):
        def do_foo(self):
            pass
    cmd = MyCmd()
    cmd.onecmd('foo')

def test_153_158():
    class MyCmd(Cmd):
        def do_foo(self):
            pass
    cmd = MyCmd()
    cmd.onecmd('foo')

def test_166():
    cmd = Cmd()
    cmd.emptyline()

def test_170():
    cmd = Cmd()
    cmd.postcmd(False, 'foo')

def test_181():
    cmd = Cmd()
    cmd.postloop()

def test_188_195():
    cmd = Cmd()
    cmd.precmd('foo')

def test_197_201():
    class MyCmd(Cmd):
        def do_foo(self):
            pass
    cmd = MyCmd()
    cmd.onecmd('foo')

def test_213_222():
    class MyCmd(Cmd):
        def do_foo(self):
            pass
