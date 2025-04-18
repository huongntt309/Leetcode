// https: // leetcode.com/problems/valid-anagram/?envType=problem-list-v2&envId=2nlt4w25
/* 
Valid Anagram
Problem:
Given two strings s and t, return true if t is an anagram of s and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
For example, "anagram" is an anagram of "nagaram", and "rat" is an anagram of "car".

Solution:
1. Check if the lengths of the two strings are equal. If not, return false.
2. Create an array of size 26 to count the frequency of each character in the first string.
3. Iterate through the first string and increment the count for each character.
4. Iterate through the second string and decrement the count for each character.
5. If any count is not zero, return false.
6. If all counts are zero, return true.
7. Time complexity: O(n), where n is the length of the strings.
// 8. Space complexity: O(1), since the size of the count array is constant (26).
*/
class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        if (s.length() != t.length())
            return false;

        int count[26] = {0}; // Mảng tần suất cho 26 chữ cái

        for (char c : s)
            count[c - 'a']++; // Đếm số lần xuất hiện ký tự trong s
        for (char c : t)
            count[c - 'a']--; // Giảm số lần xuất hiện trong t

        for (int i = 0; i < 26; i++)
        {
            if (count[i] != 0)
                return false; // Nếu có ký tự khác 0, không phải anagram
        }

        return true;
    }
};