# https://leetcode.com/problems/decode-string/description/?envType=problem-list-v2&envId=2nlt4w25
# # Medium
""" 
Decode String
Problems:
Given an encoded string, return its decoded string.
example:    
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Input: s = "3[a2[c]]"
Output: "accaccacc"

Solution:
1. Initialize an empty stack to store characters and digits.
2. Loop through each character in the input string s.
3. If the character is a digit, check if the last element in the stack is also a digit. If it is, concatenate the digit to the last element. Otherwise, push the digit onto the stack.
4. If the character is a letter, check if the last element in the stack is also a letter. If it is, concatenate the letter to the last element. Otherwise, push the letter onto the stack.
5. If the character is '[', push it onto the stack.
6. If the character is ']', pop the last element from the stack (which will be a letter), then pop the last element again (which will be '['), and finally pop the last element again (which will be a digit). Multiply the letter by the digit and push the result back onto the stack.
7. After processing all characters, join the elements in the stack to form the final decoded string and return it.

"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # st = []
        st = []
        # loop qua từng char trong s
            # nhận vào digit, nếu trước đó là digit -> up digit lên, push lại vào st
            # nhận vào letter, nếu trước đó là letter -> concat và push lại vào st
            # nhận vào [, bỏ qua, đi tiếp
            # nhận vào ], pop letters, pop digits, d * l -> để push lại st
        for char in s:
            if char.isdigit():
                if st and st[-1].isdigit():
                    st[-1] += char
                else:
                    st.append(char)
            elif char.isalpha():
                if st and st[-1].isalpha():
                    st[-1] += char
                else:
                    st.append(char)
            elif char == '[':
                st.append(char)
            elif char == ']':
                letters = st.pop()
                open_bracket = st.pop()
                digits = st.pop()
                new_str = int(digits) * letters
                if st and st[-1].isalpha():
                    st[-1] += new_str
                else:
                    st.append(new_str)
            
        return ''.join(st)
    
# Test cases
solution = Solution()
print(solution.decodeString("3[a]2[bc]"))  # Output: "aaabcbc"
print(solution.decodeString("3[a2[c]]"))  # Output: "accaccacc"
print(solution.decodeString("2[abc]3[cd]ef"))  # Output: "abcabccdcdcdef"
print(solution.decodeString("abc3[cd]xyz"))  # Output: "abccdcdcdxyz"
             
