# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        uniques=set()
        tail=head
        dummy=ListNode(0)
        ans=dummy
        while tail:
            if tail.val in uniques:
                tail=tail.next
            else:
                if tail:
                    uniques.add(tail.val)
                    ans.next=ListNode(tail.val)
                    ans=ans.next
                    tail=tail.next
        return dummy.next

            
