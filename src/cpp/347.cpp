#include <fmt/base.h>
#include <fmt/ranges.h>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

class Solution {
public:
  std::vector<int> topKFrequent(std::vector<int> &nums, int k) {
    // find the k most frequent elements in the array by
    // 1. constructing the frequency mapping
    // 2. creating a heap structure to track the k elements with the highest
    // frequency
    //    - the heap is the perfect data structure because it can efficiently
    //    track the smallest or largest elements
    //      - the heap only needs a comparison operator, so we can pass in
    //      std::pair just fine
    //      - in C++, this is done using std::make_heap or with the
    //      std::priority_queue
    //    - a naiive approach is to use the max heap, but a performance
    //    optimization here is to use a min heap and only track k elements
    // 3. loop over the heap structure to get the elements with the highest
    // frequency
    std::unordered_map<int, int> num_freq;
    for (const auto &num : nums) {
      num_freq[num]++;
    }

    // maintain a max-heap of size k
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>,
                        std::greater<std::pair<int, int>>>
        heap;
    for (const auto &[num, freq] : num_freq) {
      heap.emplace(freq, num); // define heap by frequency, not number itself
      // this step is important for performance reasons if k is a large number
      // no need to carry around n numbers when we only care about k
      if (heap.size() > k) {
        heap.pop();
      }
    }

    // the heap is size k, and the elements are sorted in min-heap fashion
    // since the order of the elements returned doesn't matter, just pop off all
    // k elements
    std::vector<int> k_largest(k);
    for (int i = 0; i < k; i++) {
      auto [freq, value] = heap.top();
      heap.pop(); // remember to delete the element
      k_largest[i] = value;
    }
    return k_largest;
  }
};

int main(int argc, char *argv[]) {
  Solution s;
  using inputs_t = std::pair<std::vector<int>, int>;
  using outputs_t = std::vector<int>;
  std::vector<std::pair<inputs_t, outputs_t>> tests = {
      {{{1, 2, 2, 3, 3, 3}, 2}, {2, 3}},
      {{{1, 1, 1, 2, 2, 3}, 2}, {2, 1}},
      {{{1, 1, 1, 2, 2, 2, 3, 3, 3}, 3}, {1, 2, 3}},
      {{{7, 7}, 1}, {7}},
  };

  for (auto &[test, expected] : tests) {
    auto &[nums, target] = test;
    auto result = s.topKFrequent(nums, target);

    fmt::println("Result: {}", result);
    if (result == expected) {
      std::cout << "Pass" << "\n";
    } else {
      std::cout << "Fail" << "\n";
    }
  }

  return 0;
}
