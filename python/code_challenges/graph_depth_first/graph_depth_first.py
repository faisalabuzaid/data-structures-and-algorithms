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

    def dfs(self,graph, source, path=[]):
        if source not in path:
            path.append(source)
            if source not in graph:
                return path
            for neighbor in graph[source]:
                path = self.dfs(graph, neighbor, path)
        return path
    
if __name__ == "__main__":
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
    
    print(g.size())
    print(g.get_vertices())
    print(g.get_neighbors('10'))
    print(g.breadth_first("5"))

    graph2 = {"A": ["B", "C",'G','D',"E",'H',"F"],
                "B": ['C','G'],
                "C": ["G"],
                "D": ['E','H','F'],
                "E": ["D"],
                "F": ['H'],
                "H": ["D"],
                "G":["C"],
                }
    path = g.dfs(graph2, "A")
    print(path)
