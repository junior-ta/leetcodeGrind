# Given an integer array nums and an integer k, return the k most frequent elements within the array.
#
# Bucketsort algo:


from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs={}
        buckets=[[] for _ in range(len(nums)+1)]

        #keep track of each number freq
        for num in nums:
            freqs[num]= 1 + freqs.get(num, 0)

        #bucket sort the numbers by frequency
        #each index in the array is a frequence, it contains a list of numbers with that freq
        for key,value in freqs.items():
            buckets[value].append(key)

        #get K numbers in reverse order
        result=[]
        for bucket in range(len(buckets)-1, 0, -1):
            for num in buckets[bucket]:
                result.append(num)

                if len(result) == k:
                    return result

        return []


if __name__ == '__main__':
    test1= Solution()
    print(test1.topKFrequent(nums = [1,2,2,3,3,3], k = 2))
