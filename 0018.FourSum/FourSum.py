class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        sol = []
        nums.sort()

        m = 0
        while m < len(nums):
            i = m + 1
            while i < len(nums):
                j = i + 1
                k = len(nums) -1
                while j < k:
                    if nums[m] + nums[i] + nums[j] + nums[k] == target:
                        sol.append([nums[m],nums[i],nums[j],nums[k]])
                        k = k - 1
                        while j<k and nums[k+1] == nums[k] :
                            k = k - 1
                        j = j + 1
                        while j<k and nums[j-1] == nums[j]:
                            j = j + 1
                    elif nums[m] + nums[i] + nums[j] + nums[k] > target:
                        k = k - 1
                        while j<k and nums[k+1] == nums[k] :
                            k = k - 1
                    elif nums[m] + nums[i] + nums[j] + nums[k] < target:
                        j = j + 1
                        while j<k and nums[j-1] == nums[j]:
                            j = j + 1
                i =  i + 1
                while i < len(nums) and nums[i] == nums[i-1]:
                    i = i + 1
            m = m + 1
            while m < len(nums) and nums[m] == nums[m-1]:
                m = m + 1
        return sol

if __name__ == "__main__":
    mac = Solution()
    print(mac.fourSum([1,0,-1,0,-2,2] , 0))
    print(mac.fourSum([2,2,2,2,2] , 8))