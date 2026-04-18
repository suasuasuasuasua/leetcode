#include <cctype>
#include <fmt/base.h>
#include <fmt/ranges.h>
#include <iostream>
#include <map>
#include <string>
#include <vector>

class Solution {
public:
  std::vector<std::vector<std::string>>
  groupAnagrams(std::vector<std::string> &strs) {
    // anagrams must sure all the same characters and frequencies
    // the trick to this problem is creating the hash index out of an fixed size
    // array
    // - my incomplete solution was trying to use the std::unordered_map for the
    // overall container and for the key
    // - the reason why this doesn't work is because the std::unordered_map is
    // not hashable and is thus not a valid key. moreover, it may not be a good
    // key anyway since operator< is not guaranteed to work in all situations. a
    // simple std::string or std::array is guaranteed to work
    // - in C++, std::map is a red-black binary tree and only needs operator< to
    // be defined
    std::vector<std::vector<std::string>> ret;
    std::map<std::array<int, 26>, std::vector<std::string>> mappings;

    // break down each string to the map
    for (const auto &s : strs) {
      std::array<int, 26> counter{0};
      for (const auto &c : s) {
        int idx = std::tolower(c) - 'a';
        counter[idx]++;
      }

      mappings[counter].push_back(s);
    }

    for (const auto &[_, v] : mappings) {
      ret.push_back(v);
    }

    return ret;
  }
};

int main(int argc, char *argv[]) {
  Solution s;
  std::vector<std::pair<std::vector<std::string>,
                        std::vector<std::vector<std::string>>>>
      tests = {
          {{"act", "pots", "tops", "cat", "stop", "hat"},
           {{"pots", "tops", "stop"}, {"hat"}, {"act", "cat"}}},
          {{"x"}, {{"x"}}},
          {{""}, {{""}}},
      };

  for (auto &[test, expected] : tests) {
    auto result = s.groupAnagrams(test);
    if (result == expected) {
      std::cout << "Pass" << std::endl;
    } else {
      std::cout << "Fail" << std::endl;
    }
  }

  return 0;
}
