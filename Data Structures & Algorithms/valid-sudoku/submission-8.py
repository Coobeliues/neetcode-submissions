class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = {}, {}, {}

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue

                if i not in rows:
                    rows[i] = set()
                if j not in cols:
                    cols[j] = set()
                sq_key = (i // 3, j // 3)
                if sq_key not in squares:
                    squares[sq_key] = set()
                
                if val in rows[i] or val in cols[j] or val in squares[sq_key]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                squares[sq_key].add(val)
        
        return True
