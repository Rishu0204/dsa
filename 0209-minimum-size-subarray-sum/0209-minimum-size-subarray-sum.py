class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_w= float('inf')
        l=0
        summ=0
        for r in range(len(nums)):
            summ+=nums[r]

            while summ>=target:
                min_w=min(min_w,r-l+1)
                summ-=nums[l]
                l+=1
            
        return min_w if min_w<float('inf') else 0