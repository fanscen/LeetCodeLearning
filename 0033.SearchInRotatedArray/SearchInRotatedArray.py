class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.bisearch(nums,target,0,len(nums)-1)

    def bisearch(self, nums: list[int], target: int, left: int, right: int) -> int:
        middle = int((left + right)/2)
        if nums[middle] == target:
            return middle
        elif middle == left or middle ==right:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else :
                return -1
        else :
            if nums[left] <= target :
                if nums[left] < nums[middle] and nums[middle] < target:
                    return self.bisearch(nums,target,middle,right)
                else :
                    return self.bisearch(nums,target,left,middle)
            else :
                if target < nums[middle] and nums[middle] < nums[right] :
                    return self.bisearch(nums,target,left,middle)
                else : 
                    return self.bisearch(nums,target,middle,right)

if __name__ == "__main__":
    mac = Solution()
    #print(mac.search([4,5,6,7,0,1,2],0))
    print(mac.search([4,5,6,7,0,1,2],3))
    #print(mac.search([1],0))
