import sys
import os
sys.path.append(r'/root/RAPiT-project')
sys.path.append(r'/root/RAPiT-project/data/complicated_tests')
import pytest
import data.complicated_tests.graphlib as graphlib
from data.complicated_tests.graphlib import *

from types import GenericAlias

def test_data_complicated_tests_graphlib_1(graphlib):
    graphlib._NODE_OUT

def test_data_complicated_tests_graphlib_2():
    ts = graphlib.TopologicalSorter()
    ts.add("node1")
    ts.add("node2", "node1")

def test_19():
    ts = graphlib.TopologicalSorter()
    nodeinfo = ts._get_nodeinfo("node1")

def test_23():
    ts = graphlib.TopologicalSorter()
    nodeinfo = ts._get_nodeinfo("node1")
    nodeinfo.npredecessors = -1

def test_45_48():
    ts = graphlib.TopologicalSorter()
    ts.add("node1")
    ts.add("node2", "node1")
    ts.prepare()

def test_50_52():
    ts = graphlib.TopologicalSorter()
    ts.add("node1")
    ts.add("node2", "node1")
    ts.prepare()
    ts.get_ready()

def test_55_57():
    ts = graphlib.TopologicalSorter()
    ts.add("node1")
    ts.add("node2", "node1")
    ts.prepare()
    ts.done("node1")

def test_74_75():
    ts = graphlib.TopologicalSorter()
    ts.add("node1")
    ts.add("node2", "node1")
    ts.prepare()
    ts.get_ready()

def test_78_79():
    ts = graphlib.TopologicalSorter()
    ts.add("node1")
    ts.add("node2", "node1")
    ts.prepare()
    ts.get_ready()

def test_82_84():
    ts = graphlib.TopologicalSorter()
    ts.add("node1")
    ts.add("node2", "node1")
    ts.prepare()
    ts.get_ready()
    ts.done("node1")

def test_97_98():
    ts = graphlib.TopologicalSorter()
    ts.add("node1")
    ts.add("node2", "node1")
    ts.prepare()
    ts.get_ready()
    ts.done("node1")

def test_100_101():
    ts = graphlib.TopologicalSorter()
    ts.add("node1")
    ts.add("node2", "node1")
    ts.prepare()
    ts.get_ready()
    ts.done("node1")

def test_108_110():
    ts = graphlib.TopologicalSorter()
    ts.add

def test_data_complicated_tests_graphlib_3():
    sorter = graphlib.TopologicalSorter()
    sorter.add(1, 2)
    sorter.add(3)

def test_75():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.get_ready()

def test_98():
    sorter = graphlib.TopologicalSorter()
    sorter.add(1, 2)
    sorter.done(1)

def test_110():
    sorter = graphlib.TopologicalSorter()
    sorter.add(1, 2)
    sorter.prepare()
    sorter.done(1)

def test_123():
    sorter = graphlib.TopologicalSorter()
    sorter.add(1, 2)
    sorter.prepare()
    sorter.get_ready()

def test_148_150():
    sorter = graphlib.TopologicalSorter()
    sorter.add(1, 2)
    sorter.prepare()
    sorter.is_active()

def test_153():
    sorter = graphlib.TopologicalSorter()
    sorter.prepare()
    sorter.get_ready()

def test_168():
    sorter = graphlib.TopologicalSorter()
    sorter.add(1, 2)
    sorter.prepare()
    sorter.done(1)

def test_176():
    sorter = graphlib.TopologicalSorter()
    sorter.add(1, 2)
    sorter.done(1)

def test_185_186():
    sorter = graphlib.TopologicalSorter()
    sorter.add(1, 2)
    sorter.done(1)

def test_188():
    sorter = graphlib.TopologicalSorter()
    sorter.add(1, 2)
    sorter.done(1)

def test_217_218():
    sorter = graphlib.TopologicalSorter()
    sorter.add(1, 2)
    sorter.prepare()
    sorter.done(1)

def test_248_252():
    sorter = graphlib.TopologicalSorter()
    sorter.add(1, 2)
    sorter.static_order()

def test_data_complicated_tests_graphlib_4():
    graphlib.TopologicalSorter({1: [2], 2: [3]}).add(3, 4)

def test_data_complicated_tests_graphlib_5():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1')
    sorter.add('node2', 'node1')
    sorter.add('node3', 'node2')

def test_98():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1')
    sorter.prepare()
    sorter.get_ready()

def test_110():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1')
    sorter.add('node2', 'node1')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('node1')

def test_123():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1')
    sorter.prepare()
    sorter.get_ready()

def test_149():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1')
    sorter.prepare()
    sorter.get_ready()

def test_153():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1')
    sorter.prepare()
    sorter.get_ready()

def test_176():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1')
    sorter.add('node2', 'node1')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('node1')
    sorter.get_ready()

def test_185_186():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1')
    sorter.add('node2', 'node1')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('node2')

def test_188():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('node1')

def test_218():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1')
    sorter.add('node2', 'node1')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('node2')

def test_248_252():
    sorter = graphlib.TopologicalSorter()
    sorter.add('node1')
    sorter.add('node2', 'node1')
    sorter.prepare()
    next(sorter.static_order())

def test_data_complicated_tests_graphlib_6():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a', 'b')
    sorter.add('b', 'a')

def test_98():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a', 'b')
    sorter.prepare()
    sorter.done('b')
    sorter.get_ready()

def test_110():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a', 'b')
    sorter.prepare()
    sorter.get_ready()
    sorter.done('b')

def test_123():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a', 'b')
    sorter.prepare()
    print(sorter.get_ready())

def test_149():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a', 'b')
    sorter.prepare()
    sorter.done('a')

def test_153():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a', 'b')
    sorter.prepare()
    print(sorter.is_active())

def test_168():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a', 'b')
    sorter.prepare()
    sorter.done('a')
    print(sorter.is_active())

def test_176():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a', 'b')
    sorter.prepare()
    sorter.done('a', 'b')

def test_185():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a', 'b')
    sorter.prepare()
    sorter.done('a')

def test_186():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a', 'b')
    sorter.prepare()
    sorter.done('a')

def test_188():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a', 'b')
    sorter.prepare()
    sorter.done('b')

def test_218():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a', 'b')
    sorter.prepare()
    print(next(sorter.static_order()))

def test_252():
    sorter = graphlib.TopologicalSorter()
    sorter.add('a', 'b')
    print(next(sorter.static_order()))

def test_data_complicated_tests_graphlib_7():
    T = graphlib.TopologicalSorter()
    T.add(1, 2)
    T.add(2)
    T.prepare()

def test_98():
    T = graphlib.TopologicalSorter()
    T.add(1)
    T.prepare()
    T.get_ready()

def test_110():
    T = graphlib.TopologicalSorter()
    T.add(1)
    T.prepare()
    T._find_cycle()

def test_123():
    T = graphlib.TopologicalSorter()
    T.add(1, 2)
    T.prepare()
    T.get_ready()

def test_149():
    T = graphlib.TopologicalSorter()
    T.add(1, 2)
    T.prepare()
    T.done(1)

def test_153():
    T = graphlib.TopologicalSorter()
    T.add(1, 2)
    T.prepare()
    T.is_active()

def test_168():
    T = graphlib.TopologicalSorter()
    T.add(1, 2)
    T.prepare()
    T.done(1)

def test_176():
    T = graphlib.TopologicalSorter()
    T.add(1, 2)
    T.prepare()
    T.done(2)

def test_185():
    T = graphlib.TopologicalSorter()
    T.add(1, 2)
    T.prepare()
    T.done(2)

def test_186():
    T = graphlib.TopologicalSorter()
    T.add(1, 2)
    T.prepare()
    T.done(2)

def test_188():
    T = graphlib.TopologicalSorter()
    T.add(1, 2)
    T.done(2)
    T._find_cycle()

def test_218():
    T = graphlib.TopologicalSorter()
    T.add(1, 2)
    T.prepare()
    T._find_cycle()

def test_252():
    T = graphlib.TopologicalSorter()
    T.add(1, 2)
    T.prepare()
    T.static_order()
