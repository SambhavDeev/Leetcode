class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime=[True]*(right+1)
        is_prime[0]=is_prime[1]=False
        for i in range(2,int(right**0.5)+1):
            if is_prime[i]:
                for j in range(i*i,right+1,i):
                    is_prime[j]=False
        ans=[]
        for i in range(left,right+1):
            if is_prime[i]:
                ans.append(i)
        if len(ans)<2:
            return [-1,-1]

        diff=float("inf")
        pair=[-1,-1]
        for i in range(1,len(ans)):
            curr=ans[i]-ans[i-1]
            if curr<diff:
                diff=curr
                pair=[ans[i-1],ans[i]]

        return pair





        