class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

    
        result = []
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        while top <= bottom and left <= right:
            # 从左到右遍历上边界
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1  # 上边界下移
            
            # 从上到下遍历右边界
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # 右边界左移
            
            # 检查是否还有行需要遍历
            if top <= bottom:
                # 从右到左遍历下边界
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1  # 下边界上移
            
            # 检查是否还有列需要遍历
            if left <= right:
                # 从下到上遍历左边界
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # 左边界右移
        
        return result