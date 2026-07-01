# Given a string s, find the length of the longest substring without duplicate characters.
#
# A substring is a contiguous sequence of characters within a string.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxlen = 0
        seen = set()
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])

            maxlen = max(maxlen, r - l + 1)

        return maxlen
