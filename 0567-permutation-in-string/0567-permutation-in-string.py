class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)

        if n1>n2:
            return False
        
        s1Count=[0]*26
        s2Count=[0]*26

        for i in range(n1):
            s1Count[ ord(s1[i]) - 97 ] += 1
            s2Count[ ord(s2[i]) - 97 ] += 1
        
        if s1Count==s2Count:
            return True
        
        #since n1 was exclusive in 1st loop till the remaining n2
        for i in range(n1,n2):
            s2Count[ ord(s2[i]) - 97 ] += 1
            s2Count[ ord(s2[i-n1]) - ord('a')] -= 1
            if s1Count==s2Count:
                return True
        return False 


