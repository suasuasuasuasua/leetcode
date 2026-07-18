<!-- markdownlint-disable MD013 -->
# Anduril SWE Tech Screen — 2-Week Prep Plan

**Interview date:** ✅ **CONFIRMED — Fri 2026-07-24, 1:30pm** (the preferred Friday slot came through). Full runway, no compression needed. Interview is *afternoon*, so Fri AM = light warmup only.

**Format:** 40–45 min live coding on HackerRank, ~2 problems (1 easier + 1 harder), LeetCode **Medium** level.

**Language:** **Python** (fewer syntax fights, more escape hatches under time pressure). Note: this repo is currently C++ (`src/cpp/`), but interview in Python.

## Progress log

- **Fri Jul 10 (~2.5 hr):** Early start! Finished 125, 167, 15. Solved 3Sum twice (hashmap + textbook sorted two-pointer); nailed the duplicate-skip reasoning and O(n²) optimality. Stopped before 11 Container With Most Water.
- **Sat Jul 11:** Rest day (hiking + time with girlfriend) — recovery is part of the plan.
- **Sun Jul 12 (full day):** Finished Sliding Window + Binary Search. Binary search was the grind — 33 took a while to see the two-level "which half is sorted" decision, and 875 was ~40 min (20 staring, 20 on edge cases). Came out with a clear Flavor A vs Flavor B mental model. See "Binary Search — lessons learned" below. Made Anki cards.
- **Mon Jul 13 (AM):** Linked List. Warmup 20 (stack) — worked but roundabout (copied string + `pop(0)` → O(n²), pushed closers then double-popped); relearned the clean template (iterate directly, `stack.pop() != mapping[ch]`, closers never go on the stack). 206 Reverse List (~15 min) — was one step from correct; bug was `while head and head.next` stopping on the last node + `return head` instead of `return prev`. Both from over-guarding the last node, which is exactly the node whose flip gives the new head.
  Continued: 21 (~7 min, dummy head), 19 (two-pointer gap + dummy for remove-head), 141 (~2 min), 142 (~3 min — got the phase-2 algebra: it works *because* of phase 1's 2:1 speed ratio, which forces L ≡ C−m mod C).
  Finished the day with 2 Add Two Numbers (~10 min). **Full Linked List core done** (206, 21, 19, 141, 142, 2) — dummy-head + two-pointer patterns are clicking. Stretch 143 Reorder List skipped (out of time). Self-assessment: warmup 20 took too long, and was rusty on reverse (206) + remove-nth (19) — the **dummy-node idiom** was the main thing to relearn. Worth a re-drill later in the week.
- **Tue Jul 14 (AM):** Trees I complete (226, 104, 543, 110) + warmups 1 (~2 min) & 150 RPN (~10 min, truncate-toward-zero ≠ floor). Recursion clicked fast: the post-order "combine children" template, then the "return X / track Y" pattern in 3 flavors (tuple, nonlocal, sentinel). 226 in-order-fails insight was the highlight.
- **Wed Jul 15 (AM):** Trees II complete (100, 572, 235, 102) + warmups 739 (~8 min, monotonic stack) & 238 (~30 min, prefix/suffix — learned the O(1)-space version: write prefix into output, fold suffix with a running scalar). Clarified DFS vs BFS (pre/in/post all DFS; BFS = queue). 235: "BST → decide direction, don't search" (O(h) not O(n·h)); strict `<`/`>` needed so "node == target" falls through to LCA. 102: first BFS — snapshot `len(queue)` per level. **102 flagged for review.**
- **Thu Jul 16 (AM):** Trees III complete (199, 230, 98, 105) + warmups 49 & 155 (~3 min each). **ENTIRE TREES BLOCK DONE.** 199 BFS from memory (review paid off). 230: in-order=sorted + early exit; guard `is not None` not truthy. 98: the ancestor-range trap → pass `(low,high)` down; **info-flow principle: down→pre-order, up→post-order**. 105 (hard) in ~5-10 min — nailed the preorder-root + inorder-split insight; O(n) upgrade noted. Ahead of schedule — didn't need the Friday buffer.
- **Fri Jul 17:** Interview **confirmed for Fri Jul 24 1:30pm** 🎯. Work ran long — Heaps slipped to Sat. Rebalanced Week 2 (below): weekend absorbs Heaps, DP/Tries (Tier 3) is the shock absorber, two mocks stay protected. Solo side-quest: LC 6 Zigzag (learned the `numRows==1` guard + list-of-lists over defaultdict + O(n²) `+=` vs `join`; Python `list` = dynamic array not linked list, so `pop(0)` is O(n)).
- **Sat Jul 17→18 update:** Day off will be **Thu Jul 23** (interview eve — Mock #2 + behavioral, then taper); **Mon Jul 20** has a work meeting so DP/Tries is compressed.
- **Next up (Sat Jul 18):** Heaps (703, 1046, 215, 973) + Backtracking. Last Tier-1 topic!

## Lessons learned — patterns that fought back

### Binary Search (Sun Jul 12) — the big grind

**Flavor A vs Flavor B (the key mental model).** Recognize which one you're in *before* coding:

- **Flavor A — find an exact target** (704, 33): loop `while low <= high`, `return mid` on a hit, may return `-1` for not-found.
- **Flavor B — converge on a boundary** (153, 875, and 1011/410/1482): loop `while low < high`, *no* early return, predicate is monotonic (`F F F T T T`), fall out with `low == high` on the flip. No not-found case — the answer always exists in range. The tell: **there's no target to match; you're locating where a yes/no property changes.**

**33 Search in Rotated — the two-level decision.** The bug that ate the most time: collapsing "which half is sorted?" and "is the target in it?" into one `if`. It's *two* steps:

1. First prove which half is the clean sorted run: `if nums[low] <= nums[mid]:` → left is sorted; else → right is sorted.
2. *Only inside the known-sorted half*, range-check the target (inclusive both ends) to decide which way to go.
   - The `<=` in step 1 is load-bearing: when the window is 1–2 elements, `mid == low`, so `nums[low] == nums[mid]`; strict `<` misroutes it.
   - Rotation direction (left vs right) doesn't matter — "one half is always a clean sorted run" holds for any rotation.

**875 Koko — binary search on the *answer space*, not the array.** The flip that unlocked it: stop searching the piles; search over candidate eating speeds `k`. Recipe for this whole family:

1. **Domain:** what value am I searching over? Here `k ∈ [1, max(piles)]`. Start `low = 1` (not 0) — the true minimum domain removes the divide-by-zero guard entirely.
2. **Predicate:** a *computable* monotonic yes/no using data I already have — `feasible(k)` = `sum(ceil(pile / k) for pile) <= h`. The `ceil` is the edge case (she can't share an hour across piles).
3. **Converge:** `feasible` on `mid` → `high = mid`; else `low = mid + 1`; `return low`. No running-min/`result` var needed — the invariants (`high` always feasible, everything `< low` infeasible) make `low` the answer.

**153 Find Min — the predicate must be computable, and the anchor matters.**

- Don't phrase the predicate as "is this right of the pivot?" — that's circular (the pivot is what you're finding). Make it a real comparison: **`nums[mid] <= nums[high]`**. First `True` = the minimum.
- Anchor on `nums[high]`, *not* `nums[low]`: `nums[high]` always sits in the run containing the min, so the `F...F T...T` shape survives even the not-rotated edge case. Anchoring on `low` breaks on an already-sorted array.
- Generalizable recipe: **(1) domain, (2) computable monotonic predicate — never the answer itself, (3) pick the anchor/direction that survives the edge cases.**

### Sliding Window (Sun Jul 12) — smoother, a few patches

Less painful than binary search; the fixes were mostly about *when* to update state, not the core idea.

- **424 Longest Repeating Char Replacement — record-after-shrink gotcha.** Update the answer at the right moment relative to shrinking the window. Optimization: track a running `max_freq` instead of recomputing the most-common char each step (you don't even need to decrease it — the window never shrinks below the best seen).
- **567 Permutation in String — fixed-size window.** Slide a window the size of the pattern and compare counts. Patch (`fix(567)`): **incrementally update the count on slide** (add the entering char, remove the leaving one) instead of rebuilding the frequency map every step.
- **3 Longest Substring w/o Repeat.** The O(n) set-walk works; optional follow-up is the last-seen-index jump to move `left` in one hop instead of shrinking one char at a time.
- **Takeaway:** most sliding-window bugs are *timing* — where in the loop you record the answer vs. grow vs. shrink. Decide that order deliberately up front.

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

Foundation is solid, but these need a **brush-up re-drill** (highest interview frequency — re-code cold on Wed Jul 22 + as daily warmups): Arrays & Hashing → **1, 49, 347, 238, 128**; Stack → **20, 150, 739, 155**. The plan resumes the NeetCode 150 roadmap and drills the patterns interviewers reach for most.

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

#### Fri Jul 10 (done ✅) — Two Pointers (early start)

- [x] [125 Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- [x] [167 Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- [x] [15 3Sum](https://leetcode.com/problems/3sum/) ← common

#### Sat Jul 11 — REST 🥾 (hiking + girlfriend; recovery is part of the plan)

#### Sun Jul 12 (full day) — Finish Two Pointers + Sliding Window + Binary Search

- Finish Two Pointers:
  - [x] [11 Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (quick warmup)
- Sliding Window:
  - [x] [121 Best Time to Buy/Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
  - [x] [3 Longest Substring w/o Repeat](https://leetcode.com/problems/longest-substring-without-repeating-characters/) ← common (O(n) set-walk done; last-seen-index jump = optional follow-up)
  - [x] [424 Longest Repeating Char Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) (record-after-shrink gotcha; opt: running max_freq)
  - [x] [567 Permutation in String](https://leetcode.com/problems/permutation-in-string/) (fixed-size window; opt: incremental slide vs rebuild)
- Binary Search:
  - [x] [704 Binary Search](https://leetcode.com/problems/binary-search/) (nail the template — mid computed at top of loop)
  - [x] [74 Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) (nested search works; cleaner: flatten index mid//n, mid%n)
  - [x] [153 Find Min in Rotated](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) (canonical: compare nums[mid] vs nums[high], high=mid, while low<high, no running-min)
  - [x] [33 Search in Rotated](https://leetcode.com/problems/search-in-rotated-sorted-array/) ← common
  - [x] [875 Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) (search on answer space)
- Stretch: [ ] [42 Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) · [ ] [76 Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

#### Mon Jul 13 (AM) — Linked List

- [x] [206 Reverse List](https://leetcode.com/problems/reverse-linked-list/) ← must be instant (~15 min; `while head` + `return prev`)
- [x] [21 Merge Two Sorted](https://leetcode.com/problems/merge-two-sorted-lists/) (~7 min; dummy head `head = curr = ListNode()`, O(1) leftover attach)
- [x] [19 Remove Nth From End](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) (two-pointer gap; dummy makes remove-head collapse into the normal case — was the 20-failing-case bug)
- [x] [141 Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (~2 min, remembered Floyd's) / [x] [142 Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Floyd's)
- [x] [2 Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) (~10 min; digit+digit+carry, `divmod`. Reversed lists = node order is add order, no powers of 10. Polish: `while l1 or l2 or carry` folds the final-carry node into the loop)
- Stretch: [ ] [143 Reorder List](https://leetcode.com/problems/reorder-list/)

#### Tue Jul 14 (AM) — Trees I (traversal)

- [x] [226 Invert](https://leetcode.com/problems/invert-binary-tree/) (<5 min; pre-order swap. In-order FAILS — swapping *between* the two recursions redirects step 3 onto the old-left (undo) and skips the old-right entirely. Pre/post both safe.)
- [x] [104 Max Depth](https://leetcode.com/problems/maximum-depth-of-binary-tree/) (~3 min; post-order "combine children". Cleanest = no accumulator: `return 1 + max(depth(left), depth(right))`. Two accumulation styles: thread down as param vs build up via return.)
- [x] [543 Diameter](https://leetcode.com/problems/diameter-of-binary-tree/) (~10 min; "return one thing, track another" — helper returns *height* (`1 + max(l,r)`), harvest *diameter* (`l + r`) into a side var. Reuses 104's depth. Prefer `nonlocal best` over a class var — class-scope state can leak across calls.)
- [x] [110 Balanced](https://leetcode.com/problems/balanced-binary-tree/) (~5 min; solved with the **tuple-return** style `(height, is_balanced)` — a 3rd variant alongside 543's side-var and the `-1` sentinel. All O(n). Toolkit for "return X, track Y": tuple / nonlocal / sentinel — pick by what Y is.)

#### Wed Jul 15 (AM) — Trees II (structure + BFS)

- [x] [100 Same Tree](https://leetcode.com/problems/same-tree/) (~5 min; walk two nodes in lockstep, `match` on the None cases. Pre-order is fail-fast — check val before recursing so `and` short-circuits) / [x] [572 Subtree](https://leetcode.com/problems/subtree-of-another-tree/) (recursion-in-recursion: reuse `isSameTree` at every node. Outer combine is **`or`** ("match somewhere"), base case `False` — neutral element of `or`)
- [x] [235 LCA of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) (~6 min, but my version was O(n·h): post-order over all nodes + BST-search from each. **Optimal is O(h) single walk down**: both vals > node → go right; both < → go left; else they split → node IS the LCA. Lesson: "BST" → *decide direction*, don't search everywhere.)
- [x] [102 Level Order (BFS)](https://leetcode.com/problems/binary-tree-level-order-traversal/) ← must know (~15 min. First solved with DFS+depth-index (valid! pre-order fills each level L→R), then re-drilled the real **BFS**: `deque`, `while queue` = one level per iter, **snapshot `n = len(queue)` before the inner loop** to carve levels. `popleft()` O(1) not `pop(0)`. **REVIEW — first queue traversal; Anki card + re-drill.** BFS is the must-know for Sat graph day.)

#### Thu Jul 16 (AM) — Trees III (views + BST)

- [x] [199 Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) (~2-3 min from memory — BFS re-drill stuck! Grab rightmost per level. Tidy-up: capture the `i == level_size-1` node directly instead of building full level lists then discarding.)
- [x] [98 Validate BST](https://leetcode.com/problems/validate-binary-search-tree/) ← common (hit the classic trap: checking parent-child only misses ancestor constraints. Fix: pass a **(low, high) range** down, tighten on descent — left→`(low, node.val)`, right→`(node.val, high)`. **Big principle: info flows DOWN → pre-order (constrain, fail-fast); info flows UP → post-order (aggregate, e.g. 104/543/110).**)
- [x] [230 Kth Smallest in BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) (~10 min; **in-order = sorted**, k-th visited node = answer, with early exit. `k` is a *rank* not a value; increment counter ONCE in the node-slot of L-Node-R. Robustness: guard with `if result is not None` (bare `if result` breaks when answer is 0).)
- [x] [105 Build Tree from Pre/Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) (~5-10 min! preorder[0] = root; split inorder at root → left/right subtrees; recurse. My version O(n²) (`pop(0)` + `.index()` + slicing). **Optimal O(n): value→index hashmap, a preorder cursor, pass `(lo,hi)` bounds instead of slicing.** Same "precompute lookup + pass indices, don't rescan/copy" lesson.)

#### Fri Jul 17 — ⚠️ mostly lost to work; Heaps pushed to Sat

### Week 2 — advanced patterns + interview simulation

> **Rebalanced Fri Jul 17** after Heaps slipped a day. Interview confirmed for Fri 1:30pm = full runway, so the cascade is gentle. Priorities that stay protected: **Heaps (last Tier-1)**, **Graphs (top Tier-2)**, and **two mocks (Tue + Thu)**. **2-D DP + Tries (Tier 3)** is the shock absorber — compress or drop it if time runs short. **Mon has a work meeting** (DP compressed); **Thu is the day off** — a full interview-eve day for Mock #2 (+ optional 3rd) and behavioral, then taper.

#### Sat Jul 18 (full day) — Heaps + Backtracking

- Heaps (last Tier-1 — do first):
  - [x] [703 Kth Largest in Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) (~10 min; **the core "min-heap of size k" pattern**. Min-on-top is deliberate: evict the weakest survivor in O(log k), so top = kth largest. Gotchas: `heapify` is in-place/returns None; `nlargest` returns a plain list; `while`→`if` in add (push one at a time).)
  - [x] [1046 Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) (~5 min; **max-heap via negation** (`heapq` is min-only). Rule: "real→negate→heap; heap→negate→real", apply mechanically at push/pop edges. Classic slip: forgetting to negate the final return. `x - y` on two negated pops = the correctly-negated difference.)
  - [x] [215 Kth Largest Element](https://leetcode.com/problems/kth-largest-element-in-an-array/) ← common (solved 3 ways: `nlargest`, heapify-all + pop-down-to-k, size-k min-heap. Heap answer is A-grade — can *explain* quickselect's O(n) motivation (partition → recurse one side) even without coding it. **📌 DOGEARED STRETCH: quickselect implementation** — count-based 3-way partition; revisit fresh, watch NeetCode's video. Not needed for the interview.)
  - [x] [973 K Closest Points](https://leetcode.com/problems/k-closest-points-to-origin/) (compare squared dist `x*x+y*y`, skip sqrt. **THE key heap heuristic: a size-k heap uses the OPPOSITE orientation so its top = the weakest of your k = the eviction candidate.** k-largest→min-heap (703); k-smallest→max-heap (973). Eviction: `heapreplace` when new beats `heap[0]`.)
  - Stretch: [ ] [621 Task Scheduler](https://leetcode.com/problems/task-scheduler/)
- Backtracking:
  - [ ] [78 Subsets](https://leetcode.com/problems/subsets/)
  - [ ] [39 Combination Sum](https://leetcode.com/problems/combination-sum/) ← common
  - [ ] [46 Permutations](https://leetcode.com/problems/permutations/)
  - [ ] [79 Word Search](https://leetcode.com/problems/word-search/)
  - [ ] [22 Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

#### Sun Jul 19 (full day) — Graphs + Intervals / Greedy

- Graphs (top Tier-2 — reuses your BFS/DFS from trees):
  - [ ] [200 Number of Islands](https://leetcode.com/problems/number-of-islands/) ← common
  - [ ] [133 Clone Graph](https://leetcode.com/problems/clone-graph/)
  - [ ] [695 Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
  - [ ] [207 Course Schedule](https://leetcode.com/problems/course-schedule/) (topo/cycle) ← common
  - [ ] [994 Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) (multi-source BFS)
  - Stretch: [ ] [417 Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
- Intervals/Greedy:
  - [ ] [57 Insert Interval](https://leetcode.com/problems/insert-interval/)
  - [ ] [56 Merge Intervals](https://leetcode.com/problems/merge-intervals/) ← common
  - [ ] [435 Non-overlapping](https://leetcode.com/problems/non-overlapping-intervals/)
  - [ ] [253 Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (LC premium; [NeetCode](https://neetcode.io/problems/meeting-schedule-ii))
  - [ ] [53 Max Subarray](https://leetcode.com/problems/maximum-subarray/) (Kadane's)
  - [ ] [55 Jump Game](https://leetcode.com/problems/jump-game/)

#### Mon Jul 20 — DP + Tries (Tier 3 — the shock absorber; compress or drop if time's tight)

- 1-D DP:
  - [ ] [70 Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
  - [ ] [198 House Robber](https://leetcode.com/problems/house-robber/) / [213 House Robber II](https://leetcode.com/problems/house-robber-ii/)
  - [ ] [322 Coin Change](https://leetcode.com/problems/coin-change/) ← common
  - [ ] [139 Word Break](https://leetcode.com/problems/word-break/)
  - Stretch: [ ] [300 Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- 2-D DP + Tries (lowest priority — first to cut):
  - [ ] [62 Unique Paths](https://leetcode.com/problems/unique-paths/)
  - [ ] [1143 Longest Common Subseq](https://leetcode.com/problems/longest-common-subsequence/)
  - [ ] [208 Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/)
  - [ ] [211 Add & Search Words](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
  - [ ] [5 Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- *(⚠️ Monday has a work meeting — time is tight, so this is compressed. That's fine: DP/Tries is the shock absorber. Get 1-D DP if you can; let 2-D/Tries slide.)*

#### Tue Jul 21 (AM) — Mock interview #1

- 45-min timer, 2 unseen problems (1 easy-medium warmup + 1 medium-hard, e.g. a graph or tree). Talk out loud the whole time; use a blank pad, no autocomplete.
- Debrief: did you ask clarifying Qs? State complexity before coding? Test at the end?

#### Wed Jul 22 (AM) — Weak-area drilling + Array/Stack re-drill

- Re-code the 3–5 starred problems you missed. Re-do the single hardest problem from your two weakest categories, timed.
- **Array & Hashing / Stack re-drill** (already solved — re-code cold, ~5–8 min each, no peeking). Pick the ones that feel rusty; these are the highest-frequency at Medium:
  - Arrays & Hashing: [ ] [1 Two Sum](https://leetcode.com/problems/two-sum/) · [ ] [49 Group Anagrams](https://leetcode.com/problems/group-anagrams/) · [ ] [347 Top K Frequent](https://leetcode.com/problems/top-k-frequent-elements/) · [ ] [238 Product Except Self](https://leetcode.com/problems/product-of-array-except-self/) · [ ] [128 Longest Consecutive Seq](https://leetcode.com/problems/longest-consecutive-sequence/)
  - Stack: [ ] [20 Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) · [ ] [150 Eval RPN](https://leetcode.com/problems/evaluate-reverse-polish-notation/) · [ ] [739 Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) (monotonic stack) · [ ] [155 Min Stack](https://leetcode.com/problems/min-stack/)
  - Optional/harder: [ ] [853 Car Fleet](https://leetcode.com/problems/car-fleet/) · [ ] [84 Largest Rectangle](https://leetcode.com/problems/largest-rectangle-in-histogram/) (only if time — rarer under 45 min)
- **Also warm up with ONE of these each weekday morning (Mon–Thu)** before the day's topic — 5 min, get the fingers moving on a pattern you already know. Rotates the re-drill across the week so it isn't all crammed into Wednesday.

#### Thu Jul 23 — 🏖️ DAY OFF WORK (interview eve — front-load, then taper)

- **Morning (do the work):** Mock #2, fresh problems, 45-min timer — **do this one inside the HackerRank sandbox/CodePair editor** to learn the real environment (no autocomplete, custom test input, Python 3 in the dropdown, whitespace behavior). If it went well, optionally a 3rd mock — mocks are the single highest-value use of this day.
- **Setup check (do it today, not Fri 1pm):** Chrome + HackerRank CodePair, camera/mic test, stable internet, scratch paper ready. If it's video, tidy a small patch of background or sit against a plain wall (or use background blur).
- **Midday:** Prep your **"why Anduril"** answer + 3–4 thoughtful interviewer questions. Re-code any 1–2 problems that felt shaky this week (Anki review).
- **⚠️ Afternoon/evening — TAPER.** No new material, no grinding. The night before is for *rest and confidence*, not cramming. A tired brain interviews worse than a slightly-less-drilled one. Get good sleep.

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
