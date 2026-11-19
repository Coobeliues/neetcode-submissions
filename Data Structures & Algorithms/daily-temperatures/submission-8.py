class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and temperatures[i] > stack[-1][1]:
                sI, sT = stack.pop()

                res[sI] = i - sI
            
            stack.append((i, t))
        
        return res