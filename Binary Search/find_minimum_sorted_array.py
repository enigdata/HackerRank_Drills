'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

Example 1:

Input：[4, 5, 6, 7, 0, 1, 2]
Output：0
Explanation：
The minimum value in an array is 0.
Example 2:

Input：[2,1]
Output：1
Explanation：
The minimum value in an array is 1.

'''

class Solution:
    def find_min(self, array):
        left, right = 0, len(array) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            print(mid)
            if array[mid] <= array[right]: 
                right = mid
            else:
                left = mid
            print(left, right)
        
        return array[right]

if __name__ == "__main__":
    print(Solution().find_min([4, 5, 6, 7, 0, 1, 2]))

