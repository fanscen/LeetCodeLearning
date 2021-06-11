class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        sol = []
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1
        while True:
            i = up
            j = left
            while j <= right:
                sol.append(matrix[i][j])
                j = j + 1
            up = up + 1
            if up > down:
                break

            i = up
            j = right
            while i <= down:
                sol.append(matrix[i][j])
                i= i + 1
            right = right - 1
            if right < left:
                break

            i = down
            j = right
            while j >= left:
                sol.append(matrix[i][j])
                j = j - 1
            down = down - 1
            if up > down:
                break

            i = down
            j = left
            while i >= up:
                sol.append(matrix[i][j])
                i = i - 1
            left = left + 1
            if left >  right:
                break
        return sol

    def spiralOrder2(self,matrix: list[list[int]]) -> list[int]:
        sol = []
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1

        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        i,j = 0,0
        directionsIndex = 0
        while True:
            sol.append(matrix[i][j])
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
        return sol

if __name__ == "__main__":
    mac = Solution()

    print(mac.spiralOrder2([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))