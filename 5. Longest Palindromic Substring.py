class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = right = 0
        is_inner_word_palindrome = [[False for i in range(len(s))] for j in range(len(s))]
        for j in range(1, len(s)):
            for i in range(j):
                is_palindrome = is_inner_word_palindrome[i+1][j-1] or j - i <= 2
                if s[i] == s[j] and is_palindrome:
                    is_inner_word_palindrome[i][j] = True
                    
                    if j - i > right - left:
                        left = i
                        right = j
                        
        return s[left:right+1]
        
