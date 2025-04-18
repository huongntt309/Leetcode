# https://leetcode.com/problems/zigzag-conversion/description/?envType=problem-list-v2&envId=2nlt4w25
# Medium
""" 
Zigzag Conversion
Given a string s and an integer numRows, return the zigzag conversion of s on the given number of rows.
The zigzag pattern is formed by writing the characters of the string in a zigzag pattern across the specified number of rows, and then reading the characters row by row.
Example:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
because the zigzag pattern is:
P   A   H   N
A P L S I I G
Y   I   R

Solution:
1. Check if numRows is 1 or greater than or equal to the length of the string s. If so, return s as it is already in the desired format.
2. Calculate the circle length, which is the number of characters in one complete zigzag cycle.
3. Initialize a list res with empty strings for each row.
4. Loop through each character in the string s.
5. For each character, calculate its position in the zigzag pattern using the modulo operator and the circle length.
6. Append the character to the corresponding row in the res list.
7. After processing all characters, join the strings in the res list to form the final result.
8. Return the final result.
Time complexity: O(n), where n is the length of the input string s.
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        """
            string = "0123456789'10'11'12" numRow = 4
            convert-> '0    6    12'
                       1 5  7 11
                       2 4  8 10
                       3    9
             
                       row 1 has 1 5 7 11 -- % circle = 1 / 5
                       row 2 has 2 4 8 10 -- % circle = 2 / 4
        """
        if numRows == 1 or numRows >= len(s):
            return s

        circle = numRows * 2 - 2
        res = [""] * numRows 

        for i in range(len(s)):
            num = min(i % circle, circle - i % circle)
            res[num] += s[i] 

        totalRes = "".join(res) 
    
        return totalRes