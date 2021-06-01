class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        iround = 0
        sidelength = len(matrix)
        while iround < int(len(matrix)/2):
            j = 0
            while j < sidelength - 1:
                temp = matrix[0+iround][j+iround]
                matrix[0+iround][j+iround] = matrix[sidelength-1-j+iround][0+iround]
                matrix[sidelength-1-j+iround][0+iround] = matrix[sidelength-1+iround][sidelength-1-j+iround]
                matrix[sidelength-1+iround][sidelength-1-j+iround] = matrix[j+iround][sidelength-1+iround]
                matrix[j+iround][sidelength-1+iround] = temp
                j = j + 1
            sidelength = sidelength - 2
            iround = iround + 1

if __name__ == "__main__":
    mac = Solution()

    matrix = [[1,2],[3,4]]
    mac.rotate(matrix)
    print(matrix)