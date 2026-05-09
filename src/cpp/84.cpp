#include <iostream>
#include <stack>
#include <vector>

class Solution {
public:
  int largestRectangleArea(std::vector<int> &heights) {
    // the largest rectangle can be calculated in two ways
    //
    // 1. it is either going to be the largest value in the array
    // 2. or, it's going to be a rectangle spanned over the bars

    // use a monotonically ascending stack to find the largest left and
    // rightmost bounds possible
    std::stack<int> s;

    int area = 0;
    for (int height : heights) {
      // use the height of the bar as the area
      area = std::max(area, height);

      // create temporary stack to iterate through
      std::stack<int> temp_s(s);

      // look left as far back as we can to construct the width
      int width = 1;
      int temp_height = height; // init as current height
      while (!temp_s.empty()) {
        int prev_height = temp_s.top();
        // use smaller and smaller heights if encountered
        if (prev_height < temp_height) {
          temp_height = prev_height; // attempt constructing off previous height
        }
        temp_s.pop();
        width++;
        // attempt to get a higher area
        area = std::max(area, temp_height * width);
      }

      s.push(height);
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
