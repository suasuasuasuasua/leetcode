#include <cctype>
#include <cstdlib>
#include <fmt/ranges.h>
#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
  static constexpr std::string START_TOKEN = "<begin>";
  static constexpr std::string END_TOKEN = "<end>";

  std::string encode(std::vector<std::string> &strs) {
    // encoding the string should be reversible
    std::string ret;

    // use the <begin> and <end> tag to delimit and the length of the string for
    // the decoder to know how far to stop reading
    for (const auto &s : strs) {
      ret += std::to_string(s.size()) + START_TOKEN + s + END_TOKEN;
    }

    return ret;
  }

  std::vector<std::string> decode(std::string s) {
    std::vector<std::string> ret;

    std::size_t i = 0;
    while (i < s.size()) {
      // try to find the start token to determine the size of the number
      int j = i;
      while (s.substr(j, START_TOKEN.size()) != START_TOKEN) {
        j++;
      }

      // form the number using the length of the number
      auto c_len = j - i;
      auto c_num =
          std::stoi(s.substr(i, c_len)); // could throw exceptions but meh
      // look ahead c_num characters for special delimiter (<end>)
      std::string inner_s = s.substr(i + c_len + START_TOKEN.size(), c_num);
      ret.push_back(inner_s);
      i = j + START_TOKEN.size() + c_num + END_TOKEN.size();
    }
    return ret;
  }
};

int main(int argc, char *argv[]) {
  Solution s;
  using inputs_t = std::vector<std::string>;
  std::vector<inputs_t> tests = {
      {"Hello", "World"},
      {"abc123", "456def"},
      {"0"},
      {"we", "say", ":", "yes", "!@#$%^&*()"},
  };

  for (auto &test : tests) {
    auto result = s.encode(test);
    auto result_back = s.decode(result);

    fmt::println("Result Encode: {}", result);
    fmt::println("Result Decode: {}", result_back);

    if (result_back == test) {
      std::cout << "Pass" << "\n";
    } else {
      std::cout << "Fail" << "\n";
    }
  }

  return 0;
}
