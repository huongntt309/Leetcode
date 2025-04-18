# https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=2nlt4w25
# Medium
""" 
Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. 
If the value of the symbol is less than the value of the next symbol, it is subtracted.
For example, IV is 4 because I is less than V.
If the value of the symbol is greater than or equal to the value of the next symbol, it is added.
For example, VI is 6 because I is greater than V.
The same principle applies to the rest of the symbols.
The input string is guaranteed to be valid.
The input string will not contain any leading zeroes.
Example 1:
Input: s = "III"                
Output: 3
Example 2:
Input: s = "IV"
Output: 4
Solution:
1. Create a dictionary to map Roman numerals to their integer values.
2. Initialize a variable result to 0 to store the final integer value.
3. Loop through the string s from the first character to the second-to-last character.
#    a. If the value of the current character is less than the value of the next character, subtract the value of the current character from result.
#    b. Otherwise, add the value of the current character to result.
# 4. After the loop, add the value of the last character to result.
# 5. Return result.
#
# Time complexity: O(n), where n is the length of the input string s.
# Space complexity: O(1), since we are using a fixed-size dictionary and a few variables.
"""

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> dict_char_value = {
            {'I', 1},   {'V', 5},   {'X', 10},  {'L', 50},
            {'C', 100}, {'D', 500}, {'M', 1000}};

        int result = 0;
        for (size_t i = 0; i < s.length() - 1; ++i) {
            if (dict_char_value[s[i]] < dict_char_value[s[i + 1]]) {
                result -= dict_char_value[s[i]];
            } else {
                result += dict_char_value[s[i]];
            }
        }
        result += dict_char_value[s.back()];
        return result;
    }
};