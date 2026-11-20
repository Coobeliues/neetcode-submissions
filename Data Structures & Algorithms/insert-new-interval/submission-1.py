class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, inter in enumerate(intervals):
            if inter[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif inter[1] < newInterval[0]:
                res.append(inter)
            else:
                newInterval[0] = min(newInterval[0], inter[0]) 
                newInterval[1] = max(newInterval[1], inter[1])
        res.append(newInterval)

        return res