import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.copy as copy
from data.complicated_tests.copy import *

import types
import weakref
from copyreg import dispatch_table

def test_data_complicated_tests_copy_1():
    import copy
    a = None
    copy.copy(a)
