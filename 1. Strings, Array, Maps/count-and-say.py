# https://leetcode.com/problems/count-and-say/description/?envType=problem-list-v2&envId=2nlt4w25
# Medium
""" 
Count and Say
Pre-prequisite: RLE (Run-length encoding)
RLE: Run-length encoding is a compression method that replaces consecutive repeated characters with a single character followed by the count of repetitions.
For example, the string "aaabbc" can be encoded as "3a2b1c".

Problem:
Count and Say is a sequence of numbers where each term is derived from the previous term by counting the number of consecutive digits and saying what they are.
For example, the first few terms of the sequence are:
1.     1
2.     11   
3.     21
4.     1211
5.     111221

Solutions:
1. Use a helper function to perform run-length encoding on the previous term.
2. Initialize a list to store the terms of the sequence.
3. Start with the first term "1" and iterate from 2 to n.
4. For each term, call the helper function to generate the next term based on the previous term.
5. Append the generated term to the list.
6. Return the last term in the list as the result.

Time complexity: O(n * m), where n is the number of terms and m is the average length of the terms.

"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def runlengthEncoding(s):
            count = 1
            result = ""
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    result += str(count) + s[i - 1]
                    count = 1
            result += str(count) + s[-1]
            return result

        # base case n == 1, return 1
        if n == 1:
            return "1"
        dp = ["1"]
        for _ in range (2, n + 1):
            dp.append(runlengthEncoding(dp[-1]))
        return dp[-1]
    
# Test cases
solution = Solution()
print(solution.countAndSay(1))  # Output: "1"
print(solution.countAndSay(2))  # Output: "11"
print(solution.countAndSay(3))  # Output: "21"
print(solution.countAndSay(4))  # Output: "1211"
print(solution.countAndSay(5))  # Output: "111221"
