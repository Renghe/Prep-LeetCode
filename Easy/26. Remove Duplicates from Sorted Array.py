from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0  # last unique element index

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1   # total unique numbers


# -------------------------
# Testing in VS Code
# -------------------------

print("Running Remove Duplicates Example...")

nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()

k = sol.removeDuplicates(nums)

print("k =", k)
print("Modified nums =", nums)
print("Unique portion =", nums[:k])
