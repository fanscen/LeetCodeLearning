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

if __name__ == "__main__":
    mac = Solution()

    print(mac.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))