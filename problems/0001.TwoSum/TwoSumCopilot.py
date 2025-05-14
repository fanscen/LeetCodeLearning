'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。

示例1：
输入：nums = [2, 7, 11, 15], target = 9
输出：[0, 1]
解释：因为nums[0] + nums[1] == 9 ，返回[0, 1] 。
示例2：
输入：nums = [3, 2, 4], target = 6
输出：[1, 2]
示例3：
输入：nums = [3, 3], target = 6
输出：[0, 1]
'''

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

if __name__ == "__main__":
    solution = Solution()

    # 示例 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(result1)  # 输出：[0, 1]

    # 示例 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(result2)  # 输出：[1, 2]

    # 示例 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(result3)  # 输出：[0, 1]