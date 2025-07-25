class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        sol = []
        i = 0
        while i < n:
            sol.append([0]*n)
            i +=1
        
        left = 0
        right = n - 1
        up = 0
        down = n - 1

        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        i,j = 0,0
        directionsIndex = 0
        val = 1
        while val <= n*n:
            sol[i][j] = val
            if i + directions[directionsIndex][0] < up or i + directions[directionsIndex][0] > down or \
                j + directions[directionsIndex][1] < left or j + directions[directionsIndex][1] > right:
                if directionsIndex == 0:
                    up = up + 1
                elif directionsIndex == 1:
                    right = right - 1
                elif directionsIndex == 2:
                    down = down -1
                else:
                    left = left + 1                 
                directionsIndex = (directionsIndex + 1)%4
            if left > right or up > down:
                break

            i = i + directions[directionsIndex][0]
            j = j + directions[directionsIndex][1]
            val +=1
        return sol

if __name__ == "__main__":
    mac = Solution()

    print(mac.generateMatrix(3))