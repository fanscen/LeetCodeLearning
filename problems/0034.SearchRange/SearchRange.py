class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1,-1]
        left = self.bisearchleft(nums,target,0,len(nums)-1)
        if left == -1:
            return [-1,-1]
        else:
            right = left
            while right < len(nums) - 1 and nums[right] == nums[right+1]:
                right = right + 1
            return [left,right]

    def bisearchleft(self,nums: list[int],target: int,left: int,right:int) -> int:
        middle = int((left + right)/2)
        if nums[middle] == target:
            i = middle
            while i > 0 and nums[i-1] == nums[i]:
                i = i - 1
            return i
        elif middle == left or middle ==right:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else :
                return -1
        elif target < nums[middle]:
            return self.bisearchleft(nums,target,left,middle)
        else:
            return self.bisearchleft(nums,target,middle,right)

        
if __name__ == "__main__":
    solution = Solution()
    # 测试用例
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8),  # 目标值在数组中出现多次
        ([5, 7, 7, 8, 8, 10], 6),    # 目标值不在数组中
        ([], 0),                      # 空数组
        ([1], 1),                     # 只有一个元素且等于目标值
        ([2, 2], 2)                   # 所有元素都等于目标值
    ]
    
    for nums, target in test_cases:
        result = solution.searchRange(nums, target)
        print(f"输入: nums = {nums}, target = {target}")
        print(f"输出: {result}")
        print("---")
