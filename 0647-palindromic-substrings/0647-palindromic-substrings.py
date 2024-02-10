class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(s):
            return s==s[::-1]
        
        count=0 
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                sub=s[i:j]
                if is_palindrome(sub):
                    count+=1
        return count
        