#include <stack>
#include <vector>

class Solution {
public:
  int carFleet(int target, std::vector<int> &position,
               std::vector<int> &speed) {
    // the goal of this problem is to determine the number of car fleets
    //
    // a car fleet is defined as a "pack" of cars that are moving together, as
    // none can pass each other in a one-lane highway. so same position and same
    // speed
    //
    // the target describes how long the highway is
    // the position list describes how far along each car is
    // the velocity list describes how fast each car is respectively

    // start by packing together and sorting the positions and speeds
    std::vector<std::pair<int, int>> pos_speeds(position.size());
    for (std::size_t i = 0; i < position.size(); i++) {
      pos_speeds[i] = {position.at(i), speed.at(i)};
    }

    std::sort(pos_speeds.begin(), pos_speeds.end(), std::greater());

    // track the time that a fleet takes
    // time[i] = (target - position[i]) / speed[i]
    std::stack<float> s;

    for (const auto &[pos, sp] : pos_speeds) {
      float time = (target - pos) / static_cast<float>(sp);

      // if the current time is greater than the top, then that means the
      // current car is moving at a faster rate. join the two cars into a fleet.
      // NOTE: this is a no-op because we don't want to add any new times
      if (!s.empty() && time <= s.top()) {
        // s.pop();
      } else {
        s.push(time);
      }
    }

    return s.size();
  }
};
