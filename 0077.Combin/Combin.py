class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        sols = []

        if n == k :
            sol = [ i + 1 for i in range(n)]
            sols.append(sol)
            return sols
        if k == 1 :
            for i in range (n):
                sols.append([i+1])
            return sols

        sols1 = self.combine(n-1,k-1)
        for sol in sols1:
            sol.append(n)
        sols = sols1 + self.combine(n-1,k)
        return sols

if __name__ == "__main__":
    mac = Solution()
    print(mac.combine(4,2))