class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        is_palindrome_word = [[False for j in range(len(s))] for i in range(len(s))]
        count = len(s)
        for j in range(1,len(s)):
            for i in range(j):
                is_palindrome = is_palindrome_word[i+1][j-1] or j-i <= 2
                if s[i] == s[j] and is_palindrome:
                    is_palindrome_word[i][j] = True
                    count += 1
        return count
