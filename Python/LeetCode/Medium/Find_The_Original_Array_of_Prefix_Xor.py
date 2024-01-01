# You are given an integer array pref of size n. Find and return the array 
# arr of size n that satisfies:

#     pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].

# Note that ^ denotes the bitwise-xor operation.

# It can be proven that the answer is unique.

# Hint
# Consider the following equation: x ^ a = b. How can you find x?
# Notice that arr[i] ^ pref[i-1] = pref[i]. 
# This is the same as the previous equation.
 

# Example 1:

# Input: pref = [5,2,0,3,1]
# Output: [5,7,2,3,2]
# Explanation: From the array [5,7,2,3,2] we have the following:
# - pref[0] = 5.
# - pref[1] = 5 ^ 7 = 2.
# - pref[2] = 5 ^ 7 ^ 2 = 0.
# - pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
# - pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.

# Example 2:

# Input: pref = [13]
# Output: [13]
# Explanation: We have pref[0] = arr[0] = 13.

# Constraints:

#     1 <= pref.length <= 105
#     0 <= pref[i] <= 106

from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [0] * len(pref)
        arr[0] = pref[0]
        arr.reverse()
        pref.reverse()
        
        for i in range(len(pref)):
            if i != len(pref) - 1:
                arr[i] = pref[i] ^ pref[i + 1]
            else:
                break
        arr.reverse()
        return arr


pref = [5,2,0,3,1]

solution = Solution()

result = solution.findArray(pref)

print(result)