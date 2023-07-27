class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        tMatrix = [[] for i in range(len(matrix[0]))]
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(c):
                tMatrix[j].append(matrix[i][j])

        return tMatrix
