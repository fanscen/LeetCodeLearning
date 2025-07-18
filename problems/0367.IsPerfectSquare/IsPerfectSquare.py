class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True 
        
        left, right = 2, num
        
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1        
        return False

if __name__ == "__main__":
    solution = Solution()
    # 测试用例
    test_cases = [
        4,   # 完全平方数
        8,   # 非完全平方数
        1,   # 边界情况
        16,  # 完全平方数
        20   # 非完全平方数
    ]
    
    for x in test_cases:
        result = solution.isPerfectSquare(x)
        print(f"输入: num = {x}")
        print(f"输出: {result}")
        print("---")
