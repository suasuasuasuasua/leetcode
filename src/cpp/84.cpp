#include <iostream>
#include <stack>
#include <vector>

class Solution {
public:
  int largestRectangleArea(std::vector<int> &heights) {
    // use a monotonically ascending stack to find the largest left and
    // rightmost bounds possible
    //
    // a monotonically ascending stack looks like in histogram form
    //          []    <- can no longer be extended right (width=4-3, area=6*1)
    //          []       will be "extended into" by previous rectangles beause
    //          []       they must by definition be less than
    //       [] []    <- same here (width=4-2, area=3*2)
    //    [] [] [] []
    // [] [] [] [] []
    // 0  1  2  3  4
    std::stack<std::pair<std::size_t, int>> s;

    int area = 0;
    for (std::size_t i = 0; i < heights.size(); i++) {
      std::size_t start = i;
      int height = heights.at(i);

      // repeatedly pop off the stack while the current element is the smallest
      //
      // this means that the height can no longer be extended to the right, and
      // it should just be considered in isolation
      while (!s.empty() && height < s.top().second) {
        int width = i - s.top().first;
        area = std::max(area, s.top().second * width);
        // reset the new height's starting index to this (popped) height's index
        // NOTE: can't just increment an offset by -1 because the popped heights
        // are not necessarily in order
        start = s.top().first;
        s.pop();
      }

      s.push({start, height});
    }

    // these heights must have extended to the end of the histogram.
    //
    // the width is the difference between the length of the numbers array and
    // the index, while the height is simply the height value
    while (!s.empty()) {
      auto [idx, height] = s.top();
      auto width = heights.size() - idx;
      area = std::max(area, static_cast<int>(height * width));
      s.pop();
    }

    return area;
  }
};

int main(int argc, char *argv[]) {
  Solution s;
  using inputs_t = std::vector<int>;
  using outputs_t = int;
  std::vector<std::pair<inputs_t, outputs_t>> tests = {
      {{7, 1, 7, 2, 2, 4}, 8},
      {{2, 1, 5, 6, 2, 3}, 10},
      {{3, 6, 5, 7, 4, 8, 1, 0}, 20},
  };

  for (auto &[nums, expected] : tests) {
    if (s.largestRectangleArea(nums) == expected) {
      std::cout << "Pass" << std::endl;
    } else {
      std::cout << "Fail" << std::endl;
    }
  }

  return 0;
}
