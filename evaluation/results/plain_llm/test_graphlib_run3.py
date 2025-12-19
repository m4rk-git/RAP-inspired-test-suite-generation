from data.complicated_tests.graphlib import *
import pytest
from typing import List, Tuple, Dict, Set

# Test cases for TopologicalSorter class

def test_add_nodes():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    assert sorter._node2info['A'].npredecessors == 2
    assert sorter._node2info['B'].npredecessors == 1
    assert sorter._node2info['C'].npredecessors == 1
    assert sorter._node2info['D'].npredecessors == 0
    assert sorter._node2info['A'].successors == ['B', 'C']
    assert sorter._node2info['B'].successors == ['D']
    assert sorter._node2info['C'].successors == ['D']
    assert sorter._node2info['D'].successors == []

def test_add_nodes_with_duplicates():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'B', 'C')
    assert sorter._node2info['A'].npredecessors == 2
    assert sorter._node2info['B'].npredecessors == 1
    assert sorter._node2info['C'].npredecessors == 1

def test_add_nodes_with_nonexistent_predecessors():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'E')
    assert sorter._node2info['D'].npredecessors == 0
    assert sorter._node2info['E'].npredecessors == 0

def test_prepare_no_cycles():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    sorter.prepare()
    assert sorter.is_active()
    assert sorter.get_ready() == ('D',)
    sorter.done('D')
    assert not sorter.is_active()

def test_prepare_with_cycles():
    sorter = TopologicalSorter()
    sorter.add('A', 'B')
    sorter.add('B', 'A')
    with pytest.raises(CycleError) as exc_info:
        sorter.prepare()
    assert "nodes are in a cycle" in str(exc_info.value)
    assert exc_info.value.args[1] == ['A', 'B', 'A']

def test_get_ready_no_nodes():
    sorter = TopologicalSorter()
    sorter.prepare()
    assert not sorter.is_active()
    assert sorter.get_ready() == ()

def test_get_ready_with_nodes():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    sorter.prepare()
    assert sorter.get_ready() == ('D',)
    sorter.done('D')
    assert sorter.get_ready() == ()

def test_done_no_nodes():
    sorter = TopologicalSorter()
    sorter.prepare()
    with pytest.raises(ValueError) as exc_info:
        sorter.done('A')
    assert "node 'A' was not added using add()" in str(exc_info.value)

def test_done_with_nodes():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    sorter.prepare()
    assert sorter.get_ready() == ('D',)
    sorter.done('D')
    assert not sorter.is_active()

def test_done_with_nonexistent_nodes():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    sorter.prepare()
    with pytest.raises(ValueError) as exc_info:
        sorter.done('E')
    assert "node 'E' was not added using add()" in str(exc_info.value)

def test_done_with_nodes_not_ready():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    sorter.prepare()
    with pytest.raises(ValueError) as exc_info:
        sorter.done('A')
    assert "node 'A' was not passed out (still not ready)" in str(exc_info.value)

def test_done_with_nodes_already_done():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.done('D')
    assert "node 'D' was already marked done" in str(exc_info.value)

def test_static_order_no_cycles():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    result = list(sorter.static_order())
    assert result == ['D', 'B', 'C', 'A']

def test_static_order_with_cycles():
    sorter = TopologicalSorter()
    sorter.add('A', 'B')
    sorter.add('B', 'A')
    with pytest.raises(CycleError) as exc_info:
        list(sorter.static_order())
    assert "nodes are in a cycle" in str(exc_info.value)
    assert exc_info.value.args[1] == ['A', 'B', 'A']

def test_static_order_no_nodes():
    sorter = TopologicalSorter()
    result = list(sorter.static_order())
    assert result == []

def test_static_order_with_nodes():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    result = list(sorter.static_order())
    assert result == ['D', 'B', 'C', 'A']

def test_static_order_with_nonexistent_nodes():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.add('E', 'A')
    assert "node 'E' was not added using add()" in str(exc_info.value)

def test_static_order_with_nodes_not_ready():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.done('A')
    assert "node 'A' was not passed out (still not ready)" in str(exc_info.value)

def test_static_order_with_nodes_already_done():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.done('D')
    assert "node 'D' was already marked done" in str(exc_info.value)

def test_static_order_with_nodes_not_added():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.add('E', 'A')
    assert "node 'E' was not added using add()" in str(exc_info.value)

def test_static_order_with_nodes_not_ready():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.done('A')
    assert "node 'A' was not passed out (still not ready)" in str(exc_info.value)

def test_static_order_with_nodes_already_done():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.done('D')
    assert "node 'D' was already marked done" in str(exc_info.value)

def test_static_order_with_nodes_not_added():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.add('E', 'A')
    assert "node 'E' was not added using add()" in str(exc_info.value)

def test_static_order_with_nodes_not_ready():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.done('A')
    assert "node 'A' was not passed out (still not ready)" in str(exc_info.value)

def test_static_order_with_nodes_already_done():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.done('D')
    assert "node 'D' was already marked done" in str(exc_info.value)

def test_static_order_with_nodes_not_added():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.add('E', 'A')
    assert "node 'E' was not added using add()" in str(exc_info.value)

def test_static_order_with_nodes_not_ready():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.done('A')
    assert "node 'A' was not passed out (still not ready)" in str(exc_info.value)

def test_static_order_with_nodes_already_done():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.done('D')
    assert "node 'D' was already marked done" in str(exc_info.value)

def test_static_order_with_nodes_not_added():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.add('E', 'A')
    assert "node 'E' was not added using add()" in str(exc_info.value)

def test_static_order_with_nodes_not_ready():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.done('A')
    assert "node 'A' was not passed out (still not ready)" in str(exc_info.value)

def test_static_order_with_nodes_already_done():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.done('D')
    assert "node 'D' was already marked done" in str(exc_info.value)

def test_static_order_with_nodes_not_added():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.add('E', 'A')
    assert "node 'E' was not added using add()" in str(exc_info.value)

def test_static_order_with_nodes_not_ready():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.done('A')
    assert "node 'A' was not passed out (still not ready)" in str(exc_info.value)

def test_static_order_with_nodes_already_done():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter.add('B', 'D')
    sorter.add('C', 'D')
    sorter.add('D')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('D')
    with pytest.raises(ValueError) as exc_info:
        sorter.done('D')
    assert "node 'D' was already marked done" in str(exc_info.value)

def test_static_order_with_nodes_not_added():
    sorter = TopologicalSorter()
    sorter.add('A', 'B', 'C')
    sorter