class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]

    def uniquePaths2(self, m: int, n: int) -> int:
        sol = 0
        positions = []

        if m == 1 and n == 1:
            sol = 1

        positions.append([0,0])
        if positions[0][1] + 1 < n:
            positions.append([positions[0][0],positions[0][1] + 1])
            sol += 1
        if positions[0][0] + 1 < m:
            positions.append([positions[0][0]+1,positions[0][1]])
            sol += 1
        positions.pop(0)

        while len(positions) > 0:
            if positions[0][1] + 1 >= n or positions[0][0] + 1 >= m:
                positions.pop(0)
                continue

            positions.append([positions[0][0],positions[0][1] + 1])
            positions.append([positions[0][0] + 1,positions[0][1]])
            sol += 1
            positions.pop(0)
        return sol

if __name__ == "__main__":
    mac = Solution()

    print(mac.uniquePaths(10,10))