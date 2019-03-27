"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""

class Solution():
    def twosum(self, nums, target):
        #create a dictionary to store number and its index
        dict_ = {}
        for index, value in enumerate(nums):
            if target - value in dict_:
                return ([dict_[(target - value)], index])
                break
            dict_[value] = index
        return ([])

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(Solution().twosum(nums = nums, target = target))
    

