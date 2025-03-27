class Solution:
    def bs(self,mat,target):
        low=0
        high=len(mat)
        while low<=high:
            mid=(low+high)//2
            if mat[mid]==target:
                return True
            elif mat[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c=len(matrix),len(matrix[0])
        for i in range(r):
            if matrix[i][0]<=target<=matrix[i][c-1]:
                return self.bs(matrix[i],target)
        
        return False
