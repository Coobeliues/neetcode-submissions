class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        a = []
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        for i, v in d[:k]:
            a.append(i)
        
        return a 