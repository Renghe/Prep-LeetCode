class Solution:
    def twoSum(self, nums, target):
        mp = {}  # value : index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in mp:
                return [mp[complement], i]
            mp[num] = i

        return []
