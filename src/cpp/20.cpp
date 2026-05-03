#include <stack>
#include <string>
#include <unordered_map>

class Solution {
public:
  bool isValid(std::string s) {
    // in this problem, we are checking if a string of parenthesis is valid
    // - every opening ( has a closing )
    // - every opening { has a closing }
    // - every opening [ has a closing ]
    // moreover, open brackets are closed in the correct order

    std::stack<char> st;
    std::unordered_map<char, char> paren_mapping = {
        {')', '('},
        {'}', '{'},
        {']', '['},
    };

    for (const auto &c : s) {
      char prev;
      switch (c) {
      case '(':
      case '[':
      case '{':
        st.push(c); // push all opening parens
        break;
      case ')':
      case ']':
      case '}':
        char corres = paren_mapping[c];
        if (!st.empty() && st.top() == corres) {
          st.pop(); // pop the opening paren only if the current paren matches
        } else {
          return false;
        }
        break;
      }
    }

    // the stack must be empty at the end to be resolved
    return st.empty();
  }
};
