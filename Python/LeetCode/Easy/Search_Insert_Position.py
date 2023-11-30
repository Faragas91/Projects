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
        x = 0
        for number in nums:
            if number == target:
                return nums.index(target)
            x += 1
            if number != target and x == len(nums):
                nums.append(target)
                nums = sorted(nums)
 
# Beispiel
nums = [1,3,5,6]
target = 5

# Eine Instanz der Solution-Klasse erstellen
solution = Solution()

# Die Methode aufrufen und das Ergebnis speichern
result = solution.searchInsert(nums, target)

# Das Ergebnis anzeigen
print(result)



