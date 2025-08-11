class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []

        for i in range(numRows):
            
            row = [1] * (i + 1)
            
            for j in range(1, i):
                left = result[i-1][j-1]
                right = result[i-1][j]
                row[j] = left + right
            result.append(row)

        return result

sol = Solution()
print(sol.generate(5))



