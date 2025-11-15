class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        # 1. 先检查第一行和第一列是否本来就需要全变 0
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # 2. 用第一行和第一列做标记
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 3. 根据标记把内部置 0（不动第一行第一列）
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 4. 处理第一行
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # 5. 处理第一列
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
        