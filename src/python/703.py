# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
import heapq
from typing import List


class KthLargest:
    # problem
    # design a class that returns the kth largest element when `add` is called
    #
    # definition
    # a heap is binary tree data structure that satisfies the heap property
    # the heap property says
    # 1. the value of its children is greater than or equal to its own value
    #    this means that the smallest or largest elements are at the top of the
    #    heap, depending on the application
    # 2. a heap is also a complete binary tree
    #    - the levels of the binary tree must be filled completely except the
    #    lowest level nodes which are filled leftmost as possible
    #    - the leaves have the same depth
    #
    # notes
    # - heaps are useful for implementing priority queues
    # - binary heaps are usually implemented using arrays
    #   the root is arr[0]
    #   the ith element is arr[(i-1)/2]
    #     the left child of the ith element is arr[(2*i)+1]
    #     the right child of the ith element is arr[(2*i)+2
    # - the traversal method for a heap is level-order
    #   this can be achieved using a queue structure

    def __init__(self, k: int, nums: List[int]):
        # track the kth element
        self.k = k

        # initialize the heap using the heapq module.
        # heapify is a helper function that sorts an array in O(n) time complexity
        # into the heap structure.
        #
        # the way that heapify works is by working backwards through the array
        # and swapping elements to satisfy the heap rules
        self.heap = nums
        heapq.heapify(self.heap)

        # maintain only the k largest elements - there will be performance issues
        # if we are carry around all the numbers
        # note that this will not do anything if
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # push the value onto the heap
        heapq.heappush(self.heap, val)

        # pushing that value may make the heap too large (more than k elements)
        # if so, we need to pop off the smallest element (min-heap property)
        #
        # NOTE: this is not >= because the kth number is 0 indexed
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # heap[0] is the smallest element (min-heap property)
        #
        # NOTE: this never throws an index bound because `val` will always add
        # an element to the heap. `k` is also a non-negative number
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
