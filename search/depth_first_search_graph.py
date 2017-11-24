# --*-- coding:utf-8 --*--

"""
Depth First Search
    ------------------
    Recursive implementation of the depth first search algorithm used to
    traverse trees or graphs. Starts at a selected node (root) and explores the
    branch as far as possible before backtracking.

connect graph:
Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree.
The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again.
To avoid processing a node more than once, we use a boolean visited array.

For example, in the following graph, we start traversal from vertex 2.
When we come to vertex 0, we look for all adjacent vertices of it. 2 is also an adjacent vertex of 0.
If we don’t mark visited vertices, then 2 will be processed again and it will become a non-terminating process.
A Depth First Traversal of the following graph is 2, 0, 1, 3.

disconnect graph:
must call dfsutil for every vertex, before doing so,check if it is printed by other dfsutil


application:
Breadth-first search can be used to solve games where a series of choices result in either a winning or losing state.
 For example, BFS can help a player determine a winning sequence of moves for solving a Rubik's cube.

BFS is also used in the famous Dijkstra’s algorithm for computing the
shortest path in a graph and the Ford-Fulkerson algorithm for computing the maximum​ flow in a flow network.

Time Complexity: O(E + V)
        E = Number of edges
        V = Number of vertices (nodes)
"""


from collections import defaultdict

#region method1
class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, node, data):
        self.graph[node].append(data)

    def dfsutil(self, node, visited):
        visited[node] = True
        print (node)

        for n in self.graph[node]:
            if visited[n] == False:
                self.dfsutil(n, visited)

    def dfs_connecting(self, v):
        """
        for connectiing graph
        :param v:
        :return:
        """
        visited = [False]*len(self.graph)
        self.dfsutil(v, visited)

    def dfs_disconnectiing(self, v):
        """
        for disconnecting graph
        :param v:
        :return:
        """
        lenofgraph = len(self.graph)
        visited = [False]*lenofgraph
        for i in range(lenofgraph):
            if visited[i] == False:
                self.dfsutil(i, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.dfs_disconnectiing(2)
#endregion method1

#region method 2
def dfs_iterative(graph, start):
    """
    non recursive depth first search
    :param graph:
    :param start:
    :return:
    """
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path


adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

print(dfs_iterative(adjacency_matrix, 1))


def dfs_recursive(graph, vertex, path=[]):
    """
    recursive depth first search
    :param graph:
    :param vertex:
    :param path:
    :return:
    """
    path += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)

    return path


adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

print(dfs_recursive(adjacency_matrix, 1))
# [1, 2, 4, 6, 7, 5, 3]
# [1, 3, 5, 6, 7, 2, 4]
#endregion method 2
