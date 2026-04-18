#include <cstddef>
#include <fmt/base.h>
#include <fmt/ranges.h>
#include <iostream>
#include <unordered_map>
#include <vector>

class Solution {
public:
  std::vector<int> twoSum(std::vector<int> &nums, int target) {
    // the trick to understand in two sum is that you can store the 'missing'
    // value as the key and the index as the value (or vice versa)
    std::unordered_map<int, int> m;
    std::vector<int> ret;

    for (int i = 0; i < nums.size(); i++) {
      int num = nums[i];
      if (m.contains(num)) {
        // NOTE: i is guaranteed to be greater than m[num]
        // since we're looping over the indices from 0 to N, m[num] must have
        // been inserted sooner
        ret = {m[num], static_cast<int>(i)};
      }
      int diff = target - num;
      m[diff] = i;
    }

    return ret;
  }
};

int main(int argc, char *argv[]) {
  Solution s;
  std::vector<std::pair<std::pair<std::vector<int>, int>, std::vector<int>>>
      tests = {
          {{{3, 4, 5, 6}, 7}, {0, 1}},
          {{{4, 5, 6}, 10}, {0, 2}},
          {{{5, 5}, 10}, {0, 1}},
      };

  for (auto &[test, expected] : tests) {
    auto &[nums, target] = test;
    auto result = s.twoSum(nums, target);
    fmt::print("{} == {}? ", result, expected);

    if (result == expected) {
      std::cout << "Pass" << "\n";
    } else {
      std::cout << "Fail" << "\n";
    }
  }

  return 0;
}
