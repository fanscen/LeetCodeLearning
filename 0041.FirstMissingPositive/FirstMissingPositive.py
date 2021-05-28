class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        i = 0
        if nums[0] > 1 or nums[len(nums)-1] < 0 :
            return 1
        if len(nums) == 1:
            if nums[0] != 1:
                return 1
            else :
                return 2
        while i < len(nums) - 1:
            if nums[i+1]> 1 and nums[i+1]- nums[i] > 1 :
                if nums[i] + 1 > 0:
                    return nums[i] + 1
                else:
                    return 1
            i = i + 1
        return nums[len(nums)-1] + 1

if __name__ == "__main__":
    mac = Solution()

    #print(mac.combinationSum2([10,1,2,7,6,1,5],8))
    #print(mac.firstMissingPositive([1,2,0]))
    #print(mac.firstMissingPositive([3,4,-1,1]))
    #print(mac.firstMissingPositive([7,8,9,11,12]))
    print(mac.firstMissingPositive([1,2,2,1,3,1,0,4,0]))