class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        ans=[]
        n=len(arr)
        arr.sort()
        for i in range(n):
            if not ans or arr[i][0]>ans[-1][1]:
                ans.append(arr[i])

            else:
                ans[-1][1]=max(arr[i][1],ans[-1][1])

        return ans        