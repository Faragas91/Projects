# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.

# Given an integer, convert it to a roman numeral.

 

# Example 1:

# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.

# Example 2:

# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.

# Example 3:

# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

 

# Constraints:

#     1 <= num <= 3999

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        while num != 0:
            bla = False
            if num >= 1000 and bla is False:
                roman += "M"
                num -= 1000
                bla = True
            if num >= 900 and bla is False:
                roman += "CM"
                num -= 900
                bla = True
            if num >= 500 and bla is False:
                roman += "D"
                num -= 500
                bla = True
            if num >= 400 and bla is False:
                roman += "CD"
                num -= 400
                bla = True
            if num >= 100 and bla is False:
                roman += "C"
                num -= 100
                bla = True
            if num >= 90 and bla is False:
                roman += "XC"
                num -= 90
                bla = True
            if num >= 50 and bla is False:
                roman += "L"
                num -= 50
                bla = True
            if num >= 40 and bla is False:
                roman += "XL"
                num -= 40
                bla = True
            if num >= 10 and bla is False:
                roman += "X"
                num -= 10
                bla = True
            if num >= 9 and bla is False:
                roman += "IX"
                num -= 9
                bla = True
            if num >= 5 and bla is False:
                roman += "V"
                num -= 5
                bla = True
            if num >= 4 and bla is False:
                roman += "IV"
                num -= 4
                bla = True
            if num >= 1 and bla is False:
                roman += "I"
                num -= 1
                bla = True
        return roman
            


num = 20

solution = Solution()

result = solution.intToRoman(num)

print(result)