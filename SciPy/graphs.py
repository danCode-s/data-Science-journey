from scipy.sparse.csgraph import bellman_ford
import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr_0 = np.array([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])

newarr = csr_matrix(arr_0)

# Dijkstra
'''

Use the dijkstra method to find the shortest path in a graph from one element to another.

It takes following arguments:

return_predecessors: boolean (True to return whole path of traversal otherwise False).
indices: index of the element to return all paths from that element only.
limit: max weight of path.
'''

# print(dijkstra(newarr, return_predecessors=True, indices=0))

'''
Floyd Warshall
Use the floyd_warshall() method to find shortest path between all pairs of elements.

'''

# print(floyd_warshall(newarr, return_predecessors=True))

'''
Bellman Ford
The bellman_ford() method can also find the shortest path between all pairs of elements, but this method can handle negative weights as well.

'''

arr_1 = np.array([
    [0, -1, 2],
    [1, 0, 0],
    [2, 0, 0]
])

newarr_1 = csr_matrix(arr_1)

print(bellman_ford(newarr_1, return_predecessors=True, indices=0))


# depth first order

'''
The depth_first_order() method returns a depth first traversal from a node.

This function takes following arguments:

the graph.
the starting element to traverse graph from.
'''

arr_2 = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr_2 = csr_matrix(arr_2)
print(depth_first_order(newarr_2, 1, 1))


'''
The breadth_first_order() method returns a breadth first traversal from a node.

This function takes following arguments:

the graph.
the starting element to traverse graph from.
'''

print(breadth_first_order(newarr_2, 1, 1))