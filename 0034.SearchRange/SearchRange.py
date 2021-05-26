class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1,-1]
        left = self.bisearchleft(nums,target,0,len(nums)-1)
        if left == -1:
            return [-1,-1]
        else:
            right = left
            while right < len(nums) - 1 and nums[right] == nums[right+1]:
                right = right + 1
            return [left,right]

    def bisearchleft(self,nums: list[int],target: int,left: int,right:int) -> int:
        middle = int((left + right)/2)
        if nums[middle] == target:
            i = middle
            while i > 0 and nums[i-1] == nums[i]:
                i = i - 1
            return i
        elif middle == left or middle ==right:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else :
                return -1
        elif target < nums[middle]:
            return self.bisearchleft(nums,target,left,middle)
        else:
            return self.bisearchleft(nums,target,middle,right)

        
if __name__ == "__main__":
    mac = Solution()
    #print(mac.search([4,5,6,7,0,1,2],0))
    #print(mac.searchRange([5,7,7,8,8,10],8))
    #print(mac.searchRange([5,7,7,8,8,10],6))
    print(mac.searchRange([1],1))