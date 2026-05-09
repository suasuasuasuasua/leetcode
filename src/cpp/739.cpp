#include <stack>
#include <vector>

class Solution {
public:
  // Input: temperatures = [30,38,30,36,35,40,28]
  // Output: [1,4,1,2,1,0,0]
  //
  // Input: temperatures = [22,21,20]
  // Output: [0,0,0]
  std::vector<int> dailyTemperatures(std::vector<int> &temperatures) {
    // given an array of temperatures, return the number of days that the
    // particular day's temperature is higher than future days
    std::vector<int> result(temperatures.size(), 0);
    // the trick is to use a stack to track the indexes in the temperatures
    // - this particular stack is called "monotonic" meaning that it either
    // strictly increases/decreases (or stays the same) in value
    //
    // the element at the top of the stack will be repeatedly "diffed" against
    // the current element
    // - if the current element is larger, then take the difference in index
    // values. this essentially counts how many elements must have been smaller
    // before encountering the larger element
    // - else, continue on and add the current index+element to the stack
    std::stack<std::pair<int, int>> s;

    for (std::size_t i = 0; i < temperatures.size(); i++) {
      int cur_temp = temperatures.at(i);
      // repeatedly pops off the stack while the current element is the largest
      while (!s.empty() && cur_temp > s.top().second) {
        result.at(s.top().first) = i - s.top().first;
        s.pop();
      }

      s.push({static_cast<int>(i), cur_temp});
    }

    return result;
  }
};
