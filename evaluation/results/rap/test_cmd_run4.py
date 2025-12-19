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

def test_47():
    import sys
    sys.path.append('path_to_module')

def test_49_50():
    cmd = Cmd()
    cmd.prompt
    cmd.identchars

def test_55():
    cmd = Cmd()
    cmd.cmdloop()

def test_67_77():
    cmd = Cmd()
    cmd.onecmd('test_command')

def test_79():
    cmd = Cmd()
    cmd.preloop()

def test_90_91():
    cmd = Cmd()
    cmd.stdin = sys.stdin

def test_93_95():
    cmd = Cmd()
    cmd.stdout = sys.stdout

def test_97_99():
    cmd = Cmd()
    cmd.cmdqueue = []

def test_101():
    cmd = Cmd()
    cmd.use_rawinput

def test_108_115():
    cmd = Cmd()
    cmd.precmd('test_command')

def test_117():
    cmd = Cmd()
    cmd.postcmd(None, 'test_command')

def test_119():
    cmd = Cmd()
    cmd.onecmd('EOF')

def test_121_133():
    cmd = Cmd()
    cmd.parseline('test_command')

def test_135_139():
    cmd = Cmd()
    cmd.default('test_command')

def test_141_145():
    cmd = Cmd()
    cmd.do_help('topic')

def test_147_151():
    cmd = Cmd()
    cmd.do_shell('test_command')

def test_153_158():
    cmd = Cmd()
    cmd.complete('test_command', 0)

def test_161():
    cmd = Cmd()
    cmd.postloop()

def test_166():
    cmd = Cmd()
    cmd.emptyline()

def test_168():
    cmd = Cmd()
    cmd.postcmd(None, '')

def test_170():
    cmd = Cmd()
    cmd.postcmd(True, 'test_command')

def test_172():
    cmd = Cmd()
    cmd.postcmd(False, 'test_command')

def test_174():
    cmd = Cmd()
    cmd.postcmd(None, 'test_command')

def test_176():
    cmd = Cmd()
    cmd.postcmd(None, 'test_command')

def test_data_complicated_tests_cmd_2():
    cmd = Cmd()
    cmd.cmdloop()

def test_data_complicated_tests_cmd_3():
    cmd = Cmd()
    cmd.cmdqueue.append('EOF')

def test_data_complicated_tests_cmd_4():
    cmd.cmdqueue.append('EOF')
    cmd.cmdloop()

def test_ensure_execution_line_95():
    cmd.prompt = 'custom_prompt'
    cmd.cmdloop()

def test_ensure_execution_line_115():
    cmd.cmdqueue.append('known_command')
    cmd.cmdloop()

def test_ensure_execution_line_117():
    cmd.prompt = 'custom_prompt'
    cmd.cmdqueue.append('known_command')
    cmd.cmdloop()

def test_ensure_execution_line_119():
    cmd.prompt = 'custom_prompt'
    cmd.cmdqueue.append('known_command')
    cmd.cmdloop()

def test_ensure_execution_line_121_122():
    cmd.prompt = 'custom_prompt'
    cmd.cmdqueue.append('known_command')
    cmd.cmdloop()

def test_ensure_execution_line_124_133():
    cmd.prompt = 'custom_prompt'
    cmd.cmdqueue.append('known_command')
    cmd.cmdloop()

def test_ensure_execution_line_135_139():
    cmd.prompt = 'custom_prompt'
    cmd.cmdqueue.append('known_command')
    cmd.cmdloop()

def test_ensure_execution_line_141_145():
    cmd.prompt = 'custom_prompt'
    cmd.cmdqueue.append('known_command')
    cmd.cmdloop()

def test_ensure_execution_line_153_158():
    cmd.prompt = 'custom_prompt'
    cmd.cmdqueue.append('known_command')
    cmd.cmdloop()

def test_ensure_execution_line_190():
    cmd.cmdqueue.append('help_command')
    cmd.cmdloop()

def test_ensure_execution_line_192():
    cmd.cmdqueue.append('help_command')
    cmd.cmdloop()

def test_ensure_execution_line_194_195():
    cmd.prompt = 'custom_prompt'
    cmd.cmdqueue.append('help_command')
    cmd.cmdloop()

def test_ensure_execution_line_197():
    cmd.prompt = 'custom_prompt'
    cmd.cmdqueue.append('help_command')
    cmd.cmdloop()

def test_ensure_execution_line_215():
    cmd.cmdqueue.append('known_command')
    cmd.cmdloop()

def test_ensure_execution_line_217():
    cmd.cmdqueue.append('known_command')
    cmd.cmdloop()

def test_ensure_execution_line_222():
    cmd.cmdqueue.append('known_command')
    cmd.cmd

def test_data_complicated_tests_cmd_5():
    cmd = Cmd()
    cmd.cmdloop()

def test_95():
    cmd = Cmd()
    cmd.cmdloop('intro')

def test_115():
    cmd = Cmd()
    cmd.use_rawinput = False
    cmd.cmdloop()

def test_117():
    cmd = Cmd()
    cmd.use_rawinput = False
    cmd.cmdloop('intro')

def test_119():
    cmd = Cmd()
    cmd.use_rawinput = False
    cmd.cmdloop('intro')

def test_121():
    cmd = Cmd()
    cmd.use_rawinput = True
    cmd.completekey = None
    cmd.cmdloop()

def test_122():
    cmd = Cmd()
    cmd.use_rawinput = True
    cmd.completekey = None
    cmd.cmdloop('intro')

def test_124():
    cmd = Cmd()
    cmd.use_rawinput = True
    cmd.completekey = None
    cmd.cmdloop()

def test_125():
    cmd = Cmd()
    cmd.use_rawinput = True
    cmd.completekey = None
    cmd.cmdloop()
    input('')

def test_126():
    cmd = Cmd()
    cmd.use_rawinput = True
    cmd.completekey = None
    cmd.cmdloop('intro')
    input('')

def test_127():
    cmd = Cmd()
    cmd.use_rawinput = True
    cmd.completekey = None
    cmd.cmdloop()

def test_128():
    cmd = Cmd()
    cmd.use_rawinput = True
    cmd.completekey = None
    cmd.cmdloop('intro')
    input('')

def test_133():
    cmd = Cmd()
    cmd.use_rawinput = True
    cmd.completekey = None
    cmd.cmdloop()
    input('')

def test_135():
    cmd = Cmd()
    cmd.use_rawinput = True
    cmd.completekey = None
    cmd.cmdloop('intro')
    input('')

def test_137():
    cmd = Cmd()
    cmd.use_rawinput = True
    cmd.completekey = None
    cmd.cmdloop()

def test_139():
    cmd = Cmd()
    cmd.use_rawinput = True
    cmd.completekey = None
    cmd.cmdloop('intro')
    input('')

def test_141():
    cmd = Cmd()
    cmd.use_raw
