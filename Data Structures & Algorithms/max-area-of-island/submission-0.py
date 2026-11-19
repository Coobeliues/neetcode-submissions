class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = []
        cnt = 1

        def dfs(r, c):
            nonlocal cnt
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0):
                return
            grid[r][c] = 0
            cnt += 1
            for i, j in directs:
                dfs(r + i, c + j)
            
            return cnt
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res.append(dfs(i, j) - 1)
                    cnt = 1
        
        return max(res) if len(res) > 0 else 0