# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

 

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

 

# Constraints:

#     1 <= s.length <= 104
#     s consists of parentheses only '()[]{}'.


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {')': '(', ']': '[', '}': '{'}

        if len(s) % 2 == 0:
            length = True
        else:
            length = False
            result = False

        while length and s:
            left = None
            right = None

            for char, value in mappings.items():
                if s.count(value) != s.count(char):
                    length = False
                    break
                if value in s:
                    left = value
                    right = char
                    s = s.replace(value, "", 1)
                    s = s.replace(char, "", 1)
                    break    

        if not s:
            result = True
            return result
        else:
            result = False
            return result              


# Die Eingabedaten
s = "{[(())]}[{}]"

# Eine Instanz der Solution-Klasse erstellen
solution = Solution()

# Die Methode aufrufen und das Ergebnis speichern
result = solution.isValid(s)

# Das Ergebnis anzeigen
print("The Input " + s + " is : ", result)


