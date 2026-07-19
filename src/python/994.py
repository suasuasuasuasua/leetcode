from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0 is empty
        # 1 is fresh orange
        # 2 is rotten orange
        #
        # every minute, fresh oranges next to a rotten orange becomes rotten

        def is_in_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        queue = deque()
        n_fresh = 0
        # initially, add all rotten oranges to the queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    n_fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        minutes = 0
        while queue and n_fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                # check right, down, left, up
                right = row, col + 1
                down = row + 1, col
                left = row, col - 1
                up = row - 1, col
                for c_row, c_col in [right, down, left, up]:
                    # Ensure that A) the row/col is in bounds and is a fresh banana
                    if is_in_bounds(c_row, c_col) and grid[c_row][c_col] == 1:
                        # Replace with rotten and decrement the number of fresh bananas
                        grid[c_row][c_col] = 2
                        n_fresh -= 1
                        # Enqueue the new rotten banana
                        queue.append((c_row, c_col))

            # Increment the timestep
            minutes += 1

        return minutes if n_fresh == 0 else -1
