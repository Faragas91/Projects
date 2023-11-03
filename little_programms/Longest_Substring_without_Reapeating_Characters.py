# Given a string s, find the length of the longest
# substring
# without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ""
        max_result = ""
        start = 0
        length_max_result = 0

        for i in range(len(s)):
            if s[i] not in result:
                result += s[i]
            else:
                start = start + result.index(s[i]) + 1
                result = s[start:i+1]
            
            if len(result) > len(max_result):
                max_result = result
                length_max_result = len(max_result)

        return (length_max_result)

# Erzeuge eine Instanz der Solution-Klasse und rufe die Funktion auf
solution = Solution()

# Gib das Ergebnis aus
bla = solution.lengthOfLongestSubstring("abcabcbb")
print(bla)







# s = "abcabcbb"
# result = ""
# max_result = ""
# start = 0

# for i in range(len(s)):
#     if s[i] not in result:
#         result += s[i]
#     else:
#         start = start + result.index(s[i]) + 1
#         result = s[start:i+1]
    
#     if len(result) > len(max_result):
#         max_result = result

# print(max_result)