# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        newNode=ListNode(0)
        ll=newNode
        tail=head
        while tail:
            while tail and tail.val==val:
                tail=tail.next
            if tail:
                ll.next=ListNode(tail.val)
                ll=ll.next
                tail=tail.next
        return newNode.next


        