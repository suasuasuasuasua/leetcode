#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
  bool isAnagram(std::string s, std::string t) {
    // t is only an anagram of s if t can be written using the letters from s
    // we care about the character frequencies in particular
    std::unordered_map<char, int> s_freq, t_freq;

    for (const auto &c : s) {
      s_freq[c]++;
    }
    for (const auto &c : t) {
      t_freq[c]++;
    }

    return s_freq == t_freq;
  }
};

int main(int argc, char *argv[]) {
  Solution s;
  using inputs_t = std::pair<std::string, std::string>;
  using outputs_t = bool;
  std::vector<std::pair<inputs_t, outputs_t>> tests = {
      {{"s", "nagaram"}, false},
      {{"rat", "car"}, false},
  };

  for (auto &[strs, expected] : tests) {
    auto &[s1, s2] = strs;
    if (s.isAnagram(s1, s2) == expected) {
      std::cout << "Pass" << std::endl;
    } else {
      std::cout << "Fail" << std::endl;
    }
  }

  return 0;
}
