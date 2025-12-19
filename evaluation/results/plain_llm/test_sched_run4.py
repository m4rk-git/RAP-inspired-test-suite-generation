from data.complicated_tests.sched import *
import pytest
import threading
import time

# Mocking time and sleep functions for testing
class MockTime:
    def __init__(self):
        self.current_time = 0

    def time(self):
        return self.current_time

    def sleep(self, delay):
        time.sleep(delay)

def test_scheduler_enterabs():
    mock_time = MockTime()
    sch = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    mock_time.current_time = 10
    event_id = sch.enterabs(15, 1, lambda: None)
    assert isinstance(event_id, Event)
    assert sch.queue[0].time == 15

def test_scheduler_enter():
    mock_time = MockTime()
    sch = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    mock_time.current_time = 10
    event_id = sch.enter(5, 1, lambda: None)
    assert isinstance(event_id, Event)
    assert sch.queue[0].time == 15

def test_scheduler_cancel():
    mock_time = MockTime()
    sch = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    mock_time.current_time = 10
    event_id = sch.enterabs(15, 1, lambda: None)
    sch.cancel(event_id)
    assert not sch.queue

def test_scheduler_empty():
    mock_time = MockTime()
    sch = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    assert sch.empty()
    sch.enterabs(15, 1, lambda: None)
    assert not sch.empty()

def test_scheduler_run():
    mock_time = MockTime()
    sch = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    mock_time.current_time = 10
    sch.enterabs(15, 1, lambda: mock_time.current_time := 20)
    sch.run()
    assert mock_time.current_time == 20

def test_scheduler_run_non_blocking():
    mock_time = MockTime()
    sch = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    mock_time.current_time = 10
    sch.enterabs(15, 1, lambda: mock_time.current_time := 20)
    deadline = sch.run(blocking=False)
    assert deadline == 5
    assert mock_time.current_time == 15

def test_scheduler_run_with_delay():
    mock_time = MockTime()
    sch = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    mock_time.current_time = 10
    sch.enterabs(15, 1, lambda: mock_time.current_time := 20)
    sch.run()
    assert mock_time.current_time == 20

def test_scheduler_run_with_cancel():
    mock_time = MockTime()
    sch = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    mock_time.current_time = 10
    event_id = sch.enterabs(15, 1, lambda: mock_time.current_time := 20)
    sch.cancel(event_id)
    sch.run()
    assert mock_time.current_time == 10

def test_scheduler_queue():
    mock_time = MockTime()
    sch = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    mock_time.current_time = 10
    sch.enterabs(15, 1, lambda: None)
    sch.enterabs(10, 2, lambda: None)
    assert sch.queue[0].time == 10
    assert sch.queue[1].time == 15

def test_scheduler_thread_safety():
    mock_time = MockTime()
    sch = scheduler(timefunc=mock_time.time, delayfunc=mock_time.sleep)
    def add_event():
        sch.enterabs(15, 1, lambda: None)
    threads = [threading.Thread(target=add_event) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    assert len(sch.queue) == 10