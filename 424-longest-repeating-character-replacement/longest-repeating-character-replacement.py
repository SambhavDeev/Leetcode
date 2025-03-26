class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l=0
        char=[0]*26
        freq=0
        for r in range(len(s)):
            char[ord(s[r])-ord('A')]+=1
            while (r-l+1)- max(char) >k:
                char[ord(s[l])- ord('A')]-=1
                l+=1
            freq=max(freq,r-l+1)

        return freq

            
        