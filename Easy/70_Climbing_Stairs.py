class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        a,b = 1,2
        for _ in range(3,n+1):
            a, b = b, a+b
        return b
        
sol = Solution()
print(sol.climbStairs(3))