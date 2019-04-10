'''
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
	Input:  [[5]],2
	Output: false
	
	Explanation: 
	false if not included.
	
Example 2:
	Input:  [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
],3
	Output: true
	
	Explanation: 
	return true if included.
'''

class Solution: 
    def searchMatrix_1(self, target, matrix):
        import numpy as np
        matrix = np.reshape(matrix, [1, -1])
        return target in matrix

    def searchMatrix_2(self, target, matrix):
        if not matrix or not matrix[0]:
            return False
        nrows = len(matrix)
        ncols = len(matrix[0])

        i, j = 0, nrows * ncols - 1
        while i + 1 < j:
            middle = round((i + j)/2)
            x, y = middle // ncols, middle % ncols
            if target < matrix[x][y]:
                j = middle
            elif target > matrix[x][y]:
                i = middle
            elif target == middle:
                return True

        x, y = i // ncols, i % ncols
        if matrix[x][y] == target:
            return True

        x, y = j // ncols, j % ncols
        if matrix[x][y] == target:
            return True

        return False            

    def searchMatrix_3(self, target, matrix):
        #flatten to a list and then standard binary search
        list_ = [x for y in matrix for x in y]

        i, j = 0, len(list_) - 1
        while i + 1 < j:
            middle = round((i + j)/2)
            if list_[middle] < target:
                i = middle
            elif list_[middle] > target:
                j = middle
            elif list_[middle] == target:
                return True

        if list_[i] == target:
            return True
        if list_[j] == target:
            return True
        return False
        


    
