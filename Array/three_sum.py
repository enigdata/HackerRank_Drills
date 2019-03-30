"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution():
  def three_sum(self, nums):
    #sort the array
    nums = sorted(nums)
    output = list()
    for t in range(len(nums)):
      target = -nums[t]
      i = t + 1
      j = len(nums) - 1
      while i < j:
        if nums[i] + nums[j] == target:
          output.append([nums[t], nums[i], nums[j]])
          i += 1
          j -= 1 
        elif nums[i] + nums[j] > target:
          j =- 1
        elif nums[i] + nums[j] < target:
          i += 1
    return output

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().three_sum(nums))
