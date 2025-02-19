# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new=ListNode(0)
        dummy=new
        frs=list1
        sec=list2
        while frs and sec:
            if frs.val>=sec.val:
                dummy.next=ListNode(sec.val)
                sec=sec.next
            else:
                dummy.next=ListNode(frs.val)
                frs=frs.next
            dummy=dummy.next
        while frs:
            dummy.next=ListNode(frs.val)
            frs=frs.next
            dummy=dummy.next
        while sec:
            dummy.next=ListNode(sec.val)
            sec=sec.next
            dummy=dummy.next
        return new.next