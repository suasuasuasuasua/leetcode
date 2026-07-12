from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0

        subcounter = Counter()
        result = 0
        while right < len(s):
            # add the new character to the counter
            subcounter[s[right]] += 1
            right += 1

            # find the most common character in the substring
            _, freq = subcounter.most_common(1)[0]
            # advance the left bound if we've exceeded the replacement threshold
            # - the idea is that we can only replace so many characters `k` in
            #   the substring s' in order to extend the most frequent char
            # - if we exceed that `k`, then slide the window over
            if right - left - freq > k:
                subcounter[s[left]] -= 1
                left += 1

            # record the maximum window size
            result = max(result, right - left)

        return result
