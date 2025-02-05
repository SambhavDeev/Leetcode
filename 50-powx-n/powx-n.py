class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):
            if n==0:
                return 1.0
        
            if n==1:
                return x

            if n%2==0: #even number of x so group them together for example x=2 n=4 2*2*2*2 n=4  so we can write it as (2*2)*(2*2)==4*4 where n is reduced to half
                return pow(x*x,n//2)
        
            return x*pow(x,n-1)
        
        if n<0:
            return 1.0/pow(x,-n)

        else:
            return pow(x,n)

