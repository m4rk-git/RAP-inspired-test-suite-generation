import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.graphlib as graphlib
from data.complicated_tests.graphlib import *

from types import GenericAlias

def test_data_complicated_tests_graphlib_1(): graphlib.TopologicalSorter._get_nodeinfo(2)
def test_2(): graphlib.TopologicalSorter.prepare()
def test_3(): graphlib.TopologicalSorter.get_ready()
def test_4(): graphlib.TopologicalSorter.is_active()
def test_5(): graphlib.TopologicalSorter.static_order()
def test_6(): graphlib.CycleError()
def test_7(): graphlib.TopologicalSorter.add(1)
def test_8(): graphlib.TopologicalSorter.done(2)
def test_9(): graphlib.TopologicalSorter._find_cycle()

def test_data_complicated_tests_graphlib_2():
    graph = {}
    sorter = graphlib.TopologicalSorter(graph)
    sorter.add("A")

def test_data_complicated_tests_graphlib_3():
    graphlib.TopologicalSorter(graph={"A": ["B"], "B": ["C"], "C": ["A"]})

def test_75():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.done("A")

def test_83_84():
    sorter = graphlib.TopologicalSorter()
    sorter.add("A", "B", "C")
    sorter.add("D", "A")

def test_97_98():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.done("A")
    sorter.get_ready()

def test_100_101():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.get_ready()

def test_108_110():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.done("A")
    sorter.get_ready()

def test_122_123():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.get_ready()

def test_126_129():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.get_ready()

def test_133_134():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.done("A")
    sorter.get_ready()

def test_136():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.get_ready()

def test_148_150():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.get_ready()

def test_153():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.get_ready()

def test_168():
    sorter = graphlib.TopologicalSorter()
    sorter.add("A", "B")
    sorter.prepare()
    sorter.get_ready()

def test_170():
    sorter = graphlib.TopologicalSorter()
    sorter.add("A", "B")
    sorter.prepare()
    sorter.get_ready()

def test_172():
    sorter = graphlib.TopologicalSorter()
    sorter.add("A", "B")
    sorter.prepare()
    sorter.get_ready()

def test_175_176():
    sorter = graphlib.TopologicalSorter()
    sorter.add("A", "B")
    sorter.prepare

def test_data_complicated_tests_graphlib_4():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1')

def test_98():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.add('node1')

def test_110():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.add('node1')
    sorter.get_ready()
    sorter.done('node1')

def test_123():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.add('node1')

def test_148():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.add('node1')
    sorter.get_ready()
    sorter.done('node1')

def test_153():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.add('node1')
    sorter.get_ready()
    sorter.done('node1')

def test_168():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.add('node1')
    sorter.get_ready()
    sorter.done('node1')

def test_179():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.add('node1')
    sorter.get_ready()

def test_182():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.add('node1')
    sorter.get_ready()

def test_185():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.add('node1')
    sorter.get_ready()
    sorter.done('node1')

def test_186():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.add('node1')
    sorter.get_ready()
    sorter.done('node1')

def test_188():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.add('node1')
    sorter.get_ready()
    sorter.done('node1')

def test_191():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.add('node1')
    sorter.get_ready()
    sorter.done('node1')

def test_195():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.add('node1')
    sorter.get_ready()
    sorter.done('node1')

def test_200():
    sorter = graph

def test_data_complicated_tests_graphlib_5():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a')
    sorter.prepare()
    sorter.node2info


def test_110():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a')
    sorter.prepare()
    sorter.n_passedout


def test_123():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a')
    sorter.prepare()
    sorter.ready_nodes


def test_148_150():
    sorter = graphlib.TopologicalSorter({'a': []})
    sorter.prepare()
    sorter.is_active()


def test_153():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a')
    sorter.prepare()
    bool(sorter)


def test_168():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a')
    sorter.prepare()
    sorter.node2info['a']


def test_179_182():
    sorter = graphlib.TopologicalSorter({'a': []})
    sorter.prepare()
    sorter.done('a')


def test_185_186():
    sorter = graphlib.TopologicalSorter({'a': []})
    sorter.prepare()
    sorter.done('a')


def test_188():
    sorter = graphlib.TopologicalSorter({'a': []})
    sorter.prepare()
    sorter.node2info['a'].npredecessors


def test_191():
    sorter = graphlib.TopologicalSorter({'a': []})
    sorter.prepare()
    sorter.node2info['a'].npredecessors = -2


def test_195_200():
    sorter = graphlib.TopologicalSorter({'a': []})
    sorter.prepare()
    sorter.done('a')
    sorter.node2info['a'].successors


def test_211():
    sorter = graphlib.TopologicalSorter({'a': []})
    sorter.prepare()
    'a' in sorter.node2info


def test_218():
    sorter = graphlib.TopologicalSorter({'a': ['b']})
    sorter.prepare()
    sorter.done('b')


def test_248_252():
    sorter = graphlib.TopologicalSorter({'a': []})
    for node in sorter.static_order():
        pass
    sorter.node2info['a'].npredecessors
