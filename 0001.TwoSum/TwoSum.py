class Solution:
    def twoSum(self, nums , target):
        for i in range(len(nums) - 1):
            x = nums[i]
            if target - x in nums:
                j =  i + 1
                while j < len(nums) :
                    y = nums[j]
                    if target == x + y :
                        return [i,j]
                    j = j + 1
        return []


if __name__ == '__main__':
    solution = Solution()
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(f'Input: nums = {nums1}, target = {target1}, Output: {result1}')
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f'Input: nums = {nums2}, target = {target2}, Output: {result2}')
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(f'Input: nums = {nums3}, target = {target3}, Output: {result3}')
