import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.graphlib as graphlib
from data.complicated_tests.graphlib import *

from types import GenericAlias

def test_data_complicated_tests_graphlib_1():
    from graphlib import TopologicalSorter
    sorter = TopologicalSorter()
    sorter.add("a", "b")
    sorter.add("b")
    assert sorter._find_cycle() is None

def test_3_missing_line():
    from graphlib import TopologicalSorter
    sorter = TopologicalSorter()
    sorter.add("a", "b")
    sorter.add("b")
    sorter.prepare()
    sorter.get_ready()
    assert sorter._ready_nodes is not None

def test_5_missing_line():
    from graphlib import TopologicalSorter
    sorter = TopologicalSorter()
    sorter.add("a", "b")
    sorter.add("b")
    sorter.prepare()
    assert sorter._ready_nodes is not None

def test_6_missing_line():
    from graphlib import TopologicalSorter
    sorter = TopologicalSorter()
    sorter.add("a", "b")
    sorter.add("b")
    sorter.prepare()
    assert sorter._ready_nodes is not None

def test_9_missing_line():
    from graphlib import TopologicalSorter
    sorter = TopologicalSorter()
    sorter.add("a", "b")
    sorter.add("b")
    sorter.prepare()
    sorter.get_ready()
    assert sorter._ready_nodes is not None

def test_10_missing_line():
    from graphlib import TopologicalSorter
    sorter = TopologicalSorter()
    sorter.add("a", "b")
    sorter.add("b")
    sorter.prepare()
    sorter.get_ready()
    assert sorter._ready_nodes is not None

def test_12_missing_line():
    from graphlib import TopologicalSorter
    sorter = TopologicalSorter()
    sorter.add("a", "b")
    sorter.add("b")
    sorter.prepare()
    sorter.get_ready()
    assert sorter._ready_nodes is not None

def test_14_missing_line():
    from graphlib import TopologicalSorter
    sorter = TopologicalSorter()
    sorter.add("a", "b")
    sorter.add("b")
    sorter.prepare()
    sorter.get_ready()
    assert sorter._ready_nodes is not None

def test_19_missing_line():
    from graphlib import TopologicalSorter
    sorter = TopologicalSorter()
    sorter.add("a", "b")
    sorter.add("b")
    sorter.prepare()
    sorter.get_ready()
    assert sorter._ready_nodes is not None

def test_data_complicated_tests_graphlib_2():
    graph = {1: [], 2: [1]}
    ts = graphlib.TopologicalSorter(graph)
    ts.add(3)

def test_19():
    graph = {1: [], 2: [1]}
    ts = graphlib.TopologicalSorter(graph)
    ts.add(2)
    ts.done(1)

def test_23():
    graph = {1: [2], 2: [3], 3: [1]}
    ts = graphlib.TopologicalSorter(graph)
    ts.prepare()

def test_45_48():
    graph = {1: [], 2: [1]}
    ts = graphlib.TopologicalSorter(graph)
    ts.prepare()

def test_50_52():
    graph = {1: [], 2: [1]}
    ts = graphlib.TopologicalSorter(graph)
    ts.prepare()

def test_55_57():
    graph = {1: [2], 2: [3], 3: []}
    ts = graphlib.TopologicalSorter(graph)
    ts.prepare()

def test_74_75():
    graph = {1: [], 2: [1]}
    ts = graphlib.TopologicalSorter(graph)
    ts.prepare()

def test_78_79():
    graph = {1: [2], 2: [3], 3: []}
    ts = graphlib.TopologicalSorter(graph)
    ts.prepare()

def test_82_84():
    graph = {1: [], 2: [1]}
    ts = graphlib.TopologicalSorter(graph)
    ts.prepare()

def test_97_98():
    graph = {1: [], 2: [1]}
    ts = graphlib.TopologicalSorter(graph)
    ts.prepare()

def test_100_101():
    graph = {1: [2], 2: [3], 3: []}
    ts = graphlib.TopologicalSorter(graph)
    ts.prepare()

def test_108_110():
    graph = {1: [], 2: [1]}
    ts = graphlib.TopologicalSorter(graph)
    ts.prepare()

def test_122_123():
    graph = {1: [], 2: [1]}
    ts = graphlib.TopologicalSorter(graph)
    ts

def test_data_complicated_tests_graphlib_3():
    from graphlib import TopologicalSorter
    ts = TopologicalSorter()
    ts._ready_nodes = [1, 2, 3]
    ts._npassedout = 1

def test_98():
    from graphlib import TopologicalSorter
    ts = TopologicalSorter()
    ts._ready_nodes = [1, 2, 3]
    ts._npassedout = 0

def test_122():
    from graphlib import TopologicalSorter
    ts = TopologicalSorter()
    ts.add(1)

def test_126():
    from graphlib import TopologicalSorter
    ts = TopologicalSorter()
    ts._ready_nodes = [1, 2, 3]
    ts._npassedout = 1
    ts.get_ready()

def test_133():
    from graphlib import TopologicalSorter
    ts = TopologicalSorter()
    ts._ready_nodes = [1, 2, 3]
    ts._npassedout = 1
    ts.get_ready()

def test_136():
    from graphlib import TopologicalSorter
    ts = TopologicalSorter()
    ts._ready_nodes = [1, 2, 3]
    ts._npassedout = 1
    ts.get_ready()

def test_148():
    from graphlib import TopologicalSorter
    ts = TopologicalSorter()
    ts._ready_nodes = [1, 2, 3]
    ts._npassedout = 1
    ts.is_active()

def test_153():
    from graphlib import TopologicalSorter
    ts = TopologicalSorter()
    ts._ready_nodes = [1, 2, 3]
    ts._npassedout = 1
    bool(ts)

def test_170():
    from graphlib import TopologicalSorter
    ts = TopologicalSorter()
    ts._node2info = {1: _NodeInfo(1)}
    ts.done(1)

def test_172():
    from graphlib import TopologicalSorter
    ts = TopologicalSorter()
    ts._node2info = {1: _NodeInfo(1)}
    ts.done(1)

def test_175():
    from graphlib import TopologicalSorter, _

def test_data_complicated_tests_graphlib_4():
    graph = {'A': [], 'B': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.add('C', 'A')

def test_98():
    graph = {'A': [], 'B': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.get_ready()

def test_122():
    graph = {'A': [], 'B': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.get_ready()

def test_126():
    graph = {'A': [], 'B': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.get_ready()

def test_133():
    graph = {'A': [], 'B': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.get_ready()

def test_136():
    graph = {'A': [], 'B': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.get_ready()

def test_148():
    graph = {'A': [], 'B': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.is_active()

def test_153():
    graph = {'A': [], 'B': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.is_active()

def test_170():
    graph = {'A': [], 'B': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.done('A')

def test_172():
    graph = {'A': [], 'B': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.done('A')

def test_175():
    graph = {'A': [], 'B': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.done('A')

def test_176():
    graph = {'A': [], 'B': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.done('A')

def test_179():
    graph = {'A': [], 'B': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter
