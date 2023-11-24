# Given an integer x, return true if x is a
# palindrome
# , and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        forward = ""
        backward = ""

        for i in range(0, len(str(x)), 1):
            forward += str(x)[i]

        for j in range(len(str(x)) -1, -1, -1):
            backward += str(x)[j]

        if forward == backward:
            return True
        else:   
            return False
        
# Erzeuge eine Instanz der Solution-Klasse und rufe die Funktion auf
solution = Solution()

# Gib das Ergebnis aus 
result = solution.isPalindrome(-121)
print(result)


    