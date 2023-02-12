# https://leetcode.com/problems/longest-common-prefix/

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        result = ""
        for j in range(len(first_word)+1):
            count = 0
            for i in range(0, len(strs)):
                if strs[i].startswith(first_word[0:j]):
                    count += 1
            if count == len(strs): 
                result = first_word[0:j]
        if result:
            return result
        elif len(strs) == 1:
            return first_word
        else:
            return ""

A = Solution().longestCommonPrefix(["flowers", "flow", "flight"])
# A = Solution().longestCommonPrefix(["a"])
# A = Solution().longestCommonPrefix(["flower","flower","flower","flower"])
# A = Solution().longestCommonPrefix(["c","acc","ccc"])
print(A)

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''