import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/temp')
import pytest
import data.temp.quopri as quopri
from data.temp.quopri import *

from binascii import a2b_qp
from binascii import b2a_qp
from io import BytesIO
from io import BytesIO
import sys
import getopt

def test_data_temp_quopri_1():
    quopri.encode(b' \t', BytesIO(), quotetabs=True) 

def test_02():
    quopri.encode(b' \t', BytesIO(), quotetabs=True, header=True) 

def test_03():
    quopri.encode(b' \t', BytesIO(), quotetabs=False) 

def test_04():
    quopri.encode(b' \t', BytesIO(), quotetabs=False, header=True) 

def test_05():
    quopri.decode(BytesIO(b'= \t'), BytesIO()) 

def test_06():
    quopri.decode(BytesIO(b'= \t'), BytesIO(), header=True) 

def test_07():
    quopri.decode(BytesIO(b'= \t'), BytesIO(), header=False) 

def test_08():
    quopri.decode(BytesIO(b'= \t'), BytesIO(), header=False) 

def test_09():
    quopri.encodestring(b' \t', quotetabs=True) 

def test_10():
    quopri.encodestring(b' \t', quotetabs=True, header=True) 

def test_11():
    quopri.encodestring(b' \t', quotetabs=False) 

def test_12():
    quopri.encodestring(b' \t', quotetabs=False, header=True) 

def test_13():
    quopri.decodestring(b'= \t') 

def test_14():
    quopri.decodestring(b'= \t', header=True) 

def test_15():
    quopri.decodestring(b'= \t', header=False) 

def test_16():
    quopri.decodestring(b'= \t', header=False) 

def test_17():
    quopri.needsquoting(b' ', True, False) 

def test_18():
    quopri.needsquoting(b' \t', True, False) 

def test_19():
    quopri.needsquoting(b' ', True, True) 

def test_20():
    quopri.needsquoting(b' \t', True, True) 

def test_21():
    quopri.needsquoting(b' ', False, False) 

def test_22():
    quopri.ne

def test_data_temp_quopri_2():
    quopri.encode(b' ', BytesIO(), quotetabs=True)

def test_30():
    quopri.encode(b' ', BytesIO(), quotetabs=False, header=True)

def test_36():
    quopri.quote(b' ')

def test_53():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)

def test_57():
    quopri.a2b_qp(b' ')

def test_60():
    quopri.encode(b' ', BytesIO(), quotetabs=False, header=False)

def test_65():
    quopri.decode(b' ', BytesIO(), header=False)

def test_67():
    quopri.encode(b'x\n', BytesIO(), quotetabs=False, header=False)

def test_71():
    quopri.encode(b'\n', BytesIO(), quotetabs=False, header=False)

def test_76():
    quopri.encode(b'a\x0b', BytesIO(), quotetabs=False, header=False)

def test_83():
    quopri.encode(b'\x0b', BytesIO(), quotetabs=False, header=False)

def test_85():
    quopri.encode(b'x\n', BytesIO(), quotetabs=False, header=False)

def test_86():
    quopri.encode(b'\n', BytesIO(), quotetabs=False, header=False)

def test_89():
    quopri.decode(b'\\=', BytesIO(), header=False)

def test_90():
    quopri.decode(b'=\\', BytesIO(), header=False)

def test_93():
    quopri.decode(b'\\=\n', BytesIO(), header=False)

def test_94():
    quopri.decode(b'=\\n', BytesIO(), header=False)

def test_96():
    quopri.decode(b'\\=\n', BytesIO(), header=False)

def test_98():
    quopri.decode(b'x\n', BytesIO(), header=False)

def test_99():
    quopri.decode(b'\n', BytesIO(), header=False)

def test_104():
    quopri.decode(b'\\=', BytesIO(), header=False)

def test_108():
    quopri.decode(b'=\\', BytesIO(), header=False)

def test_123():
    qu
