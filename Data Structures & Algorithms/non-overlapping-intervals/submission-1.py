class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        cnt = 0
        res = [intervals[0]]
        for i in intervals[1:]:
            if i[0] < res[-1][1]:
                cnt += 1
            else: 
                res[-1][1] = max(res[-1][1], i[1])
        
        return cnt