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


class Solution(object):
    def isValid(self, s):
        opcl = dict(('()', '[]', '{}'))
        
        stack = []
        for idx in s:
            if idx in '([{':
                stack.append(idx)
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        return len(stack) == 0         


# Die Eingabedaten
s = "[({(())}[()])]"
# Eine Instanz der Solution-Klasse erstellen
solution = Solution()

# Die Methode aufrufen und das Ergebnis speichern
result = solution.isValid(s)

# Das Ergebnis anzeigen
print("The Input " + s + " is : ", result)
