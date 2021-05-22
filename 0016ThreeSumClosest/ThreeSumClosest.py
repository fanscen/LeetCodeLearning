class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        i = 0
        j = i + 1
        k = len(nums) -1
        sol = nums[i] + nums[j] + nums[k]
        distance = abs(sol - target)

        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) -1
            while j < k:
                sumthree = nums[i] + nums[j] + nums[k]
                distancethree = abs(sumthree - target)
                                
                if distancethree < distance :
                    sol = sumthree
                    distance = distancethree

                if sumthree < target :
                    j = j + 1
                    while j<k and nums[j-1] == nums[j]:
                        j = j + 1
                else :
                    k = k - 1
                    while j<k and nums[k+1] == nums[k] :
                        k = k - 1
            i =  i + 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i = i + 1
        return sol

if __name__ == "__main__":
    mac = Solution()
    print(mac.threeSumClosest([-1,2,1,-4] , 1))