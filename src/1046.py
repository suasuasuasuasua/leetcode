# https://leetcode.com/problems/last-stone-weight/
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # problem
        # given a list of stones, we play a game where we pick the _two_ largest
        # stones from the list and smash them together (where x <= y)
        # if x == y, then the stones are destroyed
        # else, x is destroyed and the stone now has a new weight y-x
        #
        # quirks
        # python provides a heap implementation, but this is specifically a
        # min-heap implementation
        #
        # one solution online suggests negating all the values to simulate the
        # min-heap property
        #
        # solution
        # first, we should transform the list of stones into a heap structure
        # - this can be done using the heapq.heapify() function
        # next, we should perform a loop while the list of stones are greater
        # than or equal to 2.
        # finally, we should check if there is a stone left
        # - if there is, then return the weight
        # - else 0
        #
        # transform the stones array into a heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            # the first pop will give the largest stone
            # since y should be larger than x, y is the first one
            y = heapq.heappop(stones)
            # second pop will give the second largest stone
            x = heapq.heappop(stones)

            # if the weights of the stones are different, push the new smaller
            # stone
            if x != y:
                diff = y - x
                heapq.heappush(stones, diff)

        # negate the result since we transformed the data
        return -heapq.heappop(stones) if stones else 0
