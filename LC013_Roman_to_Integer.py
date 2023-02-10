# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman_dict = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
            }
        i = 0 
        while i < len(s):
            if s[i] in roman_dict.keys():
                if (i < len(s) -1) and (roman_dict[s[i+1]] > roman_dict[s[i]]):
                    # subtraction
                    result = result + (roman_dict[s[i+1]] - roman_dict[s[i]])
                    i += 1
                else:
                    # addition 
                    result = result + roman_dict[s[i]]
            i += 1
        return result
    
#A = Solution().romanToInt("XXVII")
#A = Solution().romanToInt("LVIII")
#A = Solution().romanToInt("MCMXCIV")
A = Solution().romanToInt("III")
print(A)