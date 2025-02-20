# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fst=head
        slow=head
        while fst and fst.next:
            slow=slow.next
            fst=fst.next.next
            if slow and fst and slow==fst:
                break
        else:
            return None
        slow=head
        while slow and fst!=slow:
            slow=slow.next
            fst=fst.next
        return slow
        
            