# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

# For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
# Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

# Each element of nums is in exactly one pair, and
# The maximum pair sum is minimized.
# Return the minimized maximum pair sum after optimally pairing up the elements.

 

# Example 1:

# Input: nums = [3,5,2,3]
# Output: 7
# Explanation: The elements can be paired up into pairs (3,3) and (5,2).
# The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
# Example 2:

# Input: nums = [3,5,4,2,4,6]
# Output: 8
# Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
# The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.


nums = [3,5,2,3]
half = int(len(nums) / 2)

pairs = []

for i in range(len(nums)):
    for j in range(i, len(nums) - 1):
        pair = nums[i], nums[j+1]
        pairs.append(pair)

sum_pair = []
for u in range(len(pairs)):
    sum_pair.append(sum(pairs[u]))

sorted_sums = sorted(sum_pair)

print(pairs)
    
print(sum_pair)

# set_pair = set(sum_pair)

# list_pair = list(set_pair)

# print(list_pair)