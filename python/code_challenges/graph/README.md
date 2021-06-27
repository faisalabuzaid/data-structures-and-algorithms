# Graphs

How to impelment the graph.

## Challenge

A graph is a pictorial representation of a set of objects where some pairs of objects are connected by links. The interconnected objects are represented by points termed as vertices, and the links that connect the vertices are called edges. The various terms and functionalities associated with a graph is described in great detail in our tutorial here. In this chapter we are going to see how to create a graph and add various data elements to it using a python program. Following are the basic operations we perform on graphs.


## Approach & Efficiency

- Step-by-step BFS traversal
    - 1 - Add a node/vertex from the graph to a queue of nodes to be “visited”.
    - 2 - Visit the topmost node in the queue, and mark it as such.
    - 3 - If that node has any neighbors, check to see if they have been “visited” or not.
    - 4 - Add any neighboring nodes that still need to be “visited” to the queue.
    - 5 - Remove the node we’ve visited from the queue.

BFS traversal

- Time compexity: O(n+m)
- Space Complexity: O(n)

## API

- Display graph vertices
- Display graph edges
- Add a vertex
- Add an edge
- Creating a graph

## White Board For BFS

![](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/master/whiteboards/binary_tree-breadth_first.jpg)