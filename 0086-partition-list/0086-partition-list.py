# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        frst=head
        lessk=ListNode(0)
        lk=lessk
        greatk=ListNode(0)
        gk=greatk
        while frst:
            if frst.val<x:
               lk.next=ListNode(frst.val)
               lk=lk.next
            else:
               gk.next=ListNode(frst.val)
               gk=gk.next

            frst=frst.next
        ans=ListNode(0)
        lk.next=greatk.next
        tail=ans
        tail.next=lessk.next
        return ans.next