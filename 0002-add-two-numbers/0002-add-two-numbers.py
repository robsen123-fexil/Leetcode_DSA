# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(None)
        tail=dummy
        carry=0
        while l1 or l2 or carry :
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            sums=x+y+carry
            carry=sums//10
            sums=sums%10
            tail.next=ListNode(sums)
            tail=tail.next
            l1=l1.next if l1 else 0
            l2=l2.next if l2 else 0
        return dummy.next

        