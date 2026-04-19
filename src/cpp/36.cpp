#include <cctype>
#include <fmt/ranges.h>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
  bool isValidSudoku(std::vector<std::vector<char>> &board) {
    // validate the sudoku board
    // how can we make this faster?

    // each row must contain the digits 1-9 without duplicates
    // each column must contain the digits 1-9 without duplicates
    // each of the nine 3x3 sub-boxes must contain 1-9 without duplicates
    bool ret = true;

    // there are 9 rows, cols, and subcells
    std::unordered_map<int, std::unordered_set<char>> rows_counter,
        cols_counter, subcells_counter;

    for (int i = 0; i < board.size(); i++) {
      for (int j = 0; j < board.size(); j++) {
        const char &c = board.at(i).at(j);
        if (!std::isdigit(c)) {
          continue;
        }
        // NOTE: insert returns [iterator, inserted]
        // if we don't care about frequency, then we can get away with just
        // tracking with the std::unordered_set rather than std::unordered_map
        if (auto [_, ok] = rows_counter[i].insert(c); !ok) {
          return false;
        }
        if (auto [_, ok] = cols_counter[j].insert(c); !ok) {
          return false;
        }

        int subcell_idx = (i / 3 * 3) + (j / 3);
        if (auto [_, ok] = subcells_counter[subcell_idx].insert(c); !ok) {
          return false;
        }
      }
    }

    fmt::println("{}", rows_counter);
    fmt::println("{}", cols_counter);

    return ret;
  }
};

int main(int argc, char *argv[]) {
  Solution s;
  using inputs_t = std::vector<std::vector<char>>;
  using outputs_t = bool;
  std::vector<std::pair<inputs_t, outputs_t>> tests = {
      {{{'1', '2', '.', '.', '3', '.', '.', '.', '.'},
        {'4', '.', '.', '5', '.', '.', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '.', '3'},
        {'5', '.', '.', '.', '6', '.', '.', '.', '4'},
        {'.', '.', '.', '8', '.', '3', '.', '.', '5'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '.', '.', '.', '.', '.', '2', '.', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '8'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}},
       true},
      {{{'1', '2', '.', '.', '3', '.', '.', '.', '.'},
        {'4', '.', '.', '5', '.', '.', '.', '.', '.'},
        {'.', '9', '1', '.', '.', '.', '.', '.', '3'},
        {'5', '.', '.', '.', '6', '.', '.', '.', '4'},
        {'.', '.', '.', '8', '.', '3', '.', '.', '5'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '.', '.', '.', '.', '.', '2', '.', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '8'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}},
       false}};

  for (auto &[board, expected] : tests) {
    if (s.isValidSudoku(board) == expected) {
      std::cout << "Pass" << std::endl;
    } else {
      std::cout << "Fail" << std::endl;
    }
  }

  return 0;
}
