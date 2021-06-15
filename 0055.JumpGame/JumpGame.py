class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        checkedNums = [0] * len(nums)
        return self.jumpNums(nums,0,checkedNums)

    def jumpNums(self, nums: list[int], index: int,checkedNums:list[int]) ->bool:
        if nums[index] == 0:
            return False
        if len(nums) - 1 - index <= nums[index]:
            return True
        sol = False

        i = 1
        while i <= nums[index] :
            if checkedNums[index + i] == 1:
                i += 1
                continue
            sol = self.jumpNums(nums,index + i,checkedNums)
            if sol == True:
                return True
            checkedNums[index + i] = 1
            i += 1
        return sol

    def canJump2(self, nums: list[int]) -> bool:
        k = 0
        i = 0
        while i < len(nums):
            if i > k : return False
            k = max(k, i + nums[i])
            i +=1
        return True
    
if __name__ == "__main__":
    mac = Solution()

    print(mac.canJump2([4,0,4,2,2,0,1,3,3,0,3]))