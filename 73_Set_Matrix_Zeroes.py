class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = [1] * len(matrix)
        cols = [1] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = matrix[i][j]
                    cols[j] = matrix[i][j]

        for k in range(len(matrix)):
            matrix[k] = [l * rows[k] for l in matrix[k]]

        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                matrix[m][n] = matrix[m][n] * cols[n]

        return matrix   
        # Time: O(m * n)
        # Space: O(m + n)
