class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

if __name__ == "__main__":
    mac = Solution()

    print(mac.sortColors([2,0,2,1,1,0]))