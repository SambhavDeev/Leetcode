class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #transpose
        #new matrix to create a trnaspose
        #transpose=list(map(list,zip(*matrix)))
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for row in matrix:
            row.reverse()
        return matrix