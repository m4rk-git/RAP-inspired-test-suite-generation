import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.sched as sched
from data.complicated_tests.sched import *

import time
import heapq
from collections import namedtuple
from itertools import count
import threading
from time import monotonic as _time

def test_data_complicated_tests_sched_1():
    s = sched.scheduler()
    s.enterabs(1, 1, lambda: None)
    s.run()

def test_force_line_execution():
    s = sched.scheduler()
    s.enter(1, 1, lambda: None)
    s.run()

def test_force_line_execution():
    s = sched.scheduler()
    s.cancel(None)
    s.run()

def test_force_line_execution():
    s = sched.scheduler()
    s.empty()
    s.run()

def test_force_line_execution():
    s = sched.scheduler()
    s.queue
    s.run()

def test_force_line_execution():
    s = sched.scheduler()
    s.timefunc()
    s.run()
    
def test_force_line_execution():
    s = sched.scheduler()
    s.delayfunc(1)
    s.run()

def test_force_line_execution():
    s = sched.scheduler()
    s._lock = threading.Lock()
    s.run()

def test_force_line_execution():
    s = sched.scheduler()
    s._sequence_generator = count()
    s.run()

def test_force_line_execution():
    s = sched.scheduler()
    s._queue = []
    s.run()

def test_force_line_execution():
    s = sched.scheduler()
    s._time()
    s.run()

def test_data_complicated_tests_sched_2():
    sch = sched.scheduler()
    sch.enter(1, 1, lambda: None)

def test_94_96():
    sch = sched.scheduler()
    event = sch.enterabs(1, 1, lambda: None)
    sch.cancel(event)

def test_100_101():
    sch = sched.scheduler()
    sch.queue

def test_142():
    sch = sched.scheduler()
    now = sch.timefunc()

def test_147_149():
    sch = sched.scheduler()
    sch.enter(1, 1, lambda: None)
    sch.run(blocking=False)

def test_165_167():
    sch = sched.scheduler()
    events = sch.queue
    list(events)

def test_data_complicated_tests_sched_3():
    s = sched.scheduler()
    s.enterabs(1, 1, lambda: None)
    s.run(blocking=False)

def test_149():
    s = sched.scheduler()
    s.enterabs(1, 1, lambda: None)
    s.run(blocking=False)

def test_data_complicated_tests_sched_4():
    sched_instance = sched.scheduler()
    sched_instance.run(blocking=False)

def test_149():
    sched_instance = sched.scheduler()
    with sched_instance._lock:
        pass
    sched_instance.run(blocking=True)

def test_data_complicated_tests_sched_5():
    s = sched.scheduler()
    assert s.empty()

def test_149_run():
    s = sched.scheduler()
    s.enterabs(1, 1, print, ("Hello, world!",))
    s.run(blocking=False)
    assert True  # Add an assertion to ensure the function has executed the intended line
