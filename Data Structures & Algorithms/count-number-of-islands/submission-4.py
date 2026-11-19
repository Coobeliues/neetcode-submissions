class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        directs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = '0'

            while q:
                r, c = q.popleft()
                for i, j in directs:
                    n, m = r + i, c + j
                    if (n < 0 or n >= rows or m < 0 or m >= cols or grid[n][m] == '0'):
                        continue
                    q.append((n, m))
                    grid[n][m] = '0'
            


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        
        return res