import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.textwrap as textwrap
from data.complicated_tests.textwrap import *

import re

def test_data_complicated_tests_textwrap_1():
    return textwrap.TextWrapper().fix_sentence_endings(None)
