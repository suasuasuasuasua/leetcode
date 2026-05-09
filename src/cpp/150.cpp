#include <functional>
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
  int evalRPN(std::vector<std::string> &tokens) {
    // the problem asks us to implement a reverse polish notation calculator.
    //
    // the natural answer is to use a stack, which tracks operands as the newest
    // elements, and the operators can be used as evaluations
    std::stack<int> s;
    // NOTE: function syntax is std::function<return_type(param_type, ...)>>
    std::unordered_map<std::string, std::function<int(int, int)>> ops = {
        {"+", std::plus()}, // from std::functional
        {"-", std::minus()},
        {"*", std::multiplies()},
        {"/", std::divides()},
    };

    for (const auto &token : tokens) {
      // if we encounter an operator, then evaluate
      if (ops.contains(token)) {
        int first, second, result;
        // NOTE: the first operand comes before the second operand in the stack
        second = s.top();
        s.pop();
        first = s.top();
        s.pop();
        // use the mapping to evaluate the intermediate expression
        result = ops.at(token)(first, second);
        s.push(result);
      } else {
        // description says we will always get a valid RPN expression, so no
        // need to catch exceptions
        int num = std::stoi(token);
        s.push(num);
      }
    }

    // there should only be one element left
    return s.top();
  }
};
