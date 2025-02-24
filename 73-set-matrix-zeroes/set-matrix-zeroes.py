class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        row=[0]*n
        clm=[0]*m

        for i in range (0,n):
            for j in range(0,m):
                if matrix[i][j]==0:
                    row[i]=1
                    clm[j]=1

        for i in range(0,n):
            for j in range(0,m):
                if row[i] or clm[j]:
                    matrix[i][j]=0

        return matrix

        