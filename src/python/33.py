class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # nums is sorted in ascending order (distinct values)
        # left rotated by some unknown index

        result = -1

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            value = nums[mid]

            # if we find the target, then return it straight up
            if value == target:
                result = mid
                break

            # determine which half of the list is sorted
            # the left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                # the right half is sorted
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return result
