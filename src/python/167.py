class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # 1-indexed array of integers `numbers`
        #   sorted in non-decreasing
        #   so ascending? but sometimes not ascending if has duplicate numbers
        # find two numbers, index1 and index2, that add up to a specific target number
        #
        # return the indices of the two numbers, each incremented by one

        left, right = 0, len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            # if the running sum is smaller, then the only way to make the sum bigger is the move the left pointer right, since only bigger numbers exist to the right
            elif curr_sum < target:
                left += 1
            # else if the running sum is bigger than the target, then the only way to make the sum smaller is by moving the right pointer left
            else:
                right -= 1
