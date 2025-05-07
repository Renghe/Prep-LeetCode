from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
        for key in count:
            if count[key] == 1:
                return key
            
sol = Solution()
print(sol.singleNumber([2,2,1]))