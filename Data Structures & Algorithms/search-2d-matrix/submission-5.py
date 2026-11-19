class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, (m * n) - 1
        # mid = n * m

        while l <= r:
            mid = l + (r - l) // 2
            row = mid // m
            col = mid % m

            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                r = mid - 1
            else: l = mid + 1
        
        return False
