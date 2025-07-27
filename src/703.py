# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
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
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int: ...


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
