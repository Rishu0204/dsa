class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        sol=[]
        
        i=0
        while i<len(nums):
            start=nums[i]
            
            while i < len(nums)-1 and nums[i]+1==nums[i+1]:
                i+=1
            
            if start!=nums[i]:
                sol.append(str(start)+'->'+str(nums[i]))
            else:
                sol.append(str(nums[i]))
            
            i+=1
        return sol