class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_w=0
        l=0
        count=[0]*26

        for r in range(len(s)):
            count[ord(s[r])-65]+=1

            while (r-l+1)-max(count)>k:
                count[ord(s[l])-65]-=1
                l+=1
            max_w=max(max_w,(r-l+1))
        return max_w
