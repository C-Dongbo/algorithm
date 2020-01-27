mport operator
class Solution:
    

    
    def longestPalindrome(self, s: str) -> str:
        
        def isPalindromic(s):
            if s == s[::-1]:
                return True
            else:
                return False
        
        if len(s) <= 1:
            return s
        
        max_len, idx = 0, 0 
        for i in range(len(s)):
            if isPalindromic(s[i-max_len:i+1]):
                max_len , idx = max_len + 1, i-max_len
            elif i-max_len > 0 and isPalindromic(s[i-max_len-1 : i+1]):
                max_len , idx = max_len+2, i-max_len-1

        return s[idx:idx+max_len]

