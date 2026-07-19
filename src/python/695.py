from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def is_in_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[row])

        visited = set()

        def dfs(row, col):
            if not is_in_bounds(row, col):
                return 0
            if (row, col) in visited:
                return 0
            if grid[row][col] == 0:
                return 0

            visited.add((row, col))
            ret = (
                1
                + dfs(row, col + 1)
                + dfs(row + 1, col)
                + dfs(row, col - 1)
                + dfs(row - 1, col)
            )
            return ret

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == 1:
                    result = max(result, dfs(i, j))

        return result
