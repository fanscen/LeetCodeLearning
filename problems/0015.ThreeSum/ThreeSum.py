class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sol = []
        if len(nums) < 3:
            return sol
        nums.sort()
        i = 0
        while i < len(nums) and nums[i] <= 0 :
            j = i + 1
            k = len(nums) -1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    sol.append([nums[i],nums[j],nums[k]])
                    k = k - 1
                    while j<k and nums[k+1] == nums[k] :
                        k = k - 1
                    j = j + 1
                    while j<k and nums[j-1] == nums[j]:
                        j = j + 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k = k - 1
                    while j<k and nums[k+1] == nums[k] :
                        k = k - 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j = j + 1
                    while j<k and nums[j-1] == nums[j]:
                        j = j + 1
            i =  i + 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i = i + 1
        return sol

if __name__ == "__main__":
    mac = Solution()
    print(mac.threeSum([-1,0,1,2,-1,-4]))
    print(mac.threeSum([0]))
    print(mac.threeSum([]))