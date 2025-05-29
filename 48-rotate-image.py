class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                prev = matrix[i][j]
                for ni, nj in [[j, n-1-i], [n-1-i, n-1-j], [n-1-j, i], [i, j]]:
                    matrix[ni][nj], prev = prev, matrix[ni][nj]
        '''
        Time: O(n^2)
        Space: O(1)
        '''
