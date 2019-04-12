'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Example 1:

Input: [4, 5, 1, 2, 3] and target=1, 
Output: 2.
Example 2:

Input: [4, 5, 1, 2, 3] and target=0, 
Output: -1.
'''

class Solution:
    def search_sorted_array(self, target, array):
        if len(array) == 0:
            return -1

        left, right = 0, len(array) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if array[mid] == target:
                return mid
            if array[mid] < array[right]:
                if target > array[mid] and target <= array[right]:
                    left = mid 
                else:
                    right = mid 

            else:
                if target < array[mid] and target >= array[left]:
                    right = mid 
                else:
                    left = mid 
        print(left, right)
        if target == array[left]:
            return left
        if target == array[right]:
            return right
        else:
            return -1

if __name__ == "__main__":
    print(Solution().search_sorted_array(1, [4, 5, 1, 2, 3]))

