class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1

        # try to find the biggest heights on the left and right
        area = 0
        while left < right:
            left_num = height[left]
            right_num = height[right]

            # height * width
            new_area = min(left_num, right_num) * (right - left)
            area = max(area, new_area)

            # if the left number is smaller than the right number, then we
            # should advance the left pointer to try to find a larger base
            # height
            # if the heights are equal, then moving either pointer is fine
            if left_num <= right_num:
                left += 1
            # else, we should decrease the right pointer to try to find a larger
            # base height
            else:
                right -= 1

            # in either case, the width of the area shrinks

        return area
