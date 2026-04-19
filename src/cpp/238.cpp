#include <algorithm>
#include <fmt/base.h>
#include <fmt/ranges.h>
#include <iostream>
#include <vector>

class Solution {
public:
  std::vector<int> productExceptSelf(std::vector<int> &nums) {
    // the idea behind product except self is that we can calculate running
    // products for each number in nums
    //
    // - the prefix array tracks the product of all numbers before the current
    // index
    // - the suffix array tracks the product of all numbers after the current
    // index
    //
    // at the very end, we can just multiply the prefix and suffix arrays at
    // each index
    //
    // some pitfalls i had were
    // - off-by-one errors when constructing the loops. be careful of the
    // reverse loop
    // - simplify the loop by just setting all the elements equal to 1 at the
    // start
    // - i attempted doing the division strategy, but i was being thrown off by
    // the zeros. i was able to calculate the product, but the division step was
    // tricky. for that one, we can consider three cases
    //   1. if there are no zeros, then we can just divide the product by the
    //   number
    //   2. if there is one zero, then only the index with the zero has a
    //   non-zero number. at each other number, they would necessarily have to
    //   multiply by 0
    //   3. if there is more than one zero, then all the numbers will be zero
    std::vector<int> ret;
    ret.reserve(nums.size());

    std::vector<int> prefixes(nums.size(), 1);
    // skip first element (no prefix)
    for (int i = 1; i < nums.size(); i++) {
      // use the previously calculated numbers
      int prefix = nums[i - 1] * prefixes[i - 1];
      prefixes[i] = prefix;
    }

    std::vector<int> suffixes(nums.size(), 1);
    // skip last element (no suffix)
    for (int i = nums.size() - 2; i >= 0; i--) {
      // use the previously calculated numbers
      int suffix = nums[i + 1] * suffixes[i + 1];
      suffixes[i] = suffix;
    }

    // combine the prefix and suffix terms
    std::transform(prefixes.begin(), prefixes.end(), suffixes.begin(),
                   std::back_inserter(ret),
                   [](int prefix, int suffix) { return prefix * suffix; });

    return ret;
  }
};

int main(int argc, char *argv[]) {
  Solution s;

  std::vector<std::pair<std::vector<int>, std::vector<int>>> tests = {
      {{1, 2, 3, 4}, {24, 12, 8, 6}},
      {{-1, 1, 0, -3, 3}, {0, 0, 9, 0, 0}},
      {{1, 2, 4, 6}, {48, 24, 12, 8}},
      {{-1, 0, 1, 2, 3}, {0, -6, 0, 0, 0}},
  };

  for (auto &[nums, expected] : tests) {
    if (s.productExceptSelf(nums) == expected) {
      std::cout << "Pass" << std::endl;
    } else {
      std::cout << "Fail" << std::endl;
    }
  }
  return 0;
}
