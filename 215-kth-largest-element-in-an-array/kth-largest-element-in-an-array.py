import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq=[]
        n=len(nums)
        for i in range(n):
            heapq.heappush(pq,-nums[i])

        freq=k-1
        while freq:
            heapq.heappop(pq)
            freq-=1

        return -pq[0]

        