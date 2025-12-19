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
    quopri.main()

def test_07_execute_line_7():
    import sys
    sys.argv = ['quopri.py', '-t']
    quopri.main()

def test_12_execute_line_12():
    import sys
    sys.argv = ['quopri.py', '-t', 'testfile.txt']
    quopri.main()

def test_19_execute_line_19():
    quopri.encode(quopri.BytesIO(b'hello'), quopri.BytesIO(), quotetabs=True)

def test_26_execute_line_26():
    quopri.encode(quopri.BytesIO(b'hello'), quopri.BytesIO(), quotetabs=True, header=True)

def test_30_execute_line_30():
    quopri.encode(quopri.BytesIO(b'hello'), quopri.BytesIO(), quotetabs=True, header=True)

def test_34_execute_line_34():
    quopri.decode(quopri.BytesIO(quopri.b2a_qp(b'hello')), quopri.BytesIO())

def test_36_execute_line_36():
    quopri.encode(quopri.BytesIO(b'hello'), quopri.BytesIO(), quotetabs=True, header=True)

def test_38_execute_line_38():
    quopri.encode(quopri.BytesIO(b'hello'), quopri.BytesIO(), quotetabs=True, header=True)

def test_42_execute_line_42():
    quopri.encode(quopri.BytesIO(b'hello'), quopri.BytesIO(), quotetabs=True, header=True)

def test_51_execute_line_51():
    quopri.decode(quopri.BytesIO(quopri.b2a_qp(b'hello')), quopri.BytesIO(), header=True)

def test_57_execute_line_57():
    import sys
    sys.argv = ['quopri.py', '-d', 'testfile.txt']
    quopri.main()

def test_60_execute_line_60():
    quopri.encode(quopri.BytesIO(b'hello'), quopri.BytesIO(), quotetabs=True, header=True)

def test_63_execute_line_63():
    quopri.encode(quopri.BytesIO(b'hello'), quopri.BytesIO(), quotetabs=True, header=True)

def test_data_temp_quopri_2():
    import quopri
    with open('test.txt', 'wb') as f:
        f.write(b'')
    quopri.encode(f, f)

def test_26_28():
    import quopri
    quopri.encode(b'', b'', quotetabs=True)

def test_30_32():
    import quopri
    quopri.encode(b'\t', b'', header=True)

def test_36_38():
    import quopri
    quopri.encode(b'\x00', b'', quotetabs=True)

def test_57():
    import quopri
    quopri.encode(b'\t', b'')

def test_60_63():
    import quopri
    with open('test.txt', 'wb') as f:
        f.write(b'')
    def write(s, output=f, lineEnd=b'\n'):
        quopri.encode(f, f)

def test_65():
    import quopri
    quopri.encode(b'', b'')

def test_67_69():
    import quopri
    with open('test.txt', 'wb') as f:
        f.write(b'x\n')
    quopri.encode(f, f)

def test_71_74():
    import quopri
    with open('test.txt', 'wb') as f:
        f.write(b'x\n')
    quopri.encode(f, f)

def test_76_81():
    import quopri
    with open('test.txt', 'wb') as f:
        f.write(b'x\n')
    quopri.encode(f, f)

def test_83():
    import quopri
    quopri.encode(b'', b'')

def test_85_86():
    import quopri
    with open('test.txt', 'wb') as f:
        f.write(b'x\n')
    quopri.encode(f, f)

def test_89_90():
    import quopri
    with open('test.txt', 'wb') as f:
        f.write(b'x\n')
    quopri.encode(f, f)

def test_93_94():
    import quopri
    with open('test.txt', 'wb') as f:
        f.write

def test_data_temp_quopri_3():
    from io import BytesIO
    input_data = b'Hello World!'
    output = BytesIO()
    quopri.encode(input_data, output, quotetabs=False, header=False)
    output.seek(0)
    result = output.read()
    assert result == b'Hello World!'

def test_26_missing_line():
    from io import BytesIO
    input_data = b'Hello World!'
    output = BytesIO()
    quopri.encode(input_data, output, quotetabs=False, header=False)
    output.seek(0)
    result = output.read()
    assert result == b'Hello World!'

def test_30_missing_line():
    from io import BytesIO
    input_data = b'Hello World!'
    output = BytesIO()
    quopri.encode(input_data, output, quotetabs=False, header=False)
    output.seek(0)
    result = output.read()
    assert result == b'Hello World!'

def test_36_missing_line():
    from io import BytesIO
    input_data = b'Hello World!'
    output = BytesIO()
    quopri.encode(input_data, output, quotetabs=False, header=False)
    output.seek(0)
    result = output.read()
    assert result == b'Hello World!'

def test_57_missing_line():
    from io import BytesIO
    input_data = b'Hello World!'
    output = BytesIO()
    quopri.encode(input_data, output, quotetabs=False, header=False)
    output.seek(0)
    result = output.read()
    assert result == b'Hello World!'

def test_60_missing_line():
    from io import BytesIO
    input_data = b'Hello World!'
    output = BytesIO()
    quopri.encode(input_data, output, quotetabs=False, header=False)
    output.seek(0)
    result = output.read()
    assert result == b'Hello World!'

def test_65_missing_line():
    from io import BytesIO
    input_data = b'Hello World!'
    output = BytesIO()
    quopri.encode(input_data, output, quotetabs=False, header=False)
    output.seek(0)
    result = output.read()
    assert result == b'Hello World!'

def test_67_missing_line():
    from io import BytesIO
    input_data = b'Hello World!'

def test_data_temp_quopri_4():
    from io import BytesIO
    input_string = b"Test\r\n"
    output = BytesIO()
    quopri.encode(BytesIO(input_string), output, quotetabs=True)
    assert output.getvalue() == b'Test\r\n'

def test_26_28():
    from io import BytesIO
    test_char = b'\t'
    assert quopri.needsquoting(test_char, quotetabs=True, header=False) == True

def test_30_32():
    from io import BytesIO
    test_char = b'_'
    assert quopri.needsquoting(test_char, quotetabs=True, header=True) == True

def test_36_38():
    test_char = b'A'
    assert quopri.quote(test_char) == b'=41'

def test_57():
    from io import BytesIO
    input_string = b"Test\r\n"
    quopri.encode(BytesIO(input_string), BytesIO(), quotetabs=True)

def test_60_63():
    from io import BytesIO
    input_string = b"Te_st\r\n"
    output = BytesIO()
    quopri.encode(BytesIO(input_string), output, quotetabs=True)
    assert output.getvalue() == b'Te_st\r\n'

def test_65():
    from io import BytesIO
    input_string = b"Test\r\n"
    output = BytesIO()
    quopri.encode(BytesIO(input_string), output, quotetabs=True)
    assert output.getvalue() == b'Test\r\n'

def test_67_69():
    from io import BytesIO
    test_char = b'\t'
    assert quopri.needsquoting(test_char, quotetabs=True, header=False) == True

def test_71_74():
    from io import BytesIO
    test_char = b' '
    assert quopri.needsquoting(test_char, quotetabs=True, header=True) == True

def test_76_81():
    from io import BytesIO
    input_string = b'Test\r\n'
    output = BytesIO()
    quopri.encode(BytesIO(input_string), output, quotetabs=True)
    assert output.getvalue() == b'Test\r\n'

def test_83():
    from io import BytesIO
