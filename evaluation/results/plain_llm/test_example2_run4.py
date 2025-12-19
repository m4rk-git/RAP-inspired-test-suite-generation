from data.assignment_tests.example2 import *
import pytest
import sys

# Mocking sys.stdout to capture print statements
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = io.StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout

# Test cases
def test_testme_positive():
    with Capturing() as output:
        testme(0, 10, 100)
    assert output == []

def test_testme_negative():
    with Capturing() as output:
        testme(10, 0, 100)
    assert output == []

def test_testme_c_out_of_range():
    with Capturing() as output:
        testme(0, 10, 200)
    assert output == []

def test_testme_c_in_range():
    with Capturing() as output:
        testme(0, 10, 100)
    assert output == []

def test_testme_a_negative():
    with Capturing() as output:
        testme(-10, 0, 100)
    assert output == []

def test_testme_a_positive():
    with Capturing() as output:
        testme(0, 10, 100)
    assert output == []

def test_testme_a_zero():
    with Capturing() as output:
        testme(0, 10, 100)
    assert output == []

def test_testme_b_negative():
    with Capturing() as output:
        testme(0, -10, 100)
    assert output == []

def test_testme_b_positive():
    with Capturing() as output:
        testme(0, 10, 100)
    assert output == []

def test_testme_b_zero():
    with Capturing() as output:
        testme(0, 0, 100)
    assert output == []

def test_testme_c_negative():
    with Capturing() as output:
        testme(0, 10, -100)
    assert output == []

def test_testme_c_zero():
    with Capturing() as output:
        testme(0, 10, 0)
    assert output == []

def test_testme_c_positive():
    with Capturing() as output:
        testme(0, 10, 100)
    assert output == []

def test_testme_c_large():
    with Capturing() as output:
        testme(0, 10, 1000)
    assert output == []

def test_testme_c_small():
    with Capturing() as output:
        testme(0, 10, -1000)
    assert output == []

def test_testme_c_boundary():
    with Capturing() as output:
        testme(0, 10, 57)
    assert output == []

def test_testme_c_boundary2():
    with Capturing() as output:
        testme(0, 10, 284)
    assert output == []

def test_testme_c_boundary3():
    with Capturing() as output:
        testme(0, 10, 58)
    assert output == []

def test_testme_c_boundary4():
    with Capturing() as output:
        testme(0, 10, 283)
    assert output == []

def test_testme_c_boundary5():
    with Capturing() as output:
        testme(0, 10, 57.5)
    assert output == []

def test_testme_c_boundary6():
    with Capturing() as output:
        testme(0, 10, 283.5)
    assert output == []

def test_testme_c_boundary7():
    with Capturing() as output:
        testme(0, 10, 57.4)
    assert output == []

def test_testme_c_boundary8():
    with Capturing() as output:
        testme(0, 10, 283.6)
    assert output == []

def test_testme_c_boundary9():
    with Capturing() as output:
        testme(0, 10, 57.6)
    assert output == []

def test_testme_c_boundary10():
    with Capturing() as output:
        testme(0, 10, 283.4)
    assert output == []

def test_testme_c_boundary11():
    with Capturing() as output:
        testme(0, 10, 57.7)
    assert output == []

def test_testme_c_boundary12():
    with Capturing() as output:
        testme(0, 10, 283.3)
    assert output == []

def test_testme_c_boundary13():
    with Capturing() as output:
        testme(0, 10, 57.8)
    assert output == []

def test_testme_c_boundary14():
    with Capturing() as output:
        testme(0, 10, 283.2)
    assert output == []

def test_testme_c_boundary15():
    with Capturing() as output:
        testme(0, 10, 57.9)
    assert output == []

def test_testme_c_boundary16():
    with Capturing() as output:
        testme(0, 10, 283.1)
    assert output == []

def test_testme_c_boundary17():
    with Capturing() as output:
        testme(0, 10, 58.1)
    assert output == []

def test_testme_c_boundary18():
    with Capturing() as output:
        testme(0, 10, 282.9)
    assert output == []

def test_testme_c_boundary19():
    with Capturing() as output:
        testme(0, 10, 58.2)
    assert output == []

def test_testme_c_boundary20():
    with Capturing() as output:
        testme(0, 10, 282.8)
    assert output == []

def test_testme_c_boundary21():
    with Capturing() as output:
        testme(0, 10, 58.3)
    assert output == []

def test_testme_c_boundary22():
    with Capturing() as output:
        testme(0, 10, 282.7)
    assert output == []

def test_testme_c_boundary23():
    with Capturing() as output:
        testme(0, 10, 58.4)
    assert output == []

def test_testme_c_boundary24():
    with Capturing() as output:
        testme(0, 10, 282.6)
    assert output == []

def test_testme_c_boundary25():
    with Capturing() as output:
        testme(0, 10, 58.5)
    assert output == []

def test_testme_c_boundary26():
    with Capturing() as output:
        testme(0, 10, 282.5)
    assert output == []

def test_testme_c_boundary27():
    with Capturing() as output:
        testme(0, 10, 58.6)
    assert output == []

def test_testme_c_boundary28():
    with Capturing() as output:
        testme(0, 10, 282.4)
    assert output == []

def test_testme_c_boundary29():
    with Capturing() as output:
        testme(0, 10, 58.7)
    assert output == []

def test_testme_c_boundary30():
    with Capturing() as output:
        testme(0, 10, 282.3)
    assert output == []

def test_testme_c_boundary31():
    with Capturing() as output:
        testme(0, 10, 58.8)
    assert output == []

def test_testme_c_boundary32():
    with Capturing() as output:
        testme(0, 10, 282.2)
    assert output == []

def test_testme_c_boundary33():
    with Capturing() as output:
        testme(0, 10, 58.9)
    assert output == []

def test_testme_c_boundary34():
    with Capturing() as output:
        testme(0, 10, 282.1)
    assert output == []

def test_testme_c_boundary35():
    with Capturing() as output:
        testme(0, 10, 59.1)
    assert output == []

def test_testme_c_boundary36():
    with Capturing() as output:
        testme(0, 10, 282.0)
    assert output == []

def test_testme_c_boundary37():
    with Capturing() as output:
        testme(0, 10, 59.2)
    assert output == []

def test_testme_c_boundary38():
    with Capturing() as output:
        testme(0, 10, 281.9)
    assert output == []

def test_testme_c_boundary39():
    with Capturing() as output:
        testme(0, 10, 59.3)
    assert output == []

def test_testme_c_boundary40():
    with Capturing() as output:
        testme(0, 10, 281.8)
    assert output == []

def test_testme_c_boundary41():
    with Capturing() as output:
        testme(0, 10, 59.4)
    assert output == []

def test_testme_c_boundary42():
    with Capturing() as output:
        testme(0, 10, 281.7)
    assert output == []

def test_testme_c_boundary43():
    with Capturing() as output:
        testme(0, 10, 59.5)
    assert output == []

def test_testme_c_boundary44():
    with Capturing() as output:
        testme(0, 10, 281.6)
    assert output == []

def test_testme_c_boundary45():
    with Capturing() as output:
        testme(0, 10, 59.6)
    assert output == []

def test_testme_c_boundary46():
    with Capturing() as output:
        testme(0, 10, 281.5)
    assert output == []

def test_testme_c_boundary47():
    with Capturing() as output:
        testme(0, 10, 59.7)
    assert output == []

def test_testme_c_boundary48():
    with Capturing() as output:
        testme(0, 10, 281.4)
    assert output == []

def test_testme_c_boundary49():
    with Capturing() as output:
        testme(0, 10, 59.8)
    assert output == []

def test_testme_c_boundary50():
    with Capturing() as output:
        testme(0, 10, 281.3)
    assert output == []

def test_testme_c_boundary51():
    with Capturing() as output:
        testme(0, 10, 59.9)
    assert output == []

def test_testme_c_boundary52():
    with Capturing() as output:
        testme(0, 10, 281.2)
    assert output == []

def test_testme_c_boundary53():
    with Capturing() as output:
        testme(0, 10, 60.1)
    assert output == []

def test_testme_c_boundary54():
    with Capturing() as output:
        testme(0, 10, 281.1)
    assert output == []

def test_testme_c_boundary55():
    with Capturing() as output:
        testme(0, 10, 60.2)
    assert output == []

def test_testme_c_boundary56():
    with Capturing() as output:
        testme(0, 10, 281.0)
    assert output == []

def test_testme_c_boundary57():
    with Capturing() as output:
        testme(0, 10, 60.3)
    assert output == []

def test_testme_c_boundary58():
    with Capturing() as output:
        testme(0, 10, 280.9)
    assert output == []

def test_testme_c_boundary59():
    with Capturing() as output:
        testme(0, 10, 60.4)
    assert output == []

def test_testme_c_boundary60():
    with Capturing() as output:
        testme(0, 10, 280.8)
    assert output == []

def test_testme_c_boundary61():
    with Capturing() as output:
        testme(0, 10, 60.5)
    assert output == []

def test_testme_c_boundary62():
    with Capturing() as output:
        testme(0, 10, 280.7)
    assert output == []

def test_testme_c_boundary63():
    with Capturing() as output:
        testme(0, 10, 60.6)
    assert output == []

def test_testme_c_boundary64():
    with Capturing() as output:
        testme(0, 10, 280.6)
    assert output == []

def test_testme_c_boundary65():
    with Capturing() as output: