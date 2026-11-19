
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R, D = deque(), deque()
        n = len(senate)

        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)
        
        while R and D:
            r, d = R.popleft(), D.popleft()

            if r < d:
                R.append(n + r)
            else: D.append(n + d)
        
        return 'Radiant' if R else 'Dire'