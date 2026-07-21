class Solution:
    def climbStairs(self, n: int) -> int:
        # it takes n steps to get to the top of the staircase
        # each unit of time, we can climb 1 or 2 steps
        #
        # how many distinct ways can we climb to the top of the staircase?
        if n == 1:
            return 1

        ways = [1] * n
        # there is only one way to get to step 0 (1 step)
        ways[0] = 1
        # there are two ways to get to step 1 (1 + 1 steps or 2 steps)
        ways[1] = 2

        # we should think about solving this problem using the recurrence
        # relation (induction). the number of ways is a sum of the two previous
        # cache results
        # ways(n) = ways(n-1) + ways(n-2)
        for i in range(2, n):
            # ways[i-1] encodes which paths must end in 1 step
            # ways[i-2] encodes which paths must end in 2 steps
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[-1]
