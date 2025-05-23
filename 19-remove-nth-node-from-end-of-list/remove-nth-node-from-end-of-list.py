# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:#(2n)cmplxty
        N=0
        curr=head
        while curr:
            N+=1
            curr=curr.next
        n=N-n
        if n==0:
            return head.next
        cnt=0
        curr=head
        
        while curr:
            cnt+=1
            if cnt==n:
                curr.next=curr.next.next
                break
            
            curr=curr.next
        return head
        

        

        