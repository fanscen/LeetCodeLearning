class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        f = []
        f.append(nums[0])
        i = 1
        while i < len(nums):
            f.append(max(f[i-1] + nums[i],nums[i]))
            i = i + 1
        return max(f)

if __name__ == "__main__":
    mac = Solution()

    print(mac.maxSubArray([5,4,-1,7,8]))