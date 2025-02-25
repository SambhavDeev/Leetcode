class Solution:
    def rowgen(self,row):
        ans=1
        ansrow=[1]
        for col in range(1,row):
            ans=ans*(row-col)
            ans=ans//col
            ansrow.append(ans)
        return ansrow

    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[]
        for row in range(1,numRows+1):
            triangle.append(self.rowgen(row))
        return triangle

        