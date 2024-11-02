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

