class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memory=set(nums)

        longest=0

        for num in memory:
            if longest>=len(nums):
                return longest

            if num+longest in memory:
                length=1
                while num+length in memory:
                    length+=1

                longest=max(longest,length)


        return longest