from data.complicated_tests.sched import *
import pytest
from collections import namedtuple
from itertools import count
import threading
from time import monotonic as _time

# Mocking time and sleep functions for testing
class MockTime:
    def __init__(self):
        self.current_time = 0

    def time(self):
        return self.current_time

    def sleep(self, delay):
        self.current_time += delay

class MockAction:
    def __init__(self):
        self.called = False

    def __call__(self, *args, **kwargs):
        self.called = True

def test_enterabs():
    mock_time = MockTime()
    mock_action = MockAction()
    sched = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    event = sched.enterabs(10, 1, mock_action, (1, 2), {'key': 'value'})
    assert event.time == 10
    assert event.priority == 1
    assert event.sequence == 0
    assert event.action == mock_action
    assert event.argument == (1, 2)
    assert event.kwargs == {'key': 'value'}
    assert not mock_action.called

def test_enter():
    mock_time = MockTime()
    mock_action = MockAction()
    sched = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    event = sched.enter(5, 1, mock_action, (1, 2), {'key': 'value'})
    assert event.time == 5
    assert event.priority == 1
    assert event.sequence == 0
    assert event.action == mock_action
    assert event.argument == (1, 2)
    assert event.kwargs == {'key': 'value'}
    assert not mock_action.called

def test_cancel():
    mock_time = MockTime()
    mock_action = MockAction()
    sched = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    event = sched.enterabs(10, 1, mock_action, (1, 2), {'key': 'value'})
    sched.cancel(event)
    assert not event in sched._queue

def test_empty():
    mock_time = MockTime()
    mock_action = MockAction()
    sched = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    assert sched.empty()
    sched.enterabs(10, 1, mock_action, (1, 2), {'key': 'value'})
    assert not sched.empty()

def test_run():
    mock_time = MockTime()
    mock_action = MockAction()
    sched = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    sched.enterabs(10, 1, mock_action, (1, 2), {'key': 'value'})
    sched.run()
    assert mock_action.called

def test_run_non_blocking():
    mock_time = MockTime()
    mock_action = MockAction()
    sched = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    sched.enterabs(10, 1, mock_action, (1, 2), {'key': 'value'})
    deadline = sched.run(blocking=False)
    assert deadline == 10

def test_run_with_delay():
    mock_time = MockTime()
    mock_action = MockAction()
    sched = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    sched.enterabs(10, 1, mock_action, (1, 2), {'key': 'value'})
    mock_time.current_time = 5
    sched.run()
    assert mock_action.called

def test_run_with_multiple_events():
    mock_time = MockTime()
    mock_action1 = MockAction()
    mock_action2 = MockAction()
    sched = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    sched.enterabs(10, 1, mock_action1, (1, 2), {'key': 'value'})
    sched.enterabs(15, 2, mock_action2, (3, 4), {'key': 'value'})
    sched.run()
    assert mock_action1.called
    assert mock_action2.called

def test_run_with_priority():
    mock_time = MockTime()
    mock_action1 = MockAction()
    mock_action2 = MockAction()
    sched = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    sched.enterabs(10, 1, mock_action1, (1, 2), {'key': 'value'})
    sched.enterabs(10, 2, mock_action2, (3, 4), {'key': 'value'})
    sched.run()
    assert mock_action2.called
    assert mock_action1.called

def test_run_with_sequence():
    mock_time = MockTime()
    mock_action1 = MockAction()
    mock_action2 = MockAction()
    sched = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    sched.enterabs(10, 1, mock_action1, (1, 2), {'key': 'value'})
    sched.enterabs(10, 1, mock_action2, (3, 4), {'key': 'value'})
    sched.run()
    assert mock_action1.called
    assert mock_action2.called

def test_queue():
    mock_time = MockTime()
    mock_action1 = MockAction()
    mock_action2 = MockAction()
    sched = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    sched.enterabs(10, 1, mock_action1, (1, 2), {'key': 'value'})
    sched.enterabs(15, 2, mock_action2, (3, 4), {'key': 'value'})
    queue = sched.queue
    assert len(queue) == 2
    assert queue[0].time == 10
    assert queue[0].priority == 1
    assert queue[0].sequence == 0
    assert queue[0].action == mock_action1
    assert queue[0].argument == (1, 2)
    assert queue[0].kwargs == {'key': 'value'}
    assert queue[1].time == 15
    assert queue[1].priority == 2
    assert queue[1].sequence == 1
    assert queue[1].action == mock_action2
    assert queue[1].argument == (3, 4)
    assert queue[1].kwargs == {'key': 'value'}