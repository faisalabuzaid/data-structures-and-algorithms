import collections

class Node:
    def __init__(self, value):
        self.value = value
class Graph:
    def __init__(self):
        """
        This is the constructor method of a graph
        """
        self._adjacency_list = {}

    def add_vertex(self, value):
        """
        This method is to add vertex to a graph
        """
        vertex = Node(value)
        if value in self._adjacency_list:
            print('Vertex',value,' already exists')
        self._adjacency_list[vertex.value] = []
        return vertex
      

    def add_edge(self, start_vertex, end_vertex, weight=1):
        """
        This method is to add edge to a graph
        """
        if start_vertex in self._adjacency_list.keys() and end_vertex in self._adjacency_list.keys():       
            temp = [end_vertex, weight]
            self._adjacency_list[start_vertex].append(temp)
            return
        
        raise KeyError('Key Not Found')

    def get_vertices(self):
        """
        This method to return vertexs
        """
        vertices = []
        for vertex in self._adjacency_list.keys():
            vertices .append(vertex)
        if len(vertices) > 0:
            return vertices
        return None
                

    def get_neighbors(self, vertex):
        """
        This method is to return neighbors
        """
        ni = []
        for edges in self._adjacency_list[vertex]:
            ni.append([edges[0], edges[1]])
        return ni
        

    def size(self):
        """
        This method to return size of graph
        """
        return len(self._adjacency_list)

    def breadth_first(self, root):
 
        visited = set()
        queue = collections.deque([root])
        result = []

        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            vertex = queue.pop()
            result.append(vertex)
            visited.add(vertex)
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for neighbour in self._adjacency_list[vertex]:
                if neighbour[0] not in visited:
                    visited.add(neighbour[0])
                    queue.append(neighbour[0])
        return result

def search_flight(graph, lst):
    cost = 0
    flag = False
    for i in range(len(lst)-1):
        if lst[i] in graph.get_vertices():
            for nieghbor in graph.get_neighbors(lst[i]):
                if lst[i+1] == nieghbor[0]:
                    flag = True
                    cost += nieghbor[1]
    return f'{flag}, {cost}$'

    
if __name__ == "__main__":
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

 
    print(search_flight(g,['irbid', 'amman']))
