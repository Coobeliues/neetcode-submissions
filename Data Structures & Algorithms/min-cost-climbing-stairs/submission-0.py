class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f, s = cost[0], cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(f, s)
            f = s
            s = curr
        
        return min(f, s)