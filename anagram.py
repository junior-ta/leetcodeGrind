# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charset = {}

        for char in s:
            charset[char] = 1 + charset.get(char, 0)

        for char in t:
            if char in charset.keys() and charset[char] != 0:
                charset[char] -= 1
            else:
                return False

        if 1 in charset.values(): return False

        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT

if __name__ == '__main__':
    test= Solution()

    print(test.isAnagram("racecar", "carrace"))
    print(test.isAnagram("jar", "jam"))
