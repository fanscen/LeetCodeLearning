class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        self.sol = []
        candidates.sort()
        self.biSearch(candidates,target,0,[])
        return self.sol
    
    sol = []

    def biSearch(self, candidates: list[int], target: int, left: int, sums:list[int]):
        if sum(candidates[left:]) < target:
            return
        i = left
        while i < len(candidates) and candidates[i] <= target:
            if candidates[i] == target:
                sums.append(candidates[i])
                if not(sums in self.sol):
                    self.sol.append(sums.copy())
                sums.pop()
                return
            sums.append(candidates[i])
            self.biSearch(candidates,target - candidates[i],i + 1,sums)
            sums.pop()
            i = i + 1

if __name__ == "__main__":
    mac = Solution()

    #print(mac.combinationSum2([10,1,2,7,6,1,5],8))
    print(mac.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],27))