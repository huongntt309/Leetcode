// https://leetcode.com/problems/longest-common-prefix/?envType=problem-list-v2&envId=2nlt4w25
/* 
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Solution:
1. Compare the first two strings and find the common prefix.
2. Compare the common prefix with the next string and find the new common prefix.
3. Repeat step 2 until all strings are compared.
4. If the common prefix is empty, return an empty string.
5. If the common prefix is not empty, return the common prefix.
6. Time complexity: O(n*m), where n is the number of strings and m is the length of the longest string.
7. Space complexity: O(m), where m is the length of the longest string.

NOTE:
The space complexity can be reduced to O(1) by using a pointer to the common prefix instead of creating a new string.
The time complexity can be reduced to O(n) by using a trie data structure.
*/

class Solution {
public:
    string longestCommonPrefix2Strings(string a, string b) {
        if (a == "" || b == ""){
            return "";
        }
        int minLenAB = min(a.length(), b.length());
        string res = "";
        for (int i = 0; i < minLenAB; i++){
            if (a[i] == b[i]){
                res += a[i];
            } else {
                return res;
            }
        }
        return res;   
    };
    string longestCommonPrefix(vector<string>& strs) {
        string commonPrefix = strs[0];
        for (int i = 1; i < strs.size(); i++) {
            commonPrefix = longestCommonPrefix2Strings(commonPrefix, strs[i]);
            if (commonPrefix == "") {
                return "";
            }
        }
        return commonPrefix;
    }
    
};