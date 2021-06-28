from code_challenges.graph_business_trip.graph_business_trip import Graph, search_flight
import pytest

@pytest.fixture
def my_graph():
    g = Graph()
    
    g.add_vertex('amman')
    g.add_vertex('irbid')
    g.add_vertex('zarqa')
    g.add_vertex('aqaba')
    g.add_edge('amman', 'irbid', 30)
    g.add_edge('irbid', 'amman', 30)
    g.add_edge('irbid', 'zarqa', 15)
    g.add_edge('zarqa', 'irbid', 15)
    g.add_edge('irbid', 'aqaba', 90)
    g.add_edge('aqaba', 'irbid', 90)

    return g

def test_two_cities(my_graph):
    actual = search_flight(my_graph,['irbid', 'amman'])
    expected = f'{True}, {30}$'
    assert actual == expected

def test_three_cities(my_graph):
    actual = search_flight(my_graph,['amman', 'irbid', 'zarqa'])
    expected = f'{True}, {45}$'
    assert actual == expected

def test_wrong_city(my_graph):
    actual = search_flight(my_graph,['tafila'])
    expected = f'{False}, {0}$'
    assert actual == expected

def test_wrong_route(my_graph):
    actual = search_flight(my_graph,['aqaba', 'amman'])
    expected = f'{False}, {0}$'
    assert actual == expected

