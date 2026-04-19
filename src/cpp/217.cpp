#include <iostream>
#include <unordered_set>
#include <vector>

class Solution {
public:
  // the duplicates can be filtered out using a set.
  // by definition, a set contains only unique elements, so if we were to find
  // another element that was already in the set, then it must be a duplicate
  bool hasDuplicate(std::vector<int> &nums) {
    std::unordered_set<int> unique_nums;
    for (const auto &n : nums) {
      if (unique_nums.contains(n)) {
        return true;
      }
      unique_nums.insert(n);
    }
    return false;
  }
};

int main(int argc, char *argv[]) {
  Solution s;
  using inputs_t = std::vector<int>;
  using outputs_t = bool;
  std::vector<std::pair<inputs_t, outputs_t>> tests = {
      {{1, 2, 3, 3}, true},
      {{1, 2, 3, 4}, false},
  };

  for (auto &[nums, expected] : tests) {
    if (s.hasDuplicate(nums) == expected) {
      std::cout << "Pass" << std::endl;
    } else {
      std::cout << "Fail" << std::endl;
    }
  }

  return 0;
}
