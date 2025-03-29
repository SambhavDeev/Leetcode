class Solution(object):
    def bs(self, arr,target):
        l=0
        r=len(arr)-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==target:
                return True
            elif arr[mid]<target:
                l=mid+1

            else:
                r=mid-1
        return False
        
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r=len(matrix)
        c=(len(matrix[0])-1)
        for i in range(r):
            if matrix[i][0]<=target<=matrix[i][c]:
                return self.bs(matrix[i],target)
        
        return False
        