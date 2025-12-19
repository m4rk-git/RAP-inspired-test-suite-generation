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
    quopri.encode(b'\x00', quopri.BytesIO(), False)

def test_7():
    quopri.needsquoting(b' ', False, False)

def test_8():
    quopri.MAXLINESIZE

def test_9():
    quopri.HEX

def test_10():
    quopri.EMPTYSTRING

def test_12():
    quopri.a2b_qp = None

def test_13():
    quopri.b2a_qp = None

def test_19():
    quopri.quote(b'\x00')

def test_26():
    quopri.encode(quopri.BytesIO(b'\x00'), quopri.BytesIO(), False)

def test_28():
    quopri.decode(quopri.BytesIO(b'\x00'), quopri.BytesIO())

def test_30():
    quopri.encode(quopri.BytesIO(b' '), quopri.BytesIO(), False)

def test_32():
    quopri.encode(quopri.BytesIO(b'a'), quopri.BytesIO(), False)

def test_34():
    quopri.encode(quopri.BytesIO(b'\t'), quopri.BytesIO(), False)

def test_36():
    quopri.encode(quopri.BytesIO(b' '), quopri.BytesIO(), False)

def test_38():
    quopri.encode(quopri.BytesIO(b'\n'), quopri.BytesIO(), False)

def test_42():
    quopri.encode(quopri.BytesIO(b'.'), quopri.BytesIO(), False)

def test_51():
    quopri.encode(quopri.BytesIO(b'\x00'), quopri.BytesIO(), False)

def test_55():
    quopri.encode(quopri.BytesIO(b'\x00'), quopri.BytesIO(), False)

def test_57():
    quopri.encode(quopri.BytesIO(b'\x00'), quopri.BytesIO(), False)

def test_60():
    quopri.encode(quopri.BytesIO(b'\x00'), quopri.BytesIO(), False)

def test_63():
    quopri.encode(quopri.BytesIO(b'\x00'), quopri.BytesIO(), False)

def test_65():
    qu

def test_data_temp_quopri_2():
    with open('test_file.txt', 'wb') as f:
        f.write(b'teste')
    with open('output.txt', 'wb') as f:
        quopri.encode(f, f, False)

def test_30_32():
    quopri.encode(b'teste', b'output.txt', False)

def test_51_55():
    with open('test_file.txt', 'wb') as f:
        f.write(b'teste')
    with open('output.txt', 'wb') as f:
        quopri.decode(f, f, False)

def test_57():
    quopri.encode(b'teste', b'output.txt', False)

def test_60_63():
    with open('test_file.txt', 'wb') as f:
        f.write(b'teste')
    with open('output.txt', 'wb') as f:
        quopri.encode(f, f, False)

def test_65():
    quopri.encode(b'teste', b'output.txt', False)

def test_67_69():
    with open('test_file.txt', 'wb') as f:
        f.write(b'teste')
    with open('output.txt', 'wb') as f:
        quopri.encode(f, f, False)

def test_71_74():
    with open('test_file.txt', 'wb') as f:
        f.write(b'teste')
    with open('output.txt', 'wb') as f:
        quopri.encode(f, f, False)

def test_76_81():
    with open('test_file.txt', 'wb') as f:
        f.write(b'teste')
    with open('output.txt', 'wb') as f:
        quopri.encode(f, f, False)

def test_83():
    quopri.encode(b'teste', b'output.txt', False)

def test_85_86():
    with open('test_file.txt', 'wb') as f:
        f.write(b'teste')
    with open('output.txt', 'wb') as f:
        quopri.encode(f, f, False)

def test_89_90():
    with open('test_file.txt', 'wb') as f:
        f.write(b'teste')
    with open('output.txt', 'wb') as f:
        quop
