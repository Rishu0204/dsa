class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s ={}
        counter_t={}
        for c in s:
            if c in counter_s:
                counter_s[c]+=1
            else:
                counter_s[c]=1
        
        for c in t:
            if c in counter_t:
                counter_t[c]+=1
            else:
                counter_t[c]=1
        
        if counter_s==counter_t:
            return True
        else:
            return False
        