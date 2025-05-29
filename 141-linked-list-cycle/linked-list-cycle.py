# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: #slow pointer and fast pointer
        slw=head
        fst=head
        if head!=None and head.next !=None:
            while fst:
                if fst.next:
                    slw=slw.next
                    fst=fst.next.next
                else:
                    return False
                if slw==fst:
                    return True
        else:
            return False


            