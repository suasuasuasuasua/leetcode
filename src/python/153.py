class Solution:
    def findMin(self, nums: list[int]) -> int:
        # find the minimum element in a rotated array

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            value = nums[mid]

            # look in the right sublist and discard the left sublist
            # the array is sorted so we can make the following assumptions
            # - elements to right of any element must be larger; this hold for
            #   sorted rotated arrays
            # - we can also throw away the mid point along with the left
            #   sublist
            if value > nums[high]:
                low = mid + 1
            # look in the left sublist
            # note, the mid index is included. we eliminate the right sublist
            # because we know all those elements are greater than the
            # current mid point. this keeps `mid` in the window for future
            # consideration
            else:
                high = mid

        # at this point, we have converged on the low==high==min(nums)
        return nums[low]
