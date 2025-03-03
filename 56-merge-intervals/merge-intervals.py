class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        rang=[]
        for i in range(len(intervals)):
            if not rang or intervals[i][0]>rang[-1][1]:
                rang.append(intervals[i])

            else:
                rang[-1][1]= max(rang[-1][1],intervals[i][1])

        return rang