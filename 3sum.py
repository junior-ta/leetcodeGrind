class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i, curr in enumerate(nums):
            if curr > 0:  # all numbers are greater than 0, no 3sum
                break

            if i > 0 and curr == nums[i - 1]:  # skip duplicate
                continue

            # seting the pointers
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if curr + nums[l] + nums[r] < 0:
                    l += 1

                elif curr + nums[l] + nums[r] > 0:
                    r -= 1

                else:
                    output.append([curr, nums[l], nums[r]])
                    a = nums[l]
                    r -= 1
                    while a == nums[l] and l < r:
                        l += 1

        return output
