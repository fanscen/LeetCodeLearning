class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        resultindex = 0
        seekindex = 0
        
        while seekindex < len(nums):
            if nums[seekindex] != val:
                nums[resultindex] = nums[seekindex]
                resultindex += 1
            seekindex += 1
            
        return resultindex
    
if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    solution = Solution()
    result = solution.removeElement(nums, val)
    print(result)