from typing import List
import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # map each point to its euclidean distance
        heap = list()
        for point in points:
            x, y = point
            dist = math.sqrt(x**2 + y**2)
            # store the negative distance to maintain a maximum heap
            heapq.heappush(heap, (-dist, point))

        # pop until k remaining
        while len(heap) > k:
            heapq.heappop(heap)

        return [v for _, v in heap]
