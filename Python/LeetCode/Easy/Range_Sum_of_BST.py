# Given the root node of a binary search tree and two integers low and high, 
# return the sum of values of all nodes with a value in the inclusive range [low, high].

# Example 1:


# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
# Example 2:


# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

from typing import Optional

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rangeSumBST(self, root: Optional[TreeNode], low, high):
        # Base case: Wenn der Baum leer ist, ist die Summe 0
        if root is None:
            return 0

        # Initialisiere die Summe
        ans = 0

        # Rekursiver Aufruf für den linken Teilbaum, falls vorhanden
        if root.val > low:
            ans += self.rangeSumBST(root.left, low, high)

        # Füge den aktuellen Knotenwert zur Summe hinzu, falls er im Bereich liegt
        if low <= root.val <= high:
            ans += root.val

        # Rekursiver Aufruf für den rechten Teilbaum, falls vorhanden
        if root.val < high:
            ans += self.rangeSumBST(root.right, low, high)

        return ans

# Erstelle den Beispiel-Baum
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

# Definiere die Grenzen
low = 7
high = 15

# Erstelle die Solution-Instanz und rufe die Methode auf
result = Solution().rangeSumBST(root, low, high)

# Gib das Ergebnis aus
print(result)

