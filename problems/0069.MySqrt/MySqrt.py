class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x 
        left, right = 2, x // 2
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1        
        return right
    
if __name__ == "__main__":
    solution = Solution()
    # 测试用例
    test_cases = [
        4,   # 完全平方数
        8,   # 非完全平方数
        0,   # 边界情况
        1,   # 边界情况
        16,  # 完全平方数
        20   # 非完全平方数
    ]
    
    for x in test_cases:
        result = solution.mySqrt(x)
        print(f"输入: x = {x}")
        print(f"输出: {result}")
        print("---")