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
    e = sched.scheduler(_time, time.sleep)
    
def test_33():
    print(sched.Event.time.__doc__)
    
def test_35():
    e = sched.Event('1', 1, 1, lambda: None, (), {})
    
def test_38():
    print(sched.Event.priority.__doc__)
    
def test_40():
    print(sched.Event.sequence.__doc__)
    
def test_42():
    print(sched.Event.action.__doc__)
    
def test_44():
    print(sched.Event.argument.__doc__)
    
def test_46():
    print(sched.Event.kwargs.__doc__)
    
def test_49():
    e = sched.scheduler(time.time, time.sleep)
    
def test_51():
    e = sched.scheduler(_time, time.sleep)
    
def test_53():
    e = sched.scheduler()
    
def test_56():
    e = sched.scheduler(_time, time.sleep)
    
def test_58():
    e = sched.scheduler(_time, time.sleep)
    
def test_60():
    e = sched.scheduler(_time, time.sleep)
    
def test_62():
    e = sched.scheduler(_time, time.sleep)
    
def test_69():
    e = sched.scheduler(_time, time.sleep)
    e.enterabs(1, 1, lambda: None, ())
    
def test_70():
    e = sched.scheduler(_time, time.sleep)
    e.enterabs(1, 1, lambda: None, (), {})
    
def test_72():
    e = sched.scheduler(_time, time.sleep)
    e.enterabs("1", 1, lambda: None, ())
    
def test_73():
    e = sched.scheduler(_time, time.sleep)
    e.enterabs(1, 1, lambda: None, (), {})
    
def test_75():
    e = sched.scheduler(_time, time.sleep)
    e.enterabs(1, 1, lambda: None, ())
    
def test_76():
    e = sched.scheduler(_time, time.sleep)
    e.enterabs(1, 1, lambda: None, (), {})
    
def test_78():
    e = sched.scheduler(_time, time.sleep)
    e.enter(1, 1, lambda: None, ())
    
def test_84():
    e = sched.scheduler(_time, time.sleep)
    e.enter

def test_data_complicated_tests_sched_2():
    sched_obj = sched.scheduler()
    event = sched.Event(0, 0, lambda: None)
    sched_obj._queue.remove(event)
    heapq.heapify(sched_obj._queue)


def test_100_101():
    sched_obj = sched.scheduler()
    assert sched_obj.empty()


def test_129_138():
    sched_obj = sched.scheduler()
    lock = sched_obj._lock
    q = sched_obj._queue
    delayfunc = sched_obj.delayfunc
    timefunc = sched_obj.timefunc
    pop = heapq.heappop
    lock.acquire()
    assert not q
    lock.release()


def test_140_142():
    sched_obj = sched.scheduler()
    q = sched_obj._queue
    with sched_obj._lock:
        heapq.heappush(q, sched.Event(0, 0, lambda: None))
        (time, priority, sequence, action, argument, kwargs) = q[0]
        now = timefunc()
        assert time >= now


def test_144_149():
    sched_obj = sched.scheduler()
    lock = sched_obj._lock
    q = sched_obj._queue
    delayfunc = sched_obj.delayfunc
    timefunc = sched_obj.timefunc
    pop = heapq.heappop
    with lock:
        heapq.heappush(q, sched.Event(0, 0, lambda: None))
        (time, priority, sequence, action, argument, kwargs) = q[0]
        now = timefunc()
        if time > now:
            delay = True
        else:
            delay = False
            pop(q)
    assert delay == False


def test_151_152():
    sched_obj = sched.scheduler()
    sched_obj.run(blocking=False)


def test_165_167():
    sched_obj = sched.scheduler()
    events = []
    with sched_obj._lock:
        heapq.heappush(sched_obj._queue, sched.Event(0, 0, lambda: None))
        events += sched_obj._queue[:]
    assert len(events) > 0

def test_data_complicated_tests_sched_3():
    scheduler_instance = sched.scheduler()
    event = scheduler_instance.enterabs(10, 1, print, ("hello",))
    scheduler_instance.cancel(event)

def test_138():
    scheduler_instance = sched.scheduler()
    scheduler_instance.run()

def test_140_142():
    scheduler_instance = sched.scheduler()
    scheduler_instance.enterabs(10, 1, print, ("hello",))
    scheduler_instance.run(False)

def test_144_149():
    scheduler_instance = sched.scheduler()
    scheduler_instance.enterabs(10, 1, print, ("hello",))
    scheduler_instance.run()

def test_151_152():
    scheduler_instance = sched.scheduler()
    scheduler_instance.enterabs(10, 1, print, ("hello",))
    scheduler_instance.run(False)

def test_165_167():
    scheduler_instance = sched.scheduler()
    scheduler_instance.queue
