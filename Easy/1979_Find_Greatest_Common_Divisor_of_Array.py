from typing import List
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a:int, b:int)->int:
            while b:
                a, b = b, a%b
            return a
        smallest = min(nums)
        largest = max(nums)
        return gcd(smallest, largest)
    
sol = Solution()
print(sol.findGCD([7,5,6,8,3]))
