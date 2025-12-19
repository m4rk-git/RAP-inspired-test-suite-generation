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
    quopri.encode(b'\x00', None)

def test_07():
    quopri.ESCAPE

def test_08():
    quopri.MAXLINESIZE

def test_09():
    quopri.HEX

def test_10():
    quopri.EMPTYSTRING

def test_12():
    quopri.a2b_qp

def test_14():
    quopri.b2a_qp

def test_19():
    quopri.needsquoting(b'\x00', False, False)

def test_26():
    quopri.quote(b'\x00')

def test_28():
    quopri.encode(b'\x00', None, True)

def test_30():
    quopri.quote(b' ')

def test_32():
    quopri.encode(b'\x00', None, False, True)

def test_34():
    quopri.quote(b'.')

def test_36():
    quopri.encode(b'\x00', None)

def test_38():
    quopri.encode(b'\x00', None)

def test_42():
    quopri.encode(b'\x00', None)

def test_51():
    quopri.encode(b'\x00', None)

def test_55():
    quopri.encode(b'\x00', None)

def test_57():
    quopri.encode(b'\x00', None)

def test_60():
    quopri.write(b'\x00')

def test_63():
    quopri.write(b'\x00')

def test_65():
    quopri.write(b'\x00')

def test_67():
    quopri.encode(b'\x00', None)

def test_69():
    quopri.encode(b'\x00', None)

def test_71():
    quopri.encode(b'\x00', None)

def test_74():
    quopri.encode(b'\x00', None)

def test_76():
    quopri.encode(b'\x00', None)

def test_81():
    quopri.encode(b'\x00', None)

def test_83():
    quopri.encode(b'\x00', None)

def test_data_temp_quopri_2():
    from quopri import encode, BytesIO
    input_data = b"Hello\tWorld"
    output = BytesIO()
    encode(input_data, output, quotetabs=True)
    assert output.getvalue().endswith(b'Hello=09World\n')

def test_data_temp_quopri_3():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)
def test_28():
    quopri.decode(b'', BytesIO(), header=False)
def test_31():
    quopri.needsquoting(b' ', quotetabs=True, header=False)
def test_53():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)
def test_57():
    quopri.decode(b'', BytesIO(), header=False)
def test_60():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)
def test_63():
    quopri.decode(b'', BytesIO(), header=False)
def test_65():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)
def test_67():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)
def test_69():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)
def test_71():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)
def test_74():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)
def test_76():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)
def test_81():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)
def test_83():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)
def test_85():
    quopri.decode(b'', BytesIO(), header=False)
def test_86():
    quopri.decode(b'', BytesIO(), header=False)
def test_89():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)
def test_90():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)
def test_93():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)
def test_94():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)
def test_96():
    quopri.encode(b'', BytesIO(), quotetabs=False, header=False)
def test_98():
    quopri.decode

def test_data_temp_quopri_4():
    quopri.encode(b'abc', b'def', True)

def test_53_55_57():
    quopri.encode(b'abc', b'def', False, True)

def test_60_63_65():
    quopri.encode(b'abc', b'def', True, True)

def test_67_69_71():
    quopri.encode(b'abc', b'def', True, True)

def test_73_81_83():
    quopri.encode(b'abc', b'def', True, True)

def test_96_98_99():
    quopri.encode(b'abc', b'def', True, True)

def test_102_108_119():
    quopri.encode(b'abc', b'def', True, True)

def test_123_127_129():
    quopri.encode(b'abc', b'def', True, True)

def test_132_144_146():
    quopri.encode(b'abc', b'def', True, True)

def test_154_160_167():
    quopri.decode(b'abc', b'def', True)

def test_172_168_180():
    quopri.unhex(b'01')

def test_182_184_189():
    quopri.main()

def test_data_temp_quopri_5():
    quopri.encode(b'', b'', False, False)

def test_31():
    quopri.needsquoting(b' ', True, True)

def test_57():
    quopri.encode(b'', b'', False, False)

def test_60_63():
    quopri.encode(b'', b'', False, False)

def test_65():
    quopri.encode(b'', b'', False, False)

def test_67_69():
    quopri.encode(b'', b'', False, False)

def test_71_74():
    quopri.encode(b'', b'', False, False)

def test_76_81():
    quopri.encode(b'', b'', False, False)

def test_83():
    quopri.encode(b'', b'', False, False)

def test_85_86():
    quopri.encode(b'', b'', False, False)

def test_89_90():
    quopri.encode(b'', b'', False, False)

def test_93_94():
    quopri.encode(b'', b'', False, False)

def test_96():
    quopri.encode(b'', b'', False, False)

def test_98_99():
    quopri.encode(b'', b'', False, False)

def test_102_108():
    quopri.encodestring(b'', False, False)

def test_119_121():
    quopri.decode(b'', b'', False)

def test_123_127():
    quopri.decode(b'', b'', False)

def test_129_130():
    quopri.decode(b'', b'', False)

def test_132_144():
    quopri.decode(b'', b'', False)

def test_146_151():
    quopri.decode(b'', b'', False)

def test_154_160():
    quopri.decode(b'', b'', False)

def test_167_168():
    quopri.decodestring(b'', False)

def test_177_180():
    quopri.unhex(b'')

def test_182():
    quopri.needsquoting(b'_', True, True)
