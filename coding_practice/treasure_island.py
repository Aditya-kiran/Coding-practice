from collections import deque
from typing import List


class Solution:
    def treasure_island(self, grid: List[List[int]]) -> int:

        if grid[0][0] == "D" or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        steps = 0

        queue = deque()
        queue.append([0, 0, 0])
        grid[0][0] = "D"

        while queue:
            i, j, steps = queue.popleft()
            for di, dj in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= di < len(grid) and 0 <= dj < len(grid[0]):
                    if grid[di][dj] == "X":
                        return steps + 1
                    elif grid[di][dj] == "O":
                        grid[di][dj] = "D"
                        queue.append([di, dj, steps + 1])

    def treasure_island_2(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        queue = deque()
        seen = {()}
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] == "S":
                    queue.append([i, j, 0])
                    seen.add((i, j))
        while queue:
            # print(queue)

            i, j, steps = queue.popleft()

            # for row in grid:
            #     print(row)
            for di, dj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (
                    0 <= di < len(grid)
                    and 0 <= dj < len(grid[0])
                    and (di, dj) not in seen
                    and grid[di][dj] != "D"
                ):
                    if grid[di][dj] == "X":
                        return steps + 1
                    grid[di][dj] = "D"
                    queue.append([di, dj, steps + 1])
                    seen.add((di, dj))


sol = Solution()
grid = [
    ["O", "O", "O", "O"],
    ["D", "D", "D", "O"],
    ["O", "O", "O", "O"],
    ["X", "D", "D", "O"],
]
print(sol.treasure_island(grid))

grid_2 = [
    ["S", "O", "S", "D", "S"],
    ["D", "O", "D", "O", "D"],
    ["O", "O", "O", "O", "X"],
    ["X", "D", "D", "O", "O"],
    ["X", "D", "D", "D", "O"],
]

print(sol.treasure_island_2(grid_2))
