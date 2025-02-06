# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        
        frst=head
        scnd=head.next

        frst.next=self.swapPairs(scnd.next) 
        scnd.next=frst

        return scnd
''' in the first recursive call frst=1 scnd =2 and frst.next=self.swap(3) we go to that function with head as 3(frst) and head.next=4(scnd) so in that case frst.next=swap(None) that will hit the base which will result in the return of None so by backtracking  and so that frst(3) and frst.next=none 3-None and scnd(4) and scnd.next=frst(3) 4-3-None and the func return scnd so by backtracking we reach first recursive case where frst.next==4-3-None and scnd(2).next=frst  soo 2-1-4-3-None.'''
