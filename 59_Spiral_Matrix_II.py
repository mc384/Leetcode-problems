class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for i in range(n)]
        L, R = 0, n
        T, B = 0, n
        start = 1

        while L < R and T < B:
            for i in range(L, R):
                matrix[T][i] = start
                start += 1
            print(matrix)
            T += 1
            for j in range(T, B):
                matrix[j][R-1] = start
                start += 1
            R -= 1
            if L >= R or T >= B:
                break
            for k in range(R-1, L-1, -1):
                matrix[B-1][k] = start
                start += 1
            B -= 1

            for l in range(B-1, T-1, -1):
                matrix[l][L] = start
                start += 1
            L += 1
        return matrix
