class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 :
            if nums[i-1] < nums[i] :
                j = len(nums) - 1
                while j > i - 1:
                    if nums[i-1] < nums[j]:
                        break
                    j = j - 1
                tmp = nums[j]
                nums[j] = nums[i-1]
                nums[i-1] = tmp
                
                j = len(nums) - 1
                k = i
                while k < j:
                    tmp = nums[j]
                    nums[j] = nums[k]
                    nums[k] = tmp
                    k = k + 1
                    j = j - 1 
                return
            i = i - 1
        nums.sort()
        return

if __name__ == "__main__":
    mac = Solution()
    nums = [1,2,3]
    mac.nextPermutation(nums)
    print(nums)

    nums = [3,2,1]
    mac.nextPermutation(nums)
    print(nums)

    nums = [1,3,2]
    mac.nextPermutation(nums)
    print(nums)

    nums = [1]
    mac.nextPermutation(nums)
    print(nums)

    nums = [5,8,3,2]
    mac.nextPermutation(nums)
    print(nums)
    '''
    5832
    8235
    '''