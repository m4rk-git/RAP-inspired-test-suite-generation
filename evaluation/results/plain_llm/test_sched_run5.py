from data.complicated_tests.sched import *
import pytest
import threading
import time

def test_enterabs():
    sch = scheduler()
    event = sch.enterabs(10, 1, lambda: None)
    assert event.time == 10
    assert event.priority == 1
    assert event.sequence == 0
    assert event.action == lambda: None
    assert event.argument == ()
    assert event.kwargs == {}

def test_enter():
    sch = scheduler()
    event = sch.enter(5, 1, lambda: None)
    assert event.time == sch.timefunc() + 5
    assert event.priority == 1
    assert event.sequence == 0
    assert event.action == lambda: None
    assert event.argument == ()
    assert event.kwargs == {}

def test_cancel():
    sch = scheduler()
    event = sch.enterabs(10, 1, lambda: None)
    sch.cancel(event)
    with pytest.raises(ValueError):
        sch.cancel(event)

def test_empty():
    sch = scheduler()
    assert sch.empty()
    sch.enterabs(10, 1, lambda: None)
    assert not sch.empty()

def test_run():
    sch = scheduler()
    sch.enterabs(10, 1, lambda: None)
    sch.enterabs(20, 1, lambda: None)
    sch.run()
    assert sch.empty()

def test_run_non_blocking():
    sch = scheduler()
    sch.enterabs(10, 1, lambda: None)
    sch.enterabs(20, 1, lambda: None)
    deadline = sch.run(blocking=False)
    assert deadline == 10

def test_run_with_delay():
    sch = scheduler()
    sch.enterabs(10, 1, lambda: None)
    sch.enterabs(20, 1, lambda: None)
    with patch('time.sleep') as mock_sleep:
        sch.run()
        mock_sleep.assert_called_once_with(0)

def test_run_with_exception():
    sch = scheduler()
    sch.enterabs(10, 1, lambda: None)
    sch.enterabs(20, 1, lambda: None)
    with patch('time.sleep') as mock_sleep:
        mock_sleep.side_effect = Exception
        sch.run()
        mock_sleep.assert_called_once_with(0)

def test_queue():
    sch = scheduler()
    sch.enterabs(10, 1, lambda: None)
    sch.enterabs(20, 1, lambda: None)
    queue = sch.queue
    assert len(queue) == 2
    assert queue[0].time == 10
    assert queue[1].time == 20

def test_thread_safety():
    sch = scheduler()
    def add_event():
        sch.enterabs(10, 1, lambda: None)
    threads = [threading.Thread(target=add_event) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    assert not sch.empty()