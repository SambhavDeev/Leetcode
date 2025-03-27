class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs=[[scores[i],ages[i]] for i in range(len(scores))]
        pairs.sort()#sorted with scores 

        dp=[pairs[i][0] for i in range(len(scores))]#store the scores

        for i in range(len(scores)):
            mscore,mage=pairs[i]
            for j in range(i):
                score,age=pairs[j]
                if mage>=age:
                    dp[i]=max(dp[i],mscore+dp[j])

        return max(dp)
        