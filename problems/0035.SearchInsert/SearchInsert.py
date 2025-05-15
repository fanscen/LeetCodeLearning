class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)

if __name__ == "__main__":
    solution = Solution()
    # 测试用例
    test_cases = [
        ([1, 3, 5, 6], 5),  # 目标值在数组中
        ([1, 3, 5, 6], 2),  # 目标值不在数组中
        ([1, 3, 5, 6], 7),  # 目标值大于数组中所有元素
        ([1, 3, 5, 6], 0)   # 目标值小于数组中所有元素
    ]
    
    for nums, target in test_cases:
        nums_copy = nums.copy()  # 创建副本以避免修改原数组
        result = solution.searchInsert(nums_copy, target)
        print(f"输入: nums = {nums}, target = {target}")
        print(f"输出: {result}")
        print("---")