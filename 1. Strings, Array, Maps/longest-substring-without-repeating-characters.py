# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=2nlt4w25
# # Medium
""" 
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
using a queue to store the characters of the current substring.
If a character is not in the queue, append it to the queue and update the maximum length.
If a character is already in the queue, remove characters from the front of the queue until the character is removed. Then append the character to the queue.
The maximum length is updated at each step.
"""
from collections import deque
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # init
        q = deque()
        max_res = 0
        if s == "":
            return 0
        # loop
        for c in s:
            if c not in q:
                q.append(c)
                max_res = max(max_res, len(q))
            else:
                while q and q.popleft() != c:
                    continue
                q.append(c)
                
        return max_res
# test cases
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))  # Output: 1
print(solution.lengthOfLongestSubstring("pwwkew"))  # Output: 3
print(solution.lengthOfLongestSubstring(""))  # Output: 0