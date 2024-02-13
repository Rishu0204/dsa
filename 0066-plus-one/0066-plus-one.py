class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for d in digits:
            num=num*10+d
        num+=1
        res=[int(d) for d in str(num)]
        return res