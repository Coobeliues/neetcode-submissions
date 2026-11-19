from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        cnt = Counter(hand)

        for start in sorted(hand):
            while cnt[start] > 0:
                for curr in range(start, start + groupSize):
                    if cnt[curr] == 0:
                        return False
                    cnt[curr] -= 1
        
        return True