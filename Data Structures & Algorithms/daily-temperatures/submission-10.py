class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = [0] * len(t)
        stack = []

        for i in range(len(t)):
            while stack and t[i] > t[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        
        return res