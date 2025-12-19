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
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(time.time() + 1, 1, lambda: None, ())
    s._lock.release() # Target line 26-31

def test_33():
    s = sched.scheduler(time.time, time.sleep)
    print(s.queue) # Target line 33

def test_35_36():
    Event = sched.Event(1, 1, 1, lambda: None, (), {})
    print(Event.time) # Target line 35-36
    print(Event.priority) # Target line 36

def test_38():
    s = sched.scheduler(time.time, time.sleep)
    print(s.timefunc()) # Target line 38

def test_40():
    s = sched.scheduler(time.time, time.sleep)
    print(s.delayfunc) # Target line 40

def test_42():
    s = sched.scheduler(time.time, time.sleep)
    print(s.enterabs) # Target line 42

def test_44():
    s = sched.scheduler(time.time, time.sleep)
    print(s.enter) # Target line 44

def test_46():
    s = sched.scheduler(time.time, time.sleep)
    print(s.cancel) # Target line 46

def test_49():
    s = sched.scheduler(time.time, time.sleep)
    print(s.empty) # Target line 49

def test_51():
    s = sched.scheduler(time.time, time.sleep)
    print(s.run) # Target line 51

def test_53():
    s = sched.scheduler(time.time, time.sleep)
    print(s.queue) # Target line 53

def test_56_60():
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(time.time() + 1, 1, lambda: None, ())
    s._lock.release() # Target line 56-60

def test_62():
    s = sched.scheduler(time.time, time.sleep)
    print(s.timefunc) # Target line 62

def test_69_70():
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(time.time() + 1, 1, lambda: None, ())
    s._lock.release() # Target line 69-70

def test_data_complicated_tests_sched_2():
    scheduler_instance = sched.scheduler()
    scheduler_instance.enter(1, 1, lambda: None)

def test_94_96():
    scheduler_instance = sched.scheduler()
    event = Event(1, 1, 1, lambda: None, (), {})
    scheduler_instance._queue.append(event)
    scheduler_instance.cancel(event)

def test_100_101():
    scheduler_instance = sched.scheduler()
    assert scheduler_instance.empty()

def test_129_138():
    scheduler_instance = sched.scheduler()
    with scheduler_instance._lock:
        assert scheduler_instance._queue == []

def test_140_142():
    scheduler_instance = sched.scheduler()
    event = Event(1, 1, 1, lambda: None, (), {})
    scheduler_instance._queue.append(event)
    with scheduler_instance._lock:
        scheduler_instance._queue.pop(0)

def test_144_149():
    scheduler_instance = sched.scheduler()
    now = scheduler_instance.timefunc()
    event = Event(now, 1, 1, lambda: None, (), {})
    scheduler_instance._queue.append(event)
    with scheduler_instance._lock:
        assert scheduler_instance._queue[0][0] == now

def test_151_152():
    scheduler_instance = sched.scheduler()
    scheduler_instance.run(blocking=False)

def test_data_complicated_tests_sched_3():
    scheduler_instance = sched.scheduler()
    event =_EVENT(1, 0, 0, lambda: None, (), {})
    scheduler_instance._queue.append(event)
    scheduler_instance.cancel(event)

def test_138():
    scheduler_instance = sched.scheduler()
    scheduler_instance._queue = [sched.Event(2, 0, 0, lambda: None, (), {})]
    scheduler_instance.run()

def test_140_142():
    scheduler_instance = sched.scheduler()
    scheduler_instance._queue = [sched.Event(1, 0, 0, lambda: None, (), {})]
    scheduler_instance.run()

def test_144_149():
    scheduler_instance = sched.scheduler()
    scheduler_instance._queue = [sched.Event(1, 0, 0, lambda: None, (), {})]
    with scheduler_instance._lock:
        scheduler_instance.run()

def test_151_152():
    scheduler_instance = sched.scheduler()
    scheduler_instance._queue = [sched.Event(1, 0, 0, lambda: None, (), {})]
    scheduler_instance.run()

def test_data_complicated_tests_sched_4():
    scheduler_inst = sched.scheduler()
    event = Event(1, 1, 1, lambda: None, (), {})
    scheduler_inst._queue.append(event)
    scheduler_inst.cancel(event)

def test_142():
    scheduler_inst = sched.scheduler()
    time_mock = Mock(return_value=0)
    scheduler_inst.timefunc = time_mock
    result = scheduler_inst.run(blocking=False)
    assert result == 1

def test_147_149():
    scheduler_inst = sched.scheduler()
    time_mock = Mock(side_effect=[0, 1])
    scheduler_inst.timefunc = time_mock
    scheduler_inst.delayfunc = Mock()
    scheduler_inst.run(blocking=True)
    assert scheduler_inst.delayfunc.call_args_list == [call(1), call(0)]

def test_data_complicated_tests_sched_5():
    sched_instance = sched.scheduler()
    event = sched.Event(0, 0, lambda: None)
    sched_instance._queue.append(event)
    sched_instance.cancel(event)

    events = list(sched_instance.queue)
    assert len(events) == 1, "Expected 1 event in the queue"

    event = heapq.heappop(sched_instance._queue)
    assert event.time == 0 and event.priority == 0 and event.action is None, "Event properties are incorrect"

    time = sched_instance.timefunc()
    delayfunc = sched_instance.delayfunc
    with patch.object(sched_instance, 'timefunc', return_value=time + 0.1):
        with patch.object(sched_instance, 'delayfunc', side_effect=lambda x: sleep(x)):
            sched_instance.run(False)

def test_data_complicated_tests_sched_6():
    s = sched.scheduler(time.monotonic, time.sleep)
    event_id = s.enterabs(10, 1, print, argument=('Hello, world!',))
    s.cancel(event_id)
    s.enterabs(10, 1, print, argument=('Hello, world!',))

def test_142():
    s = sched.scheduler(time.monotonic, time.sleep)
    s.enterabs(10, 1, print, argument=('Hello, world!',))
    s.run()

def test_147_149():
    s = sched.scheduler(time.monotonic, time.sleep)
    s.enterabs(10, 1, print, argument=('Hello, world!',))
    while not s.empty():
        s.run(blocking=False)
        time.sleep(1)
