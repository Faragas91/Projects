# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left, right, s):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest_palindrome = ""
        
        for i in range(len(s)):
            # Überprüfe, ob ein Palindrom mit dem aktuellen Zeichen in der Mitte beginnt.
            palindrome1 = expand_around_center(i, i, s)
            # Überprüfe, ob ein Palindrom mit den aktuellen und nächsten Zeichen in der Mitte beginnt.
            palindrome2 = expand_around_center(i, i + 1, s)
            
            # Vergleiche die Länge der gefundenen Palindrome und aktualisiere das längste Palindrom.
            if len(palindrome1) > len(longest_palindrome):
                longest_palindrome = palindrome1
            if len(palindrome2) > len(longest_palindrome):
                longest_palindrome = palindrome2

        return longest_palindrome

# Beispiel
s = "aacabdkacaa"

# Eine Instanz der Solution-Klasse erstellen
solution = Solution()

# Die Methode aufrufen und das Ergebnis speichern
result = solution.longestPalindrome(s)

# Das Ergebnis anzeigen
print("Das längste Palindrom in s ist:", result)


