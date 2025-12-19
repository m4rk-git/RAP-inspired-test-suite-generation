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
        self.current_time += delay

# Mocking the scheduler class for testing
class MockScheduler:
    def __init__(self):
        self.queue = []
        self.timefunc = MockTime().time
        self.delayfunc = MockTime().sleep

    def enterabs(self, time, priority, action, argument=(), kwargs=_sentinel):
        event = Event(time, priority, next(count()), action, argument, kwargs)
        self.queue.append(event)
        return event

    def enter(self, delay, priority, action, argument=(), kwargs=_sentinel):
        time = self.timefunc() + delay
        return self.enterabs(time, priority, action, argument, kwargs)

    def cancel(self, event):
        self.queue.remove(event)

    def empty(self):
        return not self.queue

    def run(self, blocking=True):
        while self.queue:
            event = heapq.heappop(self.queue)
            if event.time > self.timefunc():
                self.delayfunc(event.time - self.timefunc())
            event.action(*event.argument, **event.kwargs)
            self.delayfunc(0)

    @property
    def queue(self):
        return list(map(heapq.heappop, [self.queue]*len(self.queue)))

# Test cases
def test_enterabs():
    scheduler = MockScheduler()
    def action():
        pass
    event = scheduler.enterabs(10, 1, action)
    assert event.time == 10
    assert event.priority == 1
    assert event.action == action
    assert scheduler.queue[0] == event

def test_enter():
    scheduler = MockScheduler()
    def action():
        pass
    event = scheduler.enter(5, 1, action)
    assert event.time == 5
    assert event.priority == 1
    assert event.action == action
    assert scheduler.queue[0] == event

def test_cancel():
    scheduler = MockScheduler()
    def action():
        pass
    event = scheduler.enterabs(10, 1, action)
    scheduler.cancel(event)
    assert not scheduler.queue

def test_empty():
    scheduler = MockScheduler()
    assert scheduler.empty()
    scheduler.enterabs(10, 1, lambda: None)
    assert not scheduler.empty()

def test_run():
    scheduler = MockScheduler()
    def action():
        scheduler.queue.append('event_executed')
    scheduler.enterabs(10, 1, action)
    scheduler.run()
    assert scheduler.queue == ['event_executed']

def test_run_with_delay():
    scheduler = MockScheduler()
    def action():
        scheduler.queue.append('event_executed')
    scheduler.enterabs(15, 1, action)
    start_time = scheduler.timefunc()
    scheduler.run(blocking=False)
    assert scheduler.queue == ['event_executed']
    assert scheduler.timefunc() - start_time < 15

def test_run_with_cancel():
    scheduler = MockScheduler()
    def action():
        scheduler.queue.append('event_executed')
    event = scheduler.enterabs(10, 1, action)
    scheduler.run()
    assert scheduler.queue == ['event_executed']
    scheduler.cancel(event)
    assert not scheduler.queue

def test_run_with_multiple_events():
    scheduler = MockScheduler()
    def action1():
        scheduler.queue.append('event1_executed')
    def action2():
        scheduler.queue.append('event2_executed')
    scheduler.enterabs(10, 1, action1)
    scheduler.enterabs(5, 1, action2)
    scheduler.run()
    assert scheduler.queue == ['event2_executed', 'event1_executed']

def test_run_with_priority():
    scheduler = MockScheduler()
    def action1():
        scheduler.queue.append('event1_executed')
    def action2():
        scheduler.queue.append('event2_executed')
    scheduler.enterabs(10, 1, action1)
    scheduler.enterabs(10, 2, action2)
    scheduler.run()
    assert scheduler.queue == ['event2_executed', 'event1_executed']

def test_run_with_blocking_false():
    scheduler = MockScheduler()
    def action():
        scheduler.queue.append('event_executed')
    scheduler.enterabs(15, 1, action)
    start_time = scheduler.timefunc()
    deadline = scheduler.run(blocking=False)
    assert scheduler.queue == ['event_executed']
    assert scheduler.timefunc() - start_time < 15
    assert deadline < 15

def test_run_with_empty_queue():
    scheduler = MockScheduler()
    scheduler.run()
    assert not scheduler.queue

def test_run_with_delayfunc_exception():
    scheduler = MockScheduler()
    def action():
        pass
    def delayfunc(delay):
        raise Exception("Delay function exception")
    scheduler.enterabs(10, 1, action)
    scheduler.delayfunc = delayfunc
    with pytest.raises(Exception):
        scheduler.run()

def test_run_with_action_exception():
    scheduler = MockScheduler()
    def action():
        raise Exception("Action exception")
    scheduler.enterabs(10, 1, action)
    with pytest.raises(Exception):
        scheduler.run()

def test_queue_property():
    scheduler = MockScheduler()
    def action():
        pass
    scheduler.enterabs(10, 1, action)
    assert scheduler.queue[0].time == 10
    assert scheduler.queue[0].priority == 1
    assert scheduler.queue[0].action == action