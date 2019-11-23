import collections
from typing import List

"""
Problem statement: 
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Algorithm: bfs and dfs methods=

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        dfs = True
        if dfs:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == "1":
                        self.dfs(grid, i, j)
                        count += 1
            return count
        else:
            queue = []
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == "1":
                        grid[i][j] = "#"
                        queue.append([i, j])
                        self.bfs(grid, queue)
                        count += 1
            return count

    def bfs(self, grid, queue):
        while queue:
            i, j = queue.pop(0)
            for x in (-1, 1):
                if 0 <= i + x < len(grid) and grid[i + x][j] == "1":
                    grid[i + x][j] = "#"
                    queue.append((i + x, j))
                if 0 <= j + x < len(grid[0]) and grid[i][j + x] == "1":
                    grid[i][j + x] = "#"
                    queue.append((i, j + x))

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "#"
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


grid = [
    ["1", "1", "0", "1", "0"],
    ["0", "0", "0", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "1", "0", "0", "1"],
]
obj = Solution()
print(obj.numIslands(grid))

