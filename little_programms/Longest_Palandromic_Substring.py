# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
        
        
# s = "babad"

# # Eine Instanz der Solution-Klasse erstellen
# solution = Solution()

# # Die Methode aufrufen und das Ergebnis speichern
# result = solution.longestPalindrome(s)

# # Das Ergebnis anzeigen
# print("Die Länge des Palindromes in s ist:", result)

s = "babad"
palindrom = ""
max_palindrom = ""

for i in range(len(s)):
    if s[i] not in palindrom:
        palindrom += s[i]

print(palindrom)
