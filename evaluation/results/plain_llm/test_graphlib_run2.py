from data.complicated_tests.graphlib import *
import pytest
from typing import List, Tuple

def test_topological_sorter_add():
    sorter = TopologicalSorter()
    sorter.add('a', 'b', 'c')
    sorter.add('b', 'd')
    sorter.add('c', 'd')
    sorter.add('d')
    assert sorter._node2info['a'].npredecessors == 2
    assert sorter._node2info['b'].npredecessors == 1
    assert sorter._node2info['c'].npredecessors == 1
    assert sorter._node2info['d'].npredecessors == 0

def test_topological_sorter_add_existing_node():
    sorter = TopologicalSorter()
    sorter.add('a', 'b')
    sorter.add('a', 'c')
    assert sorter._node2info['a'].npredecessors == 2

def test_topological_sorter_add_existing_dependency():
    sorter = TopologicalSorter()
    sorter.add('a', 'b')
    sorter.add('b', 'c')
    sorter.add('a', 'c')
    assert sorter._node2info['b'].npredecessors == 1
    assert sorter._node2info['c'].npredecessors == 2

def test_topological_sorter_add_no_dependencies():
    sorter = TopologicalSorter()
    sorter.add('a')
    assert sorter._node2info['a'].npredecessors == 0

def test_topological_sorter_add_duplicate_dependency():
    sorter = TopologicalSorter()
    sorter.add('a', 'b', 'b')
    assert sorter._node2info['a'].npredecessors == 2

def test_topological_sorter_prepare():
    sorter = TopologicalSorter()
    sorter.add('a', 'b')
    sorter.add('b', 'c')
    sorter.prepare()
    assert sorter._ready_nodes == ['c']

def test_topological_sorter_prepare_cycle():
    sorter = TopologicalSorter()
    sorter.add('a', 'b')
    sorter.add('b', 'c')
    sorter.add('c', 'a')
    with pytest.raises(CycleError) as exc_info:
        sorter.prepare()
    assert 'nodes are in a cycle' in str(exc_info.value)
    assert exc_info.value.args[1] == ['a', 'b', 'c', 'a']

def test_topological_sorter_get_ready():
    sorter = TopologicalSorter()
    sorter.add('a', 'b')
    sorter.add('b', 'c')
    sorter.prepare()
    assert sorter.get_ready() == ('c',)
    assert sorter.get_ready() == ()

def test_topological_sorter_get_ready_no_prepare():
    sorter = TopologicalSorter()
    with pytest.raises(ValueError) as exc_info:
        sorter.get_ready()
    assert 'prepare() must be called first' in str(exc_info.value)

def test_topological_sorter_is_active():
    sorter = TopologicalSorter()
    sorter.add('a', 'b')
    sorter.add('b', 'c')
    sorter.prepare()
    assert sorter.is_active()
    sorter.done('c')
    assert sorter.is_active()
    sorter.done('b')
    assert not sorter.is_active()

def test_topological_sorter_is_active_no_prepare():
    sorter = TopologicalSorter()
    with pytest.raises(ValueError) as exc_info:
        sorter.is_active()
    assert 'prepare() must be called first' in str(exc_info.value)

def test_topological_sorter_done():
    sorter = TopologicalSorter()
    sorter.add('a', 'b')
    sorter.add('b', 'c')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('b')
    assert sorter._ready_nodes == ['c']

def test_topological_sorter_done_not_ready():
    sorter = TopologicalSorter()
    sorter.add('a', 'b')
    sorter.add('b', 'c')
    sorter.prepare()
    with pytest.raises(ValueError) as exc_info:
        sorter.done('c')
    assert 'node c was not passed out (still not ready)' in str(exc_info.value)

def test_topological_sorter_done_already_done():
    sorter = TopologicalSorter()
    sorter.add('a', 'b')
    sorter.add('b', 'c')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('b')
    with pytest.raises(ValueError) as exc_info:
        sorter.done('b')
    assert 'node b was already marked done' in str(exc_info.value)

def test_topological_sorter_done_not_added():
    sorter = TopologicalSorter()
    with pytest.raises(ValueError) as exc_info:
        sorter.done('a')
    assert 'node a was not added using add()' in str(exc_info.value)

def test_topological_sorter_done_no_prepare():
    sorter = TopologicalSorter()
    with pytest.raises(ValueError) as exc_info:
        sorter.done('a')
    assert 'prepare() must be called first' in str(exc_info.value)

def test_topological_sorter_static_order():
    sorter = TopologicalSorter()
    sorter.add('a', 'b')
    sorter.add('b', 'c')
    sorter.add('c', 'd')
    sorter.add('d')
    result = list(sorter.static_order())
    assert result == ['d', 'c', 'b', 'a']

def test_topological_sorter_static_order_cycle():
    sorter = TopologicalSorter()
    sorter.add('a', 'b')
    sorter.add('b', 'c')
    sorter.add('c', 'a')
    with pytest.raises(CycleError) as exc_info:
        list(sorter.static_order())
    assert 'nodes are in a cycle' in str(exc_info.value)
    assert exc_info.value.args[1] == ['a', 'b', 'c', 'a']