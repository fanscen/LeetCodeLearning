class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            """
            计算一个数的每个位置上的数字的平方和
            """
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        
        # 使用集合来检测循环
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1

if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))
    print(s.isHappy(2))
