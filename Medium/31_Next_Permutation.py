from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Step 1: Find the first index i such that nums[i] < nums[i + 1], from the end
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If such an index is found, find the number just greater than nums[i] to the right
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap them
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the part after index i
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
