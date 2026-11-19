class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        cnt = 0

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = '0'

            while q:
                row, col = q.popleft()

                directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for i, j in directs:
                    nr, nc = row + i, col + j

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        q.append((nr, nc))
                        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    cnt += 1
                    bfs(i, j)
        

        return cnt