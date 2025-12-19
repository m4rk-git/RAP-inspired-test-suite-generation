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
    sch = sched.scheduler()
    sch.enter(0.5, 1, print, "Hello")
    return next(iter(sch.queue)).time - sch.timefunc() > 0.0

def test_2_cancel_event():
    sch = sched.scheduler()
    event = sch.enter(1, 1, print, "Hello")
    sch.cancel(event)
    return sch.empty()

def test_3_empty_queue():
    sch = sched.scheduler()
    return sch.empty()

def test_4_run_with_blocking_true():
    sch = sched.scheduler()
    sch.enter(0.1, 1, print, "Hello")
    sch.run(blocking=True)
    return next(iter(sch.queue)).time - sch.timefunc() > 0.1

def test_5_enterabs_with_kwargs():
    sch = sched.scheduler()
    sch.enterabs(1, 1, print, kwargs={"sep": "!"})
    return next(iter(sch.queue)).kwargs == {"sep": "!"}

def test_6_enter_with_delay():
    sch = sched.scheduler()
    sch.enter(0.1, 1, print, "Hello")
    sch.run(blocking=True)
    return next(iter(sch.queue)).time - sch.timefunc() > 0.1

def test_7_enter_with_empty_args():
    sch = sched.scheduler()
    sch.enter(0.1, 1, print)
    return next(iter(sch.queue)).argument == ()

def test_8_run_with_delay():
    sch = sched.scheduler()
    sch.enter(0.5, 1, print, "Hello")
    sch.run(blocking=True)
    return next(iter(sch.queue)).time - sch.timefunc() > 0.5

def test_9_enter_with_kwargs():
    sch = sched.scheduler()
    sch.enter(1, 1, print, kwargs={"sep": "!"})
    return next(iter(sch.queue)).kwargs == {"sep": "!"}

def test_10_enterabs_with_delay():
    sch = sched.scheduler()
    sch.enterabs(1, 1, print, "Hello")
    sch.run(blocking=True)
    return next(iter(sch.queue)).time - sch.timefunc() > 1

def test_11_run_with_empty_queue():
    sch = sched.scheduler()
    return sch.run(blocking=False) is None

def test_12_enter_with_priority():
    sch = sched.scheduler()

def test_data_complicated_tests_sched_2():
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(time.time() + 1, 1, print, ("Hello, world! ",))
    s.run(blocking=False)
