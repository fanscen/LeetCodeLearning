class Solution:
    def generateMatrix22(self, n: int) -> list[list[int]]:
        # 初始化 n×n 矩阵，所有元素为0
        matrix = [[0] * n for _ in range(n)]
        
        # 定义四个边界
        left, right = 0, n - 1    # 左边界和右边界
        top, bottom = 0, n - 1    # 上边界和下边界
        
        num = 1  # 当前要填充的数字，从1开始
        
        # 当边界有效时继续填充
        while left <= right and top <= bottom:
            # 1. 从左到右填充顶行
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1  # 上边界下移
            
            # 2. 从上到下填充右列
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1  # 右边界左移
            
            # 3. 从右到左填充底行（检查是否还需要填充）
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1  # 下边界上移
            
            # 4. 从下到上填充左列（检查是否还需要填充）
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1  # 左边界右移
        
        return matrix

if __name__ == "__main__":
    mac = Solution()
    print(mac.generateMatrix22(3))
    print(mac.generateMatrix22(4))   