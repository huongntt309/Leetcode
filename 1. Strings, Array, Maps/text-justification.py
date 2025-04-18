# https://leetcode.com/problems/text-justification/?envType=problem-list-v2&envId=2nlt4w25
# Hard
""" 
Text Justification
Problem:
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully justified.
Each line should be filled with spaces between words such that the total length of the line is maxWidth. The last line should be left-justified and no extra space is inserted between words.

Example:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output: [
  "This    is    an",
  "example  of text",
  "justification.  "
]
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output: [
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]

SOlutions:
1. Initialize an empty list totalRow to store the justified lines and an empty list curRow to store the current row of words.
2. Initialize a variable accLeng to keep track of the accumulated length of words in the current row.
3. Loop through each word in the input list words.
4. For each word, add its length to accLeng.
5. If accLeng is less than or equal to maxWidth, append the word to curRow and add 1 to accLeng (for the space between words).
6. If accLeng exceeds maxWidth, call the processJustification function to justify the current row and add it to totalRow.
7. Reset curRow and accLeng, and add the current word to curRow.
8. After processing all words, check if there are any remaining words in curRow. If so, left-justify the last row and add it to totalRow.
9. Return totalRow as the final result.

Time complexity: O(n), where n is the total number of characters in the input list words.
"""
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def processJustification(curRow, maxWidth):
            res = ""
            
            if len(curRow) == 1:
                res = curRow[0] + " " * (maxWidth - len(curRow[0]))
                return res

            numWhiteSpace = len(curRow) - 1
            totalLen = sum(len(word) for word in curRow)

            numSpaceCharacter = maxWidth - totalLen 
            spaceBt2Words = numSpaceCharacter // numWhiteSpace
            remainderSpaceBt2Words = numSpaceCharacter % numWhiteSpace  
            
            res = ""
            for i, word in enumerate(curRow):
                res += word
                if i < numWhiteSpace:  # Không thêm khoảng trắng sau từ cuối cùng
                    res += " " * spaceBt2Words
                    if i < remainderSpaceBt2Words:
                        res += " "  

            return res

        totalRow = []
        curRow = []
        accLeng = 0
        for curStr in words:
            accLeng += len(curStr)

            if accLeng <= maxWidth:
                curRow.append(curStr) 
                accLeng += 1
            elif accLeng > maxWidth: 
                curRowStr = processJustification (curRow, maxWidth)
                totalRow.append(curRowStr)
                
                # reset Row
                curRow = []
                accLeng = 0
                curRow.append(curStr)
                accLeng += len(curStr)
                accLeng += 1

        # the last Row 
        if accLeng > 0:
            leftLastRow = ' '.join(curRow)
            curRowStr =  leftLastRow + " "*(maxWidth - len(leftLastRow))
            totalRow.append(curRowStr)

        return totalRow