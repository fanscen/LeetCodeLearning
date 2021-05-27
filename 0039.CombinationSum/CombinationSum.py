class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        self.sol = []
        candidates.sort()
        self.biSearch(candidates,target,0,[])
        return self.sol
    
    sol = []

    def biSearch(self, candidates: list[int], target: int, left: int, sums:list[int]):
        i = left
        while i < len(candidates) and candidates[i] <= target:
            if candidates[i] == target:
                sums.append(candidates[i])
                self.sol.append(sums.copy())
                sums.pop()
                return 
            sums.append(candidates[i])
            self.biSearch(candidates,target - candidates[i],i,sums)
            sums.pop()
            i = i + 1

if __name__ == "__main__":
    mac = Solution()

    print(mac.combinationSum([2,3,6,7],7))
    print(mac.combinationSum([2,3,5],8))
    print(mac.combinationSum([2,7,6,3,5,1],9))