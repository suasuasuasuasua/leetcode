#include <unordered_set>
#include <vector>

class Solution {
public:
  int longestConsecutive(std::vector<int> &nums) {
    // the problem is to find the longest consecutive sequence in an array of
    // numbers.
    //
    // the sequence does not have to be contiguous.
    // **the sequence does not have to appear in order like the original array**
    // elements in the sequence must be +1 larger than the previous.
    int longest = 0;

    // convert to a set so we have fast lookup times
    std::unordered_set<int> numSet(nums.begin(), nums.end());

    for (int n : numSet) {
      // find the start of a sequence
      if (numSet.contains(n - 1)) {
        continue;
      }

      // scan through the set of numbers to find the next and next and next
      int running = 1;
      while (numSet.contains(n + running)) {
        running++;
      }
      longest = std::max(longest, running);
    }

    return longest;
  }
};
