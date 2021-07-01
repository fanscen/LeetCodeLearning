class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        f = obstacleGrid
        m = len(f)
        n = len(f[0])

        if f[0][0] ==1 or f[m - 1][n - 1] == 1:
            return 0
        
        for i in range(0, m):
            for j in range(0, n):
                if f[i][j] == 1:
                    f[i][j] = -1
        
        f[0][0] = 1
        for i in range(1, m):
            if f[i][0] == -1:
                continue
            elif f[i-1][0] == -1:
                f[i][0] = 0
            else: f[i][0] = f[i-1][0]

        for i in range(1, n):
            if f[0][i] == -1:
                continue
            elif f[0][i-1] == -1:
                f[0][i] = 0
            else: f[0][i] = f[0][i-1]
 
        for i in range(1, m):
            for j in range(1, n):
                if f[i][j] == -1:
                    continue
                elif f[i - 1][j] == -1 and f[i][j - 1] == -1:
                    f[i][j] = 0
                elif f[i - 1][j] == -1:
                    f[i][j] = f[i][j - 1]
                elif f[i][j - 1] == -1:
                    f[i][j] = f[i - 1][j]
                else:f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]

if __name__ == "__main__":
    mac = Solution()

    print(mac.uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))