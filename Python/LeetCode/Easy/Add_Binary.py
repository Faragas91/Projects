# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = int(a, 2)
        decimal_b = int(b, 2)

        decimal_both = decimal_a + decimal_b

        binary_string = bin(decimal_both)[2:]
        return str(binary_string)
        

a = "1010"
b = "1011"

solution = Solution()

result = solution.addBinary(a, b)

print(result)
