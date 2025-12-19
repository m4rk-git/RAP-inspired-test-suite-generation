import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.bleach_sanitizer as bleach_sanitizer
from data.complicated_tests.bleach_sanitizer import *

from itertools import chain
import re
import warnings
from xml.sax.saxutils import unescape
from bleach import html5lib_shim
from bleach import parse_shim

def test_data_complicated_tests_bleach_sanitizer_1():
    Cleaner(tags={'a': 'b'}, attributes={'a': ['b']}, protocols={'http'}, strip=False, strip_comments=True, filters=[None], css_sanitizer=None).clean('')

def test_2():
    Cleaner().filter(None, 'a', 'b', 1)

def test_3():
    Cleaner().sanitize_uri_value('a', 1)

def test_5():
    Cleaner().attribute_filter_factory('a')

def test_7():
    Cleaner().sanitize_characters({'type': 'Characters', 'data': 'a'})

def test_8():
    Cleaner().serialize({'type': 'Characters', 'data': 'a'})

def test_12():
    Cleaner().tags = 1

def test_31():
    Cleaner().attributes = 1

def test_38():
    Cleaner().protocols = 1

def test_41():
    Cleaner().strip = 1

def test_46():
    Cleaner().strip_comments = 1

def test_50():
    Cleaner().css_sanitizer = 1

def test_53():
    Cleaner().__init__()

def test_54():
    Cleaner().__init__(tags='a')

def test_57():
    Cleaner().__init__(attributes='a')

def test_86():
    Cleaner().__init__(filters=[1])

def test_124():
    Cleaner().__init__(tags='a', attributes='b')

def test_130():
    Cleaner().__init__(tags='a', attributes='b', protocols='c')

def test_132():
    Cleaner().__init__(tags='a', attributes='b', protocols='c', strip='d')

def test_138():
    Cleaner().__init__(tags='a', attributes='b', protocols='c', strip='d', strip_comments='e')

def test_139():
    Cleaner().__init__(tags='a', attributes='b', protocols='c', strip='d', strip_comments='e', filters=[1])

def test_152():
    Cleaner().__init__(tags='a', attributes='b', protocols='c', strip='d', strip_comments='e', filters=[1], css_sanitizer='f')

def test_155():
    Cleaner().__init__(tags='a', attributes='b', protocols='c', strip='d', strip_comments='e', filters=[1], css_sanitizer='f').parser = 1

def test_data_complicated_tests_bleach_sanitizer_2():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_166():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_182():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_186():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_191():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_192():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_203():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_204():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_206():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_217():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_218():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_220():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_222():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_224():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_226():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_228():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_229():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_231():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_234():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_236():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_238():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_240():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_242():
    cleaner

def test_data_complicated_tests_bleach_sanitizer_3():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_166():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_182():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_186():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_204():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_218():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_223():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_224():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_226():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_228():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_229():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_231():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_232():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_234():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_236():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_238():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_242():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_244():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_245():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_247():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_249():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_326():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("test")

def test_329():
    cleaner

def test_data_complicated_tests_bleach_sanitizer_4():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_166():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_182():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_186():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_204():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_218():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_223_to_226():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_228_to_229():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_231_to_234():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_236():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_238():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_242():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_244_to_245():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_247():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_249():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_326():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_329():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div>test</div>")

def test_339_to_341():
    cleaner = bleach_sanitizer.C

def test_data_complicated_tests_bleach_sanitizer_5():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='https://example.com'>Click</a>")

def test_166():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<a href='mailto:example@example.com'>Email</a>")

def test_182():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("")

def test_186():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<script>alert('XSS')</script>")

def test_204():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<img src='x' onerror='alert(1)'>")

def test_218():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<svg><a xlink:href='http://example.com'>Link</a></svg>")

def test_223():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div style='color: red;'>Text</div>")

def test_224():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div style='background: url(http://example.com)'>Text</div>")

def test_225():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div style='background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...'>Text</div>")

def test_226():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div style='background: url(#local)>Text</div>")

def test_228():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div style='color: red'></div>")

def test_229():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div style='background: url(http://example.com) no-repeat'></div>")

def test_231():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div style='background: url(http://example.com) repeat'></div>")

def test_232():
    cleaner = bleach_sanitizer.Cleaner()
    cleaner.clean("<div style='background: url(http://example.com) no-repeat scroll'></div>")

def test_233():
    cleaner = bleach_sanitizer.Clean
