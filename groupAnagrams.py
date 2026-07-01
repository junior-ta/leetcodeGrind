# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Using a tuple as a key to a dictionary

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for str in strs:
            chars = [0] * 26
            for char in str:
                chars[ord(char) - ord('a')] += 1

            key = tuple(chars)
            if key not in seen:
                seen[key] = []
            seen[key].append(str)

        return list(seen.values())

if __name__ == '__main__':
    test= Solution()

    print(test.groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"]))

