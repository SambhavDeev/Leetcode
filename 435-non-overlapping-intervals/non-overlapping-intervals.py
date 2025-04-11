class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])
        end=float('-inf')
        cnt=0
        for inter in intervals:
            if inter[0]>=end:
                end=inter[1]
            else:
                cnt+=1

        return cnt