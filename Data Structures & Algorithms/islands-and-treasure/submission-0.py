class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        directs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        while q:
            r, c = q.popleft()
            for dr, nr in directs:
                dx, nx = r + dr, c + nr

                if (0 <= dx < rows and 0 <= nx < cols and grid[dx][nx] == 2147483647):
                    grid[dx][nx] = grid[r][c] + 1
                    q.append((dx, nx))
        
