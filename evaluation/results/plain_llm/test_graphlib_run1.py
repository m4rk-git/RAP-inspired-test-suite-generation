from data.complicated_tests.graphlib import *
import pytest
from types import GenericAlias

# Test cases for TopologicalSorter class

def test_add_node():
    ts = TopologicalSorter()
    ts.add('A', 'B', 'C')
    assert ts._node2info['A'].npredecessors == 2
    assert ts._node2info['B'].npredecessors == 0
    assert ts._node2info['C'].npredecessors == 0

def test_add_existing_node():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    ts.add('A', 'C')
    assert ts._node2info['A'].npredecessors == 2

def test_add_node_with_no_predecessors():
    ts = TopologicalSorter()
    ts.add('A')
    assert ts._node2info['A'].npredecessors == 0

def test_add_node_with_duplicate_predecessors():
    ts = TopologicalSorter()
    ts.add('A', 'B', 'B')
    assert ts._node2info['A'].npredecessors == 2

def test_add_node_with_non_hashable_predecessor():
    with pytest.raises(TypeError):
        ts = TopologicalSorter()
        ts.add('A', [1, 2])

def test_add_node_with_nonexistent_predecessor():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    assert ts._node2info['B'].npredecessors == 0

def test_prepare_no_cycles():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    ts.add('B', 'C')
    ts.prepare()
    assert ts.is_active()

def test_prepare_with_cycles():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    ts.add('B', 'A')
    with pytest.raises(CycleError):
        ts.prepare()

def test_get_ready_no_nodes():
    ts = TopologicalSorter()
    ts.prepare()
    assert not ts.get_ready()

def test_get_ready_with_nodes():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    ts.add('B', 'C')
    ts.prepare()
    assert ts.get_ready() == ('B',)
    assert ts.get_ready() == ('C',)
    assert not ts.get_ready()

def test_get_ready_with_cycles():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    ts.add('B', 'A')
    ts.prepare()
    assert ts.get_ready() == ('B',)
    assert ts.get_ready() == ('A',)
    assert not ts.get_ready()

def test_done_no_nodes():
    ts = TopologicalSorter()
    ts.prepare()
    with pytest.raises(ValueError):
        ts.done('A')

def test_done_with_nodes():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    ts.add('B', 'C')
    ts.prepare()
    ts.get_ready()
    ts.done('B')
    assert ts.get_ready() == ('C',)
    assert not ts.get_ready()

def test_done_with_cycles():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    ts.add('B', 'A')
    ts.prepare()
    ts.get_ready()
    ts.done('B')
    assert ts.get_ready() == ('A',)
    assert not ts.get_ready()

def test_done_with_nonexistent_node():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    ts.add('B', 'C')
    ts.prepare()
    with pytest.raises(ValueError):
        ts.done('D')

def test_done_with_node_not_ready():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    ts.add('B', 'C')
    ts.prepare()
    with pytest.raises(ValueError):
        ts.done('A')

def test_done_with_node_already_done():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    ts.add('B', 'C')
    ts.prepare()
    ts.get_ready()
    ts.done('B')
    with pytest.raises(ValueError):
        ts.done('B')

def test_is_active_no_nodes():
    ts = TopologicalSorter()
    ts.prepare()
    assert not ts.is_active()

def test_is_active_with_nodes():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    ts.add('B', 'C')
    ts.prepare()
    assert ts.is_active()
    ts.get_ready()
    ts.done('B')
    assert ts.is_active()
    ts.get_ready()
    ts.done('C')
    assert not ts.is_active()

def test_is_active_with_cycles():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    ts.add('B', 'A')
    ts.prepare()
    assert ts.is_active()
    ts.get_ready()
    ts.done('B')
    assert ts.is_active()
    ts.get_ready()
    ts.done('A')
    assert not ts.is_active()

def test_static_order_no_cycles():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    ts.add('B', 'C')
    result = list(ts.static_order())
    assert result == ['A', 'B', 'C']

def test_static_order_with_cycles():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    ts.add('B', 'A')
    with pytest.raises(CycleError):
        list(ts.static_order())

def test_class_getitem():
    ts = TopologicalSorter()
    assert isinstance(ts, GenericAlias)

# Run the tests
if __name__ == "__main__":
    pytest.main()