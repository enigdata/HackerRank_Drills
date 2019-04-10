'''
Given a list of unique words, find all pairs of** distinct** indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]

Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
'''

class Solution:
    def valid_palindrome(self, s):
        '''
        test if a string a palindrome
        '''
        if len(s) % 2 == 0:
            for i in range(round(len(s)/2)):
                if s[i] != s[i+len(s)-1]:
                    return False

        else:
            for i in range(round(len(s)/2) - 1):
                if s[i] != s[i+len(s)-1]:
                    return False
        return True

    def palindrome_pairs(self, input):
        map_ = {word: index for index, word in enumerate(input)}

        result = list()

        for index, word in enumerate(input):
            #If there is empty string, and there exists palindrome words, then add their indices
            if "" in map_ and word != "" and self.valid_palindrome(word):
                empty = ""
                result.append([map_[empty], index])
                result.append([index, map_[empty]])

            #If there is reverse word, add the indices of the word and its reverse
            reverse_word = word[::-1]
            if reverse_word in map_ and map_[reverse_word] != index:
                result.append([map_[reverse_word], index])
                result.append([index, map_[reverse_word]])

            #divide parts of the words
            for x in range(1,len(word)):
                left, right = word[:x], word[x:]
                reverse_left, reverse_right = left[::-1], right[::-1]

                if self.valid_palindrome(left) and reverse_right in map_:
                    result.append([map_[reverse_right], index])

                if self.valid_palindrome(right) and reverse_left in map_:
                    result.append([index, map_[reverse_left]])
        return [list(x) for x in set(tuple(x) for x in result)]

if __name__ == "__main__":
    print(Solution().palindrome_pairs(["bat", "tab", "cat"]))
    print(Solution().palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"]))
    