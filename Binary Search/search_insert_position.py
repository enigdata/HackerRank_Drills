'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Example
[1,3,5,6], 5 → 2

[1,3,5,6], 2 → 1

[1,3,5,6], 7 → 4

[1,3,5,6], 0 → 0
'''

class Solution():
    def search_insert(self, target, array):
        left, right = 0, len(array) - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if array[middle] == target:
                return middle
            elif array[middle] < target:
                left = middle
            else:
                right = middle

        print(left, right)
        if array[left] == target:
            return left
        if array[right] == target:
            return right
        else:
            if target < array[left]:
                return left 
            elif target > array[right]:
                return right + 1
            else:
                return left + 1

if __name__ == "__main__":
    print(Solution().search_insert(7, [1,3,5,6]))
