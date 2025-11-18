class Solution:
    def twoSum(self, nums, target): #Using Hashmap- Best Approach
        mp = {}  # value : index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in mp:
                return [mp[complement], i]
            mp[num] = i

        return []
