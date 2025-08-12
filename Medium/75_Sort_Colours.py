class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            
            elif nums[mid] == 1:
                mid += 1
            
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1

nums = [0,1,2,1,0]
sol = Solution()
sol.sortColors(nums)
print(nums)