import collections
from typing import List

"""
Algorithm used: Tarjan's Algorithm

Tarjan's algorithm is based on depth first search (DFS). The vertices are indexed as they are traversed by DFS procedure. While returning from the recursion of DFS, every vertex V gets assigned a vertex L as a representative. L is a vertex with the least index that can be reach from V. Nodes with the same representative assigned are located in the same strongly connected component.

Complexity: O(|V| + |E|)

"""


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:

        # First create a graph of the available possible connections
        graph = collections.defaultdict(list)
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        return self.tarjan(graph, n)

    def tarjan(self, graph, n):
        # Initializing the arrays that are used to store the values
        visited = [False for _ in range(n)]  # used to check if a node has been visited
        ids = [
            0 for _ in range(n)
        ]  # Unique id for each node depending on its position in the dfs
        low = [
            0 for _ in range(n)
        ]  # Lowest possible id that the current node can achieve
        Id = 0

        bridge = []  # used to store the bridges

        for i in range(n):
            if not visited[i]:
                self.dfs(graph, n, i, -1, visited, ids, low, bridge, Id)

        return bridge

    def dfs(self, graph, n, node, parent, visited, ids, low, bridge, Id):
        visited[node] = True
        Id += 1
        ids[node] = Id
        low[node] = Id  # Initially the low = id of the current node

        for next_node in graph[node]:
            if (
                next_node == parent
            ):  # Handle the edge case: if the next node is the parent, do nothing
                continue
            if not visited[next_node]:
                self.dfs(graph, n, next_node, node, visited, ids, low, bridge, Id)
                low[node] = min(
                    low[node], low[next_node]
                )  # Evoked when recursively updating the low value

                if ids[node] < low[next_node]:
                    bridge.append([node, next_node])

            else:
                low[node] = min(low[node], ids[next_node])


sol = Solution()
n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
print(sol.criticalConnections(n, connections))

