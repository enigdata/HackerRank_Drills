'''
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].

Example 1:

Input:
[]
9
Output:
[-1,-1]

Example 2:

Input:
[5, 7, 7, 8, 8, 10]
8
Output:
[3, 4]
'''

class Solution:
    #两次二分
    def search_for_range(self, target, array):

        #search for left bound
        left, right = 0, len(array) - 1
        while left + 1 < right:
            middle = (left + right)// 2
            #print(middle)
            if target > array[middle]:
                left = middle
            else:
                right = middle
        if target == array[left]:
            left_bound = left 
        if target == array[right]:
            left_bound = right 
        else:
            return [-1, -1]

        #search for right bound
        left, right = left_bound, len(array) - 1
        while left + 1 < right:
            middle = (left + right)// 2
            if target < array[middle]:
                right = middle
            else:
                left = middle

        if target == array[right]:
            right_bound = right
        if target == array[left]:
            right_bound = left
        
        return [left_bound, right_bound]

if __name__ == "__main__":
    print(Solution().search_for_range(8, [5, 7, 7, 8, 8, 10]))


        
