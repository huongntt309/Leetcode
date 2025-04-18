# https://leetcode.com/problems/set-matrix-zeroes/?envType=problem-list-v2&envId=2nlt4w25
# Medium
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        
        m = len(matrix)
        n = len(matrix[0])
        
        # Use the first row and first column as markers
        row_zero = False
        col_zero = False
        
        # Check if the first row has any zeroes
        for j in range(n):
            if matrix[0][j] == 0:
                row_zero = True
        
        # Check if the first column has any zeroes
        for i in range(m):
            if matrix[i][0] == 0:
                col_zero = True
        
        # Use the first row and first column to mark zeroes in the rest of the matrix
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set the marked cells to zero
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Set the first row to zero if needed
        if row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Set the first column to zero if needed
        if col_zero:
            for i in range(m):
                matrix[i][0] = 0