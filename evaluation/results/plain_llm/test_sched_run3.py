from data.complicated_tests.sched import *
import pytest
import threading
import time

def test_enterabs():
    sched = scheduler()
    event = sched.enterabs(10, 1, lambda: None)
    assert event.time == 10
    assert event.priority == 1
    assert event.sequence == 0
    assert event.action == lambda: None
    assert event.argument == ()
    assert event.kwargs == {}

def test_enter():
    sched = scheduler()
    event = sched.enter(5, 1, lambda: None)
    assert event.time == sched.timefunc() + 5
    assert event.priority == 1
    assert event.sequence == 0
    assert event.action == lambda: None
    assert event.argument == ()
    assert event.kwargs == {}

def test_cancel():
    sched = scheduler()
    event = sched.enterabs(10, 1, lambda: None)
    sched.cancel(event)
    with pytest.raises(ValueError):
        sched.cancel(event)

def test_empty():
    sched = scheduler()
    assert sched.empty()
    sched.enterabs(10, 1, lambda: None)
    assert not sched.empty()

def test_run():
    sched = scheduler()
    event = sched.enterabs(10, 1, lambda: None)
    assert sched.run() == 10 - sched.timefunc()
    assert not sched.empty()

def test_run_non_blocking():
    sched = scheduler()
    event = sched.enterabs(10, 1, lambda: None)
    assert sched.run(blocking=False) == 10 - sched.timefunc()
    assert not sched.empty()

def test_run_with_delay():
    sched = scheduler()
    event = sched.enterabs(10, 1, lambda: None)
    with patch.object(sched, 'delayfunc', wraps=sched.delayfunc) as mock_delay:
        sched.run()
        mock_delay.assert_called_once_with(10 - sched.timefunc())

def test_run_with_exception():
    sched = scheduler()
    event = sched.enterabs(10, 1, lambda: None)
    with patch.object(sched, 'delayfunc', side_effect=Exception):
        with pytest.raises(Exception):
            sched.run()

def test_queue():
    sched = scheduler()
    event1 = sched.enterabs(10, 1, lambda: None)
    event2 = sched.enterabs(5, 1, lambda: None)
    assert sched.queue == [event2, event1]