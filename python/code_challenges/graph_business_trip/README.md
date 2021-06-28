# Graph Bussiness Trip


Write a function called business trip takes two arguments: graph, array of city names, and return: cost or null.

## White Board

![](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/master/whiteboards/binary_tree-breadth_first.jpg)

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

## Solution

- Display graph vertices
- Display graph edges
- Add a vertex
- Add an edge
- Creating a graph

