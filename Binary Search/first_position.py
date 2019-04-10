'''
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

Example 1:
	Input:  [1,4,4,5,7,7,8,9,9,10]，1
	Output: 0
	
	Explanation: 
	the first index of  1 is 0.

Example 2:
	Input: [1, 2, 3, 3, 4, 5, 10]，3
	Output: 2
	
	Explanation: 
	the first index of 3 is 2.

Example 3:
	Input: [1, 2, 3, 3, 4, 5, 10]，6
	Output: -1
	
	Explanation: 
	Not exist 6 in array.

'''

class Solution:
    def binarysearch(self, target, array):
        i, j = 0 , len(array)
        while i + 1 < j:
            middle = round((i + j) / 2)
            if array[middle] < target:
                i = middle
            elif array[middle] > target:
                j = middle
            elif array[middle] == target:
                return middle
        if array[i] == target:
            return i
        elif array[j] == target:
            return j
        return -1

if __name__ == "__main__":
    print(Solution().binarysearch(3, [1, 2, 3, 3, 4, 5, 10]))
    print(Solution().binarysearch(6, [1, 2, 3, 3, 4, 5, 10]))
            


