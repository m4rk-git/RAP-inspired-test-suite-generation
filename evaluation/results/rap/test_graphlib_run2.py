import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.graphlib as graphlib
from data.complicated_tests.graphlib import *

from types import GenericAlias

def test_data_complicated_tests_graphlib_1():
    graph = {'A': ['B'], 'B': [], 'C': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    return sorter.prepare()

def test_2():
    graph = {'A': ['B'], 'B': [], 'C': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    return sorter.done('A')

def test_3():
    graph = {'A': ['B'], 'B': [], 'C': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    return sorter.get_ready()

def test_4():
    graph = {'A': ['B'], 'B': [], 'C': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    return sorter.is_active()

def test_5():
    graph = {'A': ['B'], 'B': [], 'C': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.add('D', 'B')
    return sorter.done('D')

def test_6():
    graph = {'A': ['B'], 'B': [], 'C': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    return sorter.done('A', 'B')

def test_7():
    graph = {'A': ['B'], 'B': [], 'C': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.done('A')
    return sorter.get_ready()

def test_8():
    graph = {'A': ['B'], 'B': [], 'C': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.done('A')
    return sorter.is_active()

def test_9():
    graph = {'A': ['B'], 'B': [], 'C': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    return sorter._find_cycle()

def test_10():
    graph = {'A': ['B'], 'B': [], 'C': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.done('A')
    return sorter.done('B')

def test_11():
    graph = {'A': ['B'], 'B': [], 'C': ['A']}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    return

def test_data_complicated_tests_graphlib_2():
    sorter = graphlib.TopologicalSorter()
    sorter.add('A')
    sorter.add('B', 'A')

def test_98():
    sorter = graphlib.TopologicalSorter()
    sorter.add('A')
    sorter.prepare()
    sorter.done('A')

def test_110():
    sorter = graphlib.TopologicalSorter()
    sorter.add('A')
    sorter.prepare()
    sorter.done('A')
    sorter.add('B', 'A')

def test_123():
    sorter = graphlib.TopologicalSorter()
    sorter.add('A')
    sorter.prepare()
    sorter.done('A')
    sorter.get_ready()

def test_149():
    sorter = graphlib.TopologicalSorter()
    sorter.add('A')
    sorter.prepare()
    sorter.done('A')

def test_153():
    sorter = graphlib.TopologicalSorter()
    sorter.add('A')
    sorter.prepare()
    sorter.done('A')

def test_176():
    sorter = graphlib.TopologicalSorter()
    sorter.add('A')
    sorter.prepare()
    sorter.done('A')

def test_185():
    sorter = graphlib.TopologicalSorter()
    sorter.add('A')
    sorter.prepare()
    sorter.done('A')

def test_186():
    sorter = graphlib.TopologicalSorter()
    sorter.add('A')
    sorter.prepare()
    sorter.done('A')

def test_188():
    sorter = graphlib.TopologicalSorter()
    sorter.add('A')
    sorter.prepare()
    sorter.done('A')

def test_191():
    sorter = graphlib.TopologicalSorter()
    sorter.add('A')
    sorter.prepare()
    sorter.done('A')

def test_195():
    sorter = graphlib.TopologicalSorter()
    sorter.add('A')
    sorter.prepare()
    sorter.done('A')

def test_200():
    sorter = graphlib.TopologicalSorter()
    sorter.add('A')
    sorter.prepare()
    sorter.done('A')

def test_218():
    sorter = graphlib.TopologicalSorter()
    sorter.add('A')
    sorter.prepare()
    sorter.done('A')

def test_248():
    sorter = graphlib.TopologicalSorter()
    sorter.add('A')
    sorter.prepare()
    sorter.done('A')

def test_252():
    sorter

def test_data_complicated_tests_graphlib_3():
    graph = {"a": [], "b": ["a"], "c": ["b"]}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.add("d", "a")

def test_98():
    graph = {"a": [], "b": ["a"], "c": ["b"]}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.get_ready()

def test_110():
    graph = {"a": [], "b": ["a"], "c": ["b"]}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.get_ready()
    sorter.done("b")
    sorter.done("b")

def test_123():
    graph = {"a": [], "b": ["a"], "c": ["b"]}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.add("d", "a")
    sorter.prepare()
    sorter.get_ready()

def test_149():
    graph = {"a": [], "b": ["a"], "c": ["b"]}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.get_ready()

def test_153():
    graph = {"a": [], "b": ["a"], "c": ["b"]}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.get_ready()
    sorter.done("b")
    sorter.done("b")

def test_176():
    graph = {"a": [], "b": ["a"], "c": ["b"]}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.get_ready()
    sorter.done("b")

def test_185():
    graph = {"a": [], "b": [], "c": ["a"]}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.get_ready()
    sorter.done("b")
    sorter.done("a")

def test_186():
    graph = {"a": [], "b": [], "c": ["a"]}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.get_ready()
    sorter.done("b")
    sorter.done("a")

def test_188():
    graph = {"a": [], "b": ["a"], "c": ["b"]}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.prepare()
    sorter.get

def test_data_complicated_tests_graphlib_4():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1', 'node2')
    sorter.add('node2', 'node3')
    sorter.add('node3', 'node1')
    sorter.prepare()
    sorter.get_ready()

def test_98():
    sorter = graphlib.TopologicalSorter()
    sorter._ready_nodes = []
    sorter._npassedout = 1
    sorter.prepare()

def test_110():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1', 'node2')
    sorter.add('node2', 'node3')
    sorter.add('node3', 'node1')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('node3')

def test_123():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.get_ready()

def test_149():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.get_ready()
    sorter.done('node1')

def test_153():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.get_ready()

def test_176():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1', 'node2')
    sorter.done('node2')

def test_185():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1', 'node2')
    sorter.done('node2')

def test_186():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1', 'node2')
    sorter.done('node2')

def test_188():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1', 'node2')
    sorter.done('node2')

def test_218():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1', 'node2')
    sorter.add('node2', 'node1')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('node1')

def test_248():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1', 'node2')
    sorter.prepare()
    for node in sorter.static_order():
        assert node in ['node1', 'node2']
