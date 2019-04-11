'''
There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].

We define a position P is a peak if:

A[P] > A[P-1] && A[P] > A[P+1]


Example 1:
	Input:  [1, 2, 1, 3, 4, 5, 7, 6]
	Output:  1 or 6
	
	Explanation:
	return the index of peek.


Example 2:
	Input: [1,2,3,4,1]
	Output:  3
'''

class Solution():
    def findPeakElement(self, array):
        left, right = 0, len(array) - 1
        while left < right:
            mid_1 = (left + right) // 2
            mid_2 = mid_1 + 1
            if array[mid_1] < array[mid_2]:
                left = mid_2
            else:
                right = mid_1
            print(left, right)
        return left

if __name__ == "__main__":
    print(Solution().findPeakElement([1,4,3,2,1]))