class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        n=len(temperatures)
        ans=[0]*n
        for i,t in enumerate(temperatures):
            while stk and stk[-1][0]<t:
                stk_t,stk_i=stk.pop()
                ans[stk_i]=i-stk_i
            stk.append((t,i))
        return ans