class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        sols = []

        if len(nums) == 0:
            sols.append([])
            return sols
        if len(nums) == 1:
            sols.append([])
            sols.append(nums)
            return sols
        
        n = nums[0]
        sols1 = self.subsets(nums[1:])
        for sol in sols1:
            sols.append(sol[:])
            sol.append(n)
            sols.append(sol[:])
        return sols

if __name__ == "__main__":
    mac = Solution()
    print(mac.subsets([0]))