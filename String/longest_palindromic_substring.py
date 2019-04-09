'''
Description
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
 
Example
Example 1:

Input:"abcdzdcab"
Output:"cdzdc"

Example 2:

Input:"aba"
Output:"aba"
'''

class Solution:
    # @return a string
    def find_palindrome(self, string, left, right):
        #中心枚举法
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return string[left + 1: right]

    def longest_palindrome(self, string):
        if len(string) <= 1:
            return string

        longest = ""
        for middle in range(len(string)):
            #find sub_palindrome with odd length
            sub = self.find_palindrome(string, middle, middle)
            if len(sub) > len(longest):
                longest = sub
            #find sub_palindrome with even length
            sub = self.find_palindrome(string, middle, middle + 1)
            if len(sub) > len(longest):
                longest = sub
        return longest
            
if __name__ == "__main__":
    print(Solution().longest_palindrome("abcdzdcab"))
    #print(Solution().longest_palindrome(string = "aba"))           　