class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        if n1>n2:
            return False
        cnts1=[0]*26
        cnts2=[0]*26
        for i in range(len(s1)):
            cnts1[ord(s1[i])-ord('a')]+=1
            cnts2[ord(s2[i])-ord('a')]+=1
        if cnts1==cnts2:
            return True

        for i in range(n1,n2):
            cnts2[ord(s2[i])-ord('a')]+=1
            cnts2[ord(s2[i-n1])-ord('a')]-=1

            if cnts2==cnts1:
                return True
        return False