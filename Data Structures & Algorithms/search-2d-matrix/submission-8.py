class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols
        while l < r:
            m = l + (r - l) // 2
            if matrix[m // cols][m % cols] == target:
                return True
            elif matrix[m // cols][m % cols] > target:
                r -= 1
            else: l += 1
        
        return False