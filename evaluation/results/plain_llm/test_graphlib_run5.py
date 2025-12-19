from data.complicated_tests.graphlib import *
import pytest
from typing import *

def test_add_nodes():
    ts = TopologicalSorter()
    ts.add('a', 'b', 'c')
    ts.add('b', 'c')
    ts.add('c')
    assert ts._node2info['a'].npredecessors == 2
    assert ts._node2info['b'].npredecessors == 2
    assert ts._node2info['c'].npredecessors == 0
    assert 'a' in ts._ready_nodes
    assert 'b' in ts._ready_nodes
    assert 'c' in ts._ready_nodes

def test_add_existing_node():
    ts = TopologicalSorter()
    ts.add('a', 'b')
    ts.add('a', 'c')
    assert ts._node2info['a'].npredecessors == 2
    assert 'a' in ts._ready_nodes

def test_add_node_with_no_dependencies():
    ts = TopologicalSorter()
    ts.add('a')
    assert ts._node2info['a'].npredecessors == 0
    assert 'a' in ts._ready_nodes

def test_add_node_with_duplicate_dependency():
    ts = TopologicalSorter()
    ts.add('a', 'b', 'b')
    assert ts._node2info['a'].npredecessors == 2
    assert 'a' in ts._ready_nodes

def test_add_node_with_nonexistent_dependency():
    ts = TopologicalSorter()
    ts.add('a', 'b')
    ts.add('b')
    assert ts._node2info['a'].npredecessors == 1
    assert 'a' in ts._ready_nodes

def test_prepare_no_cycles():
    ts = TopologicalSorter()
    ts.add('a', 'b')
    ts.add('b', 'c')
    ts.add('c')
    ts.prepare()
    assert ts.is_active()
    assert 'a' in ts._ready_nodes
    assert 'b' in ts._ready_nodes
    assert 'c' in ts._ready_nodes

def test_prepare_with_cycles():
    ts = TopologicalSorter()
    ts.add('a', 'b')
    ts.add('b', 'c')
    ts.add('c', 'a')
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    assert 'a' in exc_info.value.args[1]

def test_get_ready_no_nodes_ready():
    ts = TopologicalSorter()
    ts.add('a', 'b')
    ts.add('b', 'c')
    ts.add('c')
    ts.prepare()
    ts.done('a', 'b', 'c')
    assert not ts.is_active()
    assert ts.get_ready() == ()

def test_get_ready_nodes_ready():
    ts = TopologicalSorter()
    ts.add('a', 'b')
    ts.add('b', 'c')
    ts.add('c')
    ts.prepare()
    assert ts.get_ready() == ('a', 'b', 'c')

def test_done_node_not_ready():
    ts = TopologicalSorter()
    ts.add('a', 'b')
    ts.add('b', 'c')
    ts.add('c')
    ts.prepare()
    with pytest.raises(ValueError) as exc_info:
        ts.done('d')
    assert 'd' in exc_info.value.args[0]

def test_done_node_not_added():
    ts = TopologicalSorter()
    ts.add('a', 'b')
    ts.add('b', 'c')
    ts.add('c')
    ts.prepare()
    with pytest.raises(ValueError) as exc_info:
        ts.done('d')
    assert 'd' in exc_info.value.args[0]

def test_done_node_already_done():
    ts = TopologicalSorter()
    ts.add('a', 'b')
    ts.add('b', 'c')
    ts.add('c')
    ts.prepare()
    ts.done('a', 'b', 'c')
    with pytest.raises(ValueError) as exc_info:
        ts.done('a', 'b', 'c')
    assert 'a' in exc_info.value.args[0]

def test_done_node_not_passed_out():
    ts = TopologicalSorter()
    ts.add('a', 'b')
    ts.add('b', 'c')
    ts.add('c')
    ts.prepare()
    with pytest.raises(ValueError) as exc_info:
        ts.done('a', 'b')
    assert 'a' in exc_info.value.args[0]

def test_is_active_no_nodes_ready():
    ts = TopologicalSorter()
    ts.add('a', 'b')
    ts.add('b', 'c')
    ts.add('c')
    ts.prepare()
    ts.done('a', 'b', 'c')
    assert not ts.is_active()

def test_is_active_nodes_ready():
    ts = TopologicalSorter()
    ts.add('a', 'b')
    ts.add('b', 'c')
    ts.add('c')
    ts.prepare()
    assert ts.is_active()

def test_is_active_no_nodes_passed_out():
    ts = TopologicalSorter()
    ts.add('a', 'b')
    ts.add('b', 'c')
    ts.add('c')
    ts.prepare()
    assert ts.is_active()

def test_is_active_nodes_passed_out():
    ts = TopologicalSorter()
    ts.add('a', 'b')
    ts.add('b', 'c')
    ts.add('c')
    ts.prepare()
    ts.done('a', 'b', 'c')
    assert not ts.is_active()

def test_static_order_no_cycles():
    ts = TopologicalSorter()
    ts.add('a', 'b')
    ts.add('b', 'c')
    ts.add('c')
    result = list(ts.static_order())
    assert result == ['a', 'b', 'c']

def test_static_order_with_cycles():
    ts = TopologicalSorter()
    ts.add('a', 'b')
    ts.add('b', 'c')
    ts.add('c', 'a')
    with pytest.raises(CycleError) as exc_info:
        list(ts.static_order())
    assert 'a' in exc_info.value.args[1]