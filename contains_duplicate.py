# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
#using a hashset

class Solution:

    def __init__(self, nums):
        self.nums= nums

    def hasDuplicate(self) -> bool:
        seen = set()
        for num in self.nums:
            if num in seen:
                return True

            seen.add(num) #else

        return False

if __name__ == '__main__':
    test1= Solution([1, 2, 3, 3])

    print(test1.hasDuplicate())