from typing import List


class Solution:
    def dfs(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])

        zombie = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        human = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 0}

        timer = 0
        while human:
            if not zombie:
                return 0

            zombie = {
                (i + di, j + dj)
                for i, j in zombie
                for (di, dj) in [(0, 1), (1, 0), (0, -1), (-1, 0)]
                if (i + di, j + dj) in human
            }
            human -= zombie
            timer += 1
        return timer


sol = Solution()
grid = [[0, 1, 1, 0, 1], [0, 1, 0, 1, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0]]
print(sol.dfs(grid))
