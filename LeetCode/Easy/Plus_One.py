# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
 

# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Liste wird in Ganzzahlen umgewandelt
        # Hierbei benötigt die Methode map eine Zeichenkette damit es funktioniert
        number = int(''.join(map(str, digits)))
        number += 1
        # Ganzzahlen werden wieder in eine Liste umgewandelt, dabei wird die Ganzzahl als erstes in einen String umgewandelt
        digits = [int(digit) for digit in str(number)]
        return(digits)


digits = [9,9]
solution = Solution()

result = solution.plusOne(digits)

print(result)
