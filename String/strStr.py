'''
For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1.

Example 1:
	Input: source = "source" ，target = "target"
	Output: -1
	
	Explanation: 
	If the source does not contain the target content, return - 1.

Example 2:
	Input:source = "abcdabcdefg" ，target = "bcd"
	Output: 1
	
	Explanation: 
	If the source contains the target content, return the location where the target first appeared in the source.

'''

class Solution:
    def strStr_1(self, source, target):
        if len(source) == 0 or len(target) == 0:
            return -1
        for i in range(len(source) - len(target) + 1):
            if source[i] == target[0]:
                j = 1
                while j < len(target) and source[i + j] == target[j]:
                    j += 1
                if j == len(target):
                    return i
        return -1 

    def strStr_2(self, source, target):
        if len(source) == 0 or len(target) == 0:
            return -1
        for i in range(len(source) - len(target) + 1):
            if source[i:i+len(target)] == target:
                return i
        return -1

if __name__ == "__main__":
    print(Solution().strStr_1(source= 'abcdabcdefg', target = 'bcd'))
    print(Solution().strStr_2(source = 'abcdabcdefg', target = 'bcd'))
