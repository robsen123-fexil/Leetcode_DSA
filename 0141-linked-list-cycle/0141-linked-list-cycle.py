# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fst=head
        while fst and fst.next:
          
            slow=slow.next
            fst=fst.next.next
            if fst and slow:
                if fst==slow:
                    return True
        return False