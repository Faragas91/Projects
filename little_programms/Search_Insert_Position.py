# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return nums.index(target)



# Beispiel
nums = [1,3,5,6]
target = 7

# Eine Instanz der Solution-Klasse erstellen
solution = Solution()

# Die Methode aufrufen und das Ergebnis speichern
result = solution.searchInsert(nums, target)

# Das Ergebnis anzeigen
print("Der Index des Target in der Liste ist:", result)


