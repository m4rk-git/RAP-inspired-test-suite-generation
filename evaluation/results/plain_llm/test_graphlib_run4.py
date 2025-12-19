from data.complicated_tests.graphlib import *
import pytest
from typing import List, Tuple, Set

def test_topological_sorter():
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    ts = TopologicalSorter(graph)
    ts.prepare()
    result = list(ts.static_order())
    assert result == ['A', 'B', 'C', 'D']

def test_add_node():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    ts.add('B', 'C')
    ts.add('C', 'D')
    ts.add('D')
    ts.prepare()
    result = list(ts.static_order())
    assert result == ['D', 'C', 'B', 'A']

def test_add_node_with_no_dependencies():
    ts = TopologicalSorter()
    ts.add('A')
    ts.add('B')
    ts.add('C')
    ts.prepare()
    result = list(ts.static_order())
    assert result == ['A', 'B', 'C']

def test_add_node_with_duplicate_dependency():
    ts = TopologicalSorter()
    ts.add('A', 'B')
    ts.add('B', 'A')
    ts.prepare()
    result = list(ts.static_order())
    assert result == ['A', 'B']

def test_add_node_after_prepare():
    ts = TopologicalSorter()
    ts.prepare()
    with pytest.raises(ValueError):
        ts.add('A', 'B')

def test_get_ready():
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    ts = TopologicalSorter(graph)
    ts.prepare()
    result = ts.get_ready()
    assert result == ['A']
    ts.done('A')
    result = ts.get_ready()
    assert result == ['B', 'C']
    ts.done('B', 'C')
    result = ts.get_ready()
    assert result == ['D']
    ts.done('D')
    result = ts.get_ready()
    assert result == ()

def test_is_active():
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    ts = TopologicalSorter(graph)
    ts.prepare()
    assert ts.is_active()
    ts.done('A')
    assert ts.is_active()
    ts.done('B', 'C')
    assert ts.is_active()
    ts.done('D')
    assert not ts.is_active()

def test_done():
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    ts = TopologicalSorter(graph)
    ts.prepare()
    result = ts.get_ready()
    assert result == ['A']
    ts.done('A')
    result = ts.get_ready()
    assert result == ['B', 'C']
    ts.done('B', 'C')
    result = ts.get_ready()
    assert result == ['D']
    ts.done('D')
    result = ts.get_ready()
    assert result == ()

def test_done_with_invalid_node():
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    ts = TopologicalSorter(graph)
    ts.prepare()
    with pytest.raises(ValueError):
        ts.done('E')

def test_done_with_node_not_passed_out():
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    ts = TopologicalSorter(graph)
    ts.prepare()
    with pytest.raises(ValueError):
        ts.done('A', 'B')

def test_done_with_node_already_done():
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    ts = TopologicalSorter(graph)
    ts.prepare()
    ts.done('A')
    with pytest.raises(ValueError):
        ts.done('A')

def test_cycle_error():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_multiple_cycles():
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A'],
        'D': ['E'],
        'E': ['F'],
        'F': ['D']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle in [['A', 'B', 'C', 'A'], ['D', 'E', 'F', 'D']]

def test_cycle_error_with_no_cycles():
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    ts = TopologicalSorter(graph)
    ts.prepare()
    assert not ts.is_active()

def test_cycle_error_with_no_nodes():
    graph = {}
    ts = TopologicalSorter(graph)
    ts.prepare()
    assert not ts.is_active()

def test_cycle_error_with_single_node():
    graph = {
        'A': []
    }
    ts = TopologicalSorter(graph)
    ts.prepare()
    assert not ts.is_active()

def test_cycle_error_with_single_node_with_dependency():
    graph = {
        'A': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle_and_no_nodes():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle_and_no_nodes_and_no_cycles():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle_and_no_nodes_and_no_cycles_and_no_nodes():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with_dependency_and_no_cycle_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles_and_no_nodes_and_no_cycles():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    ts = TopologicalSorter(graph)
    with pytest.raises(CycleError) as exc_info:
        ts.prepare()
    cycle = exc_info.value.args[1]
    assert cycle == ['A', 'B', 'A']

def test_cycle_error_with_single_node_with