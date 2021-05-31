class Solution:
    def jump(self, nums: list[int]) -> int:
        jumpnums = [-1 for i in range(len(nums))]
        if len(nums) == 1:
            return 0
        jumpnums[len(jumpnums)-1] = 0
        i = len(nums) - 2
        while i >= 0 :
            j = 1
            while j <= nums[i] and i + j < len(nums):
                if jumpnums[i + j] == -1:
                    j = j + 1
                    continue 
                if jumpnums[i] == -1:
                    jumpnums[i] = jumpnums[i+j] + 1
                elif jumpnums[i] > jumpnums[i+j] + 1:
                    jumpnums[i] = jumpnums[i+j] + 1
                j = j + 1
            i = i - 1
        return jumpnums[0]


if __name__ == "__main__":
    mac = Solution()

    #print(mac.jump([2,3,1,1,4]))
    print(mac.jump([2,3,0,1,4]))