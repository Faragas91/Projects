# A decimal number is called deci-binary if each of its digits 
# is either 0 or 1 without any leading zeros. For example, 
# 101 and 1100 are deci-binary, while 112 and 3001 are not.

# Given a string n that represents a positive decimal integer, 
# return the minimum number of positive deci-binary numbers needed so that they sum up to n.

# Example 1:

# Input: n = "32"
# Output: 3
# Explanation: 10 + 11 + 11 = 32

# Example 2:

# Input: n = "82734"
# Output: 8

# Example 3:

# Input: n = "27346209830709182346"
# Output: 9

 

# Constraints:

#     1 <= n.length <= 105
#     n consists of only digits.
#     n does not contain any leading zeros and represents a positive integer.

class Solution:
    def minPartitions(self, n: str) -> int:
        new_n = ""
        u = 0
        j = 0
        while True:
            u = 0
            for i in n:
                if int(i) >= 1:
                    number = str(int(i) - 1)
                    new_n += number
                else:
                    new_n += i
                    u += 1
            if u == len(n):
                break
            n = new_n
            new_n = ""
            j += 1
        return j

n = "32"
# n = "82734"
# n = "27346209830709182346"

solution = Solution()

result = solution.minPartitions(n)

print(result)
