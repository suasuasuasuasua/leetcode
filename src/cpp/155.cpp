#include <stack>

class MinStack {
  // the problem asks us to define a MinStack class that supports the following
  // methods
  //
  // each function should run in O(1) time
public:
  MinStack() {}

  void push(int val) {
    // the data stack always get the value as is
    data.push(val);

    // the min stack only takes the minimum values between the new `val` and
    // what is already on top
    if (min_stack.empty()) {
      min_stack.push(val);
    } else {
      int min_val = std::min(val, min_stack.top());
      min_stack.push(min_val);
    }
  }

  void pop() {
    data.pop();
    min_stack.pop();
  }

  // return from the real stack
  int top() { return data.top(); }

  // return from the min stack
  int getMin() { return min_stack.top(); }

private:
  // the data stack simply tracks the data going in and out
  std::stack<int> data;
  // the min stack specifically tracks the minimum data at any point in the
  // data stack. it's like storing a history for the data stack at each point
  std::stack<int> min_stack;
};
