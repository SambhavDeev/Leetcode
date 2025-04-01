class Solution:
    def characterReplacement(self, s: str, k: int) -> int: #sliding window
        l=0
        freq=0
        char=[0]*26
        for r in range(len(s)):
            char[ord(s[r])-ord("A")]+=1
            while (r-l+1)-max(char)>k:
                char[ord(s[l])-ord("A")]-=1
                l+=1
            freq=max(freq,(r-l+1))

        return freq


      
     
        