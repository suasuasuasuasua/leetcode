from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # an island is connected by adjacent land horizontally or vertically
        def is_in_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        visited = set()

        def dfs(row, col):
            if (row, col) in visited:  # already seen this point
                return
            elif not is_in_bounds(row, col):  # out of bounds
                return
            elif grid[row][col] != "1":  # not an island
                return

            # mark the coordinate as visited so we don't look here again
            visited.add((row, col))
            # move up, right, down, left recursively
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row + 1, col)
            dfs(row, col - 1)

        # return the number of islands
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # if we haven't seen the cell yet and if the grid is an island
                if (i, j) not in visited and grid[i][j] == "1":
                    result += 1
                    dfs(i, j)
        return result
