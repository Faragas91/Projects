# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:

# Input: numRows = 1
# Output: [[1]]

 

# Constraints:

#     1 <= numRows <= 30

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            row = [1]  # Die erste Zahl in jeder Zeile ist 1

            for j in range(1, i):
                # Berechne den Wert gemäß den Regeln von Pascals Dreieck
                row.append(result[i-1][j-1] + result[i-1][j])

            if i > 0:
                row.append(1)  # Die letzte Zahl in jeder Zeile ist 1

            result.append(row)

        return result

numRows = 5

solution = Solution()

result = solution.generate(numRows)

print(result)
