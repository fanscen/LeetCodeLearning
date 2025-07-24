class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        # 用右指针扩展窗口
        for right in range(len(nums)):
            current_sum += nums[right]
            # 当和大于等于target时，尝试从左侧收缩窗口
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0
        
if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
    print(s.minSubArrayLen(4, [1,4,4]))
    print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
    print(s.minSubArrayLen(15, [5,1,3,5,10,7,4,9,2,8]))