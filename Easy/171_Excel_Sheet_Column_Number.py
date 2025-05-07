class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0  # To store the final result
        for char in columnTitle:
            # Calculate the value for each letter, based on its position in the alphabet
            value = ord(char) - ord('A') + 1  # Converts 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26
            # Update the result as we move from left to right (base-26)
            result = result * 26 + value
        return result


sol = Solution()
print(sol.titleToNumber('AA'))
