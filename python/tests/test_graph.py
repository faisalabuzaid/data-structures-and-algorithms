from code_challenges.graph.graph import Graph
import pytest

@pytest.fixture
def my_graph():
    g = Graph()
    
    g.add_vertex('10')
    g.add_vertex('5')
    g.add_vertex('9')
    g.add_vertex('44')
    g.add_edge('10', '5', 3)
    g.add_edge('10', '10', 6)
    g.add_edge('5', '44', 2)
    g.add_edge('44', '9', 4)
    g.add_edge('44', '10', 1)
    g.add_edge('5', '10', 7)
    g.add_edge('9', '10', 8)

    return g

def test_add_node(my_graph):
    actual = my_graph.add_vertex('20')
    expected = '20'
    assert actual.value == expected

def test_get_nodes(my_graph):
    actual = my_graph.get_vertices()
    expected = ['10', '5', '9', '44']
    assert actual == expected

def test_edges(my_graph):
    actual = my_graph.get_neighbors('10')
    expected = [['5', 3], ['10', 6]]
    assert actual == expected

def test_grapgh_size(my_graph):
    actual = my_graph.size()
    expected = 4
    assert actual == expected

def test_one_vertex():
    g = Graph()
    g.add_vertex('20')
    actual = g.get_vertices()
    expected = ['20']
    assert actual == expected

def test_empty_grapgh():
    g = Graph()
    actual = g.get_vertices()
    expected = None
    assert actual == expected

def test_breadth_first(my_graph):
    actual = my_graph.breadth_first('10')
    expected = ['10', '5', '44', '9']
    assert actual == expected