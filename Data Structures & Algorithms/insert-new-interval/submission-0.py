class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:


        arr = []
        for i, inter in enumerate(intervals):
            if newInterval[1] < inter[0]:
                arr.append(newInterval)
                return arr + intervals[i:]
            elif newInterval[0] > inter[1]:
                arr.append(inter)
            else:
                newInterval[0] = min(newInterval[0], inter[0])
                newInterval[1] = max(newInterval[1], inter[1])
        arr.append(newInterval)
        
        return arr