class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        cnt = 0
        fresh = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dx, dy in d:
                    dr, dc = dx + r, dy + c
                    
                    if (0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == 1):
                        grid[dr][dc] = 2
                        fresh -= 1
                        q.append((dr, dc))
            cnt += 1

        return cnt if fresh == 0 else -1