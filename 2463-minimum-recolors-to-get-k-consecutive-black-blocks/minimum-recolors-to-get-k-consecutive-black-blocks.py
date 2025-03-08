class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n=len(blocks)
        w=blocks[:k].count('W')
        res=w
        l,r=0,k
        while r<n:
            w+=(blocks[r]=="W")-(blocks[l]=="W")
            res=min(res,w)
            l+=1
            r+=1
        return res
            
            


        
        