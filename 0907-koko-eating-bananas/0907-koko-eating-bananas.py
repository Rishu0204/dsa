class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def K_works(k):
            hours=0
            for pile in piles:
                hours+=ceil(pile/k)
            return hours<=h
        
        l=1
        r=max(piles)

        while l<r:
            k=(l+r)//2
            if K_works(k):
                r=k
            else:
                l=k+1
        return l