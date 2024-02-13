class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_int =0
        for d in num:
            num_int=num_int*10+d
        num_int+=k
        res=[]
        while num_int>0:
            res.append(num_int%10)
            num_int//=10
        return res[::-1]