class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        # 从右上角开始
        row, col = 0, n - 1

        while row < m and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                # 当前值太大，往左一列
                col -= 1
            else:
                # 当前值太小，往下一行
                row += 1

        return False