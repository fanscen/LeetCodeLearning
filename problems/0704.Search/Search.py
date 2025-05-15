class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1

if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例1
    nums1 = [-1,0,3,5,9,12]
    target1 = 9
    print(f"输入: nums = {nums1}, target = {target1}")
    print(f"输出: {sol.search(nums1, target1)}")
    
    # 测试用例2
    nums2 = [-1,0,3,5,9,12]
    target2 = 2
    print(f"输入: nums = {nums2}, target = {target2}")
    print(f"输出: {sol.search(nums2, target2)}")

