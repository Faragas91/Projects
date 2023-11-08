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
null_matrix = np.zeros((numRows, len(s)), dtype=str)

# null_matrix[Zeile, row][Spalte, column]

down = True
diagonal = False
word = ""
i = 0

for char in s:
    if i != numRows and down == True:
        null_matrix[i][0] += char
        i +=1
    if i == numRows:
        down = False
        diagonal = True
    if diagonal == True:


        print(null_matrix)
        



#     print(char)


# print(null_matrix)
