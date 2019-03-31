'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution():
    def permute(self, nums = [1,2,3]):
        if len(nums) <= 1:
            return [nums]
        else:
            output = [] #store all permutations
            for i in range(len(nums)):
                #extract the element at position i
                cur = nums[i]
                #remaining list
                list_ = nums[:i] + nums[i+1:]
                
                #generate all permutations where cur is the first element
                for p in self.permute(list_):
                    output.append([cur] + p)
                    print(output)

            return output


if __name__ == "__main__":
    print(Solution().permute())

