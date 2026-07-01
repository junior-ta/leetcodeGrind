# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#
# Using maths with efficiency, finding the difference between the target and the actual element

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen= {}

        for i in range(len(nums)):
            difference= target - nums[i]

            if difference in seen.keys():
                return [seen[difference], i]
            else:
                if nums[i] not in seen.keys():
                    seen[nums[i]] = i


if __name__ == '__main__':
    test = Solution()

    print(test.twoSum([3,4,5,6], 7))
    print(test.twoSum([4,5,6], 10))
    print(test.twoSum([5, 5], 10))
    print(test.twoSum([4, 15, 6, 15, 20], 35))
    print(test.twoSum([0, 0, -6, 6, -4,3,5], -1))
