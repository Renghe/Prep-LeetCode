class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        return haystack.find(needle)
    
sol = Solution()
print(sol.strStr("sadbutsad","sad"))

