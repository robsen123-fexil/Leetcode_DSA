# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evens=ListNode(0)
        e=evens
        odds=ListNode(0)
        curr=head
        o=odds
        i=1
        while curr is not None:
            if i%2==0:
                e.next=ListNode(curr.val)
                e=e.next
            else:
                o.next=ListNode(curr.val)
                o=o.next
            curr=curr.next
            i+=1
        if evens.next is not None:
            o.next=evens.next
        return odds.next
