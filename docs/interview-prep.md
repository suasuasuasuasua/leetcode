<!-- markdownlint-disable MD013 -->
# Anduril SWE Tech Screen — 2-Week Prep Plan

**Interview date:** ~2026-07-24 (two weeks from 2026-07-10)

**Format:** 40–45 min live coding on HackerRank, ~2 problems (1 easier + 1 harder), LeetCode **Medium** level.

**Language:** **Python** (fewer syntax fights, more escape hatches under time pressure). Note: this repo is currently C++ (`src/cpp/`), but interview in Python.

## Progress log

- **Sat Jul 11 (~2.5 hr):** Finished 125, 167, 15. Solved 3Sum twice (hashmap
  \+ textbook sorted two-pointer); nailed the duplicate-skip reasoning and O(n²)
  optimality. **Stopped before 11 Container With Most Water** — pick up there
  next session (good warmup before Sun's Binary Search + Linked List).

## What they actually grade (from the prep PDF)

1. **Clarifying questions** — never dive straight into code. Restate the problem, ask about input size, edge cases, duplicates, empty input, sorted-ness.
2. **Speed** — explicitly called out. You must recognize the pattern fast and code the common patterns from muscle memory.
3. **Clean, bug-free code** — runs, handles edges, no off-by-one.
4. **Talk out loud** — narrate your approach, complexity, and trade-offs. Mention a brute-force first, then optimize.
5. **Test your code** — walk through an example by hand at the end. Acknowledge alternate solutions.

---

## Your starting point (already done in this repo)

- **Arrays & Hashing:** 1, 217, 242, 49, 347, 238, 36, 271, 128 ✅ (section basically complete)
- **Stack:** 20, 155, 150, 739, 84, 853 ✅

Foundation is solid. The plan resumes the NeetCode 150 roadmap and drills the patterns interviewers reach for most.

---

## Priority tiers (if you're short on time, do Tier 1 cold)

**Tier 1 — highest frequency, must be automatic:**
Two Pointers, Sliding Window, Binary Search, Linked List, Trees (BFS/DFS), Hashing, Heaps.

**Tier 2 — very common at Medium:**
Backtracking, Graphs (BFS/DFS/topo), Intervals, Greedy.

**Tier 3 — know the pattern, less likely under 45 min:**
1-D & 2-D Dynamic Programming, Tries, Bit Manipulation.

---

## The Plan — mapped to your real schedule

**Your capacity:** ~1–2 hr each weekday morning (2–3 problems, one topic); full days on weekends (6–10 problems, ~2 topics). Week 2 may include time off — use any extra hours for the "stretch" bullets and a 3rd mock.

**Cadence per problem:** ~20 min attempt → read the optimal → **re-code it from scratch** the same session if you needed hints. The re-code is where speed comes from. Star anything you missed; those become your Week-2 review pool.

The two weekends carry all the heavy new material. Weekday mornings are single topics — deliberately front-loaded with the easier warmups (good for shaking off rust) and used later for review + mocks so a busy morning can't derail you.

### Week 1 — core patterns (Tier 1)

#### Sat Jul 11 (full day) — Two Pointers + Sliding Window

- Two Pointers:
  - [x] [125 Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
  - [x] [167 Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
  - [x] [15 3Sum](https://leetcode.com/problems/3sum/) ← common
  - [ ] [11 Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- Sliding Window:
  - [ ] [121 Best Time to Buy/Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
  - [ ] [3 Longest Substring w/o Repeat](https://leetcode.com/problems/longest-substring-without-repeating-characters/) ← common
  - [ ] [424 Longest Repeating Char Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
  - [ ] [567 Permutation in String](https://leetcode.com/problems/permutation-in-string/)
- Stretch: [ ] [42 Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) · [ ] [76 Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

#### Sun Jul 12 (full day) — Binary Search + Linked List

- Binary Search:
  - [ ] [704 Binary Search](https://leetcode.com/problems/binary-search/) (nail the template)
  - [ ] [74 Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
  - [ ] [153 Find Min in Rotated](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
  - [ ] [33 Search in Rotated](https://leetcode.com/problems/search-in-rotated-sorted-array/) ← common
  - [ ] [875 Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) (search on answer space)
- Linked List:
  - [ ] [206 Reverse List](https://leetcode.com/problems/reverse-linked-list/) ← must be instant
  - [ ] [21 Merge Two Sorted](https://leetcode.com/problems/merge-two-sorted-lists/)
  - [ ] [19 Remove Nth From End](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
  - [ ] [141 Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) / [142 Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Floyd's)
  - [ ] [2 Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
- Stretch: [ ] [143 Reorder List](https://leetcode.com/problems/reorder-list/)

#### Mon Jul 13 (AM) — Trees, warmups

- [ ] [226 Invert](https://leetcode.com/problems/invert-binary-tree/)
- [ ] [104 Max Depth](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [ ] [543 Diameter](https://leetcode.com/problems/diameter-of-binary-tree/)

#### Tue Jul 14 (AM) — Trees, structure

- [ ] [110 Balanced](https://leetcode.com/problems/balanced-binary-tree/)
- [ ] [100 Same Tree](https://leetcode.com/problems/same-tree/) / [572 Subtree](https://leetcode.com/problems/subtree-of-another-tree/)
- [ ] [235 LCA of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

#### Wed Jul 15 (AM) — Trees, BFS/BST

- [ ] [102 Level Order (BFS)](https://leetcode.com/problems/binary-tree-level-order-traversal/) ← must know
- [ ] [199 Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)
- [ ] [98 Validate BST](https://leetcode.com/problems/validate-binary-search-tree/) ← common

#### Thu Jul 16 (AM) — Trees finish + Heaps start

- [ ] [230 Kth Smallest in BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- [ ] [105 Build Tree from Pre/Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- [ ] [703 Kth Largest in Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

#### Fri Jul 17 (AM) — Heaps

- [ ] [1046 Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)
- [ ] [215 Kth Largest Element](https://leetcode.com/problems/kth-largest-element-in-an-array/) (also learn quickselect) ← common
- [ ] [973 K Closest Points](https://leetcode.com/problems/k-closest-points-to-origin/)
- Stretch: [ ] [621 Task Scheduler](https://leetcode.com/problems/task-scheduler/)

### Week 2 — advanced patterns + interview simulation

#### Sat Jul 18 (full day) — Backtracking + Graphs (Tier 2)

- Backtracking:
  - [ ] [78 Subsets](https://leetcode.com/problems/subsets/)
  - [ ] [39 Combination Sum](https://leetcode.com/problems/combination-sum/) ← common
  - [ ] [46 Permutations](https://leetcode.com/problems/permutations/)
  - [ ] [79 Word Search](https://leetcode.com/problems/word-search/)
  - [ ] [22 Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- Graphs:
  - [ ] [200 Number of Islands](https://leetcode.com/problems/number-of-islands/) ← common
  - [ ] [133 Clone Graph](https://leetcode.com/problems/clone-graph/)
  - [ ] [695 Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
  - [ ] [207 Course Schedule](https://leetcode.com/problems/course-schedule/) (topo/cycle) ← common
  - [ ] [994 Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) (multi-source BFS)
- Stretch: [ ] [417 Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

#### Sun Jul 19 (full day) — Intervals + Greedy + 1-D DP

- Intervals/Greedy:
  - [ ] [57 Insert Interval](https://leetcode.com/problems/insert-interval/)
  - [ ] [56 Merge Intervals](https://leetcode.com/problems/merge-intervals/) ← common
  - [ ] [435 Non-overlapping](https://leetcode.com/problems/non-overlapping-intervals/)
  - [ ] [253 Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (LC premium; [NeetCode](https://neetcode.io/problems/meeting-schedule-ii))
  - [ ] [53 Max Subarray](https://leetcode.com/problems/maximum-subarray/) (Kadane's)
  - [ ] [55 Jump Game](https://leetcode.com/problems/jump-game/)
- 1-D DP (Tier 3):
  - [ ] [70 Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
  - [ ] [198 House Robber](https://leetcode.com/problems/house-robber/) / [213 House Robber II](https://leetcode.com/problems/house-robber-ii/)
  - [ ] [322 Coin Change](https://leetcode.com/problems/coin-change/) ← common
  - [ ] [139 Word Break](https://leetcode.com/problems/word-break/)
- Stretch: [ ] [300 Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

#### Mon Jul 20 — 2-D DP + Tries (Tier 3)

- [ ] [62 Unique Paths](https://leetcode.com/problems/unique-paths/)
- [ ] [1143 Longest Common Subseq](https://leetcode.com/problems/longest-common-subsequence/)
- [ ] [208 Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/)
- [ ] [211 Add & Search Words](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
- [ ] [5 Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- *(If you take this day off work, add a 3rd full mock in the afternoon.)*

#### Tue Jul 21 (AM) — Mock interview #1

- 45-min timer, 2 unseen problems (1 easy-medium warmup + 1 medium-hard, e.g. a graph or tree). Talk out loud the whole time; use a blank pad, no autocomplete.
- Debrief: did you ask clarifying Qs? State complexity before coding? Test at the end?

#### Wed Jul 22 (AM) — Weak-area drilling

- Re-code the 3–5 starred problems you missed. Re-do the single hardest problem from your two weakest categories, timed.

#### Thu Jul 23 (AM) — Mock #2 + behavioral + wind down

- Second 45-min mock, fresh problems.
- Prep your **"why Anduril"** answer + 3–4 thoughtful interviewer questions.
- Light review only — no new material.

#### Fri Jul 24 — Interview day 🎯

- Warm up with ONE easy problem you've solved before to get loose. Don't grind.
- Re-read the "Interview-day checklist" and "Patterns cheat-sheet" below.

### If you take time off in Week 2

Highest-value uses of extra hours, in order:

1. **More mock interviews** (up to 1/day) — speed + talking out loud is what they grade.
2. Revisit any Tier 1 topic that still feels slow (usually trees or binary search).
3. Add the "stretch" problems you skipped, especially 76, 42, 417.

---

## Patterns cheat-sheet (recognize these fast)

| Signal in the problem | Reach for |
| --- | --- |
| Sorted array, find pair/triplet | Two pointers |
| Contiguous subarray/substring, "longest/shortest" | Sliding window |
| Sorted + "find X" or "minimize max" | Binary search (incl. on answer) |
| "Top K" / "K largest/closest" | Heap or quickselect |
| Tree "level by level" / shortest path in grid | BFS (queue) |
| All combinations/permutations/subsets | Backtracking |
| Grid of connected cells, "islands/regions" | DFS/BFS flood fill |
| Prerequisites / ordering / cycle | Topological sort |
| Overlapping ranges | Sort by start, merge |
| "Number of ways" / "min cost to reach" | DP |
| Prefix/suffix products or sums | Prefix arrays |
| Fast lookup / dedup / counting | Hash map/set |

## Python quick-reference (your escape hatches)

- `from collections import Counter, defaultdict, deque` — counting, adjacency lists, O(1) queue.
- `import heapq` — min-heap: `heappush/heappop`; max-heap via negation. `heapq.nlargest(k, it)`.
- `import bisect` — `bisect_left/right`, `insort` for sorted-array insertion.
- `functools.lru_cache(None)` / `@cache` — instant memoization for DP/recursion.
- Slicing `a[::-1]`, comprehensions, `enumerate`, `zip`, `sorted(key=...)`, tuple unpacking.
- Sentinels: `float('inf')`, `dict.get(k, default)`, `collections.defaultdict(int)`.

## Interview-day checklist

1. Restate the problem in your own words.
2. Ask: input size? empty? duplicates? sorted? negative numbers? return format?
3. State brute force + its complexity out loud.
4. Propose optimal approach, state target complexity BEFORE coding.
5. Code cleanly, narrate as you go.
6. Dry-run an example; check edge cases.
7. Mention alternative solutions/trade-offs.
8. Have 3–4 questions ready for them.

## Behavioral / company prep (5–10 min of the interview)

- Read Anduril's website + the linked media (Palmer interviews, counter-drone demo) so "why Anduril" is genuine.
- Look up your interviewer on LinkedIn beforehand.
- Prep questions like: team structure, what you'd work on, how they balance speed vs. reliability, tech stack decisions.
