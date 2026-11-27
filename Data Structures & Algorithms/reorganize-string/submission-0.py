import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [(-cnt, char) for char, cnt in counts.items()]
        heapq.heapify(heap)

        prev = None
        res = []

        while heap or prev:
            if prev and not heap:
                return ''
            
            cnt, char = heapq.heappop(heap)
            res.append(char)
            cnt += 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if cnt != 0:
                prev = (cnt, char)
            
        return ''.join(res)