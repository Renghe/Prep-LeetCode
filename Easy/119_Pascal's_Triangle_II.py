from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0] * (rowIndex + 1)
        row[0] = 1

        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):  # Go right to left
                row[j] += row[j - 1]

        return row
