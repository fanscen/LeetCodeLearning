class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        while i < len(nums):
            while i < len(nums) and nums[i] == nums[i-1]:
                nums.pop(i)
            i = i + 1
        return len(nums)

if __name__ == "__main__":
    mac = Solution()
    #print(mac.removeDuplicates([1,1,2]))
    print(mac.removeDuplicates([0,0,1,1,1,1,1,1,2,2,2,2,3,3,4]))