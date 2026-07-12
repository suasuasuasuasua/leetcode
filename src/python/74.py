class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # the matrix is organized like a 1d sorted list
        # we can imagine the matrix as a flattened list

        low = 0
        rows, cols = len(matrix), len(matrix[0])
        high = rows * cols - 1

        while low <= high:
            mid = low + (high - low) // 2
            # index into the proper row then column in the flat buffer
            # - do // first to get to the proper row
            # - do % to get to the proper column
            value = matrix[mid // cols][mid % cols]

            if value == target:
                return True
            elif value < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
