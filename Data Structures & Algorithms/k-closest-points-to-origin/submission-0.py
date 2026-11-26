import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))
        
        res = []
        while k > 0:
            _, x, y = heapq.heappop(heap)
            res.append([x, y])
            k -= 1
        
        return res