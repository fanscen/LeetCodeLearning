class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        lennums = len(nums)

        if lennums % 2 == 0:
            return float((nums[int(lennums/2-1)] + nums[int(lennums/2)])/2)
        else:
            return float(nums[int((lennums-1)/2)])

if __name__ == "__main__":
    mac = Solution()
    print(mac.findMedianSortedArrays([1,3],[2]))
    print(mac.findMedianSortedArrays([1,2],[3,4]))
    print(mac.findMedianSortedArrays([0,0],[0,0]))
    print(mac.findMedianSortedArrays([],[1]))
    print(mac.findMedianSortedArrays([2],[]))