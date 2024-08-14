class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        h=set()
        l=0
        max_w=0

        for r in range(n):
            while s[r] in h:
                h.remove(s[l])
                l+=1
            w=(r-l)+1
            max_w=max(max_w,w)

            h.add(s[r])
        return max_w
           
            