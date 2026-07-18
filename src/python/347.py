from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a hash map to determine the frequency of each number
        num_freq = Counter(nums)
        freq_num = [(v, k) for k, v in num_freq.items()]

        # use a heap to get the first k most frequent numbers
        res = [v for (_, v) in heapq.nlargest(k, freq_num)]
        return res
