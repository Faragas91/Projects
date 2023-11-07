# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Explanation:
# P   A   H   N
# A P L S I I G
# Y   I   R

# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"

# Input: s = "PAYPALISHIRING", numRows = 5
# Output: "PINALSIGYAHRPI"
# Explanation:
# P       H
# A     S I
# Y   I   R
# P L     I G
# A       N


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pass

import numpy as np

numRows = 3  # Anzahl der Zeilen
s = "PAYPALISHIRING"
null_matrix = np.zeros((numRows, len(s)), dtype=int)

# null_matrix[Zeile, row][Spalte, column]

down = null_matrix[1][0]
diagonal = null_matrix[-1][-1]
word = ""


character = list(s)
print(character)





    



print(null_matrix)
