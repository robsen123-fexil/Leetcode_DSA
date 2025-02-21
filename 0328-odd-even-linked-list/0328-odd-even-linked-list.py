# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        count=0
        tail=None
        while current is not None:
            tail=current
            count+=1
            current=current.next
        rnd=count//2
        if count==2:
            return head
        current=head
        while rnd>0 and current and current.next:
            tmpval=ListNode(current.next.val)
            current.next=current.next.next
            current=current.next
            tail.next=tmpval
            tail=tail.next
            rnd-=1
        return head
        



            