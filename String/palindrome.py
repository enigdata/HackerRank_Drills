'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example
Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama"
Example 2:

Input: "race a car"
Output: false
Explanation: "raceacar"
'''

class Solution:
    def valid_Palindrome(self, string):
        if len(string) == 0:
            return False
        else:
            string = ''.join(e for e in string if e.isalnum())
            i, j = 0, len(string) - 1
            while i < j:
                if string[i].lower() != string[j].lower():
                    return False
                i += 1
                j -= 1
            return True
        
if __name__ == "__main__":
    print(Solution().valid_Palindrome(string = "race a car"))
    print(Solution().valid_Palindrome(string = "A man, a plan, a canal: Panama"))