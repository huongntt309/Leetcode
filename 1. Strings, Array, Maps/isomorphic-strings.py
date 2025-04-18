# https://leetcode.com/problems/isomorphic-strings/?envType=problem-list-v2&envId=2nlt4w25
# easy
""" 
Isomorphic Strings

Problem:
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

Solutions:
1. Use two dictionaries to map characters from s to t and t to s.
2. Iterate through both strings simultaneously and check if the mapping is consistent.
3. If a character in s is already mapped to a different character in t or vice versa, return False.
4. If all characters are mapped consistently, return True.
5. Time complexity: O(n), where n is the length of the strings.
"""
from collections import defaultdict
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictmapS = defaultdict(str)
        dictmapT = defaultdict(str)
        for i, char in enumerate(s):
            # first time
            if dictmapS[char] == "":
                dictmapS[char] = t[i]
            # used again
            elif dictmapS[char] != t[i]:
                return False
        for i, char in enumerate(t):
            # first time
            if dictmapT[char] == "":
                dictmapT[char] = s[i]
            # used again
            elif dictmapT[char] != s[i]:
                return False
        return True
    
# Test cases
solution = Solution()
print(solution.isIsomorphic("egg", "add"))  # Output: True
print(solution.isIsomorphic("foo", "bar"))  # Output: False
print(solution.isIsomorphic("paper", "title"))  # Output: True
print(solution.isIsomorphic("badc", "baba"))  # Output: False