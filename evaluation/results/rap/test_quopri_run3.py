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
    import quopri
    q = quopri.encode(quopri.BytesIO(b' '))

def test_data_temp_quopri_2():
    quopri.encode(b'', quopri.BytesIO(), quotetabs=False, header=False)

def test_26_27():
    quopri.needsquoting(b' ', quotetabs=False, header=False)

def test_30_31():
    quopri.needsquoting(b'_', quotetabs=False, header=True)

def test_36_37():
    quopri.quote(b'!')

def test_51_54():
    quopri.encode(b'', quopri.BytesIO(), quotetabs=True, header=False)

def test_60_62():
    quopri.encode(b'hello\tworld', quopri.BytesIO(), quotetabs=True, header=False)

def test_65():
    quopri.encode(b'hello world', quopri.BytesIO(), quotetabs=False, header=True)

def test_67_68():
    quopri.encode(b'\t', quopri.BytesIO(), quotetabs=False, header=False)

def test_71_74():
    quopri.encode(b'hello\nworld', quopri.BytesIO(), quotetabs=False, header=False)

def test_76_79():
    quopri.encode(b'hello world', quopri.BytesIO(), quotetabs=False, header=False)

def test_83():
    quopri.encode(b'hello world', quopri.BytesIO(), quotetabs=False, header=False)

def test_85_86():
    quopri.encode(b'hello world', quopri.BytesIO(), quotetabs=False, header=True)

def test_89_90():
    quopri.decode(b'hello world', quopri.BytesIO(), header=False)

def test_93_94():
    quopri.decode(b'hello world', quopri.BytesIO(), header=True)

def test_96():
    quopri.decode(b'hello world', quopri.BytesIO(), header=True)

def test_98_99():
    quopri.decode(b'hello world\n', quopri.BytesIO(), header=False)

def test_102_108():
    quopri.decode(b'hello world', quopri.BytesIO(), header=True)

def test_117_121():
    quopri.decode

def test_data_temp_quopri_3():
    quopri.encode(b' ', quopri.BytesIO(), True)

def test_2():
    quopri.decode(b' ', quopri.BytesIO(), True)

def test_3():
    quopri.encodestring(b' ', True)

def test_4():
    quopri.decodestring(b' ', True)

def test_5():
    quopri.encode(b' ', quopri.BytesIO(), False)

def test_6():
    quopri.decode(b' ', quopri.BytesIO(), False)

def test_7():
    quopri.encodestring(b' ')

def test_8():
    quopri.decodestring(b' ')

def test_9():
    quopri.encode(b'\t', quopri.BytesIO(), True)

def test_10():
    quopri.decode(b'\t', quopri.BytesIO(), True)

def test_11():
    quopri.encodestring(b'\t', True)

def test_12():
    quopri.decodestring(b'\t')

def test_13():
    quopri.encode(b'\t', quopri.BytesIO(), False)

def test_14():
    quopri.decode(b'\t', quopri.BytesIO(), False)

def test_15():
    quopri.encodestring(b'\t')

def test_16():
    quopri.decodestring(b'\t')

def test_17():
    quopri.encode(b'=', quopri.BytesIO(), True)

def test_18():
    quopri.decode(b'=', quopri.BytesIO(), True)

def test_19():
    quopri.encodestring(b'=')

def test_20():
    quopri.decodestring(b'=')

def test_21():
    quopri.encode(b' ', quopri.BytesIO(), True)

def test_22():
    quopri.decode(b' ', quopri.BytesIO(), True)

def test_23():
    quopri.encodestring(b' ')

def test_24():
    quopri.decodestring(b' ')

def test_25():
    quopri.encode(b' ', quopri.BytesIO(), False)

def test_26():
    quopri.decode(b' ', quopri.BytesIO(), False)

def test_27():
    qu

def test_data_temp_quopri_4(): quopri.encode(b" ", BytesIO(), False)
def test_2(): quopri.decode(b" ", BytesIO(), False)
def test_3(): quopri.encodestring(b" ")
def test_4(): quopri.decodestring(b" ")
def test_5(): quopri.main()
