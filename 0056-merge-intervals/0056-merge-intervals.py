class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval:interval[0])
        merged=[]
        
        for interval in intervals:
            #in case of no overlap
            if not merged or merged[-1][1]<interval[0]:
                merged.append(interval)
            #in case of overlap
            else:
                merged[-1]=[merged[-1][0],max(merged[-1][1],interval[1])]
        
        return merged
                