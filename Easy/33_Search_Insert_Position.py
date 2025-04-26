from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left+right)//2  #mid = 2,l=0,r=4           

            if nums[mid] == target:
                return mid
            elif nums[mid] < target: 
                left = mid + 1 #left = 0
            else:
                right = mid - 1 # right = 2-1 = 1, mid = 2
        return left
    
sol = Solution()
print(sol.searchInsert([1,3,8,9,10], 7))

