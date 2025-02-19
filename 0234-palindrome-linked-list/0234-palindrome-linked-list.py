# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy=ListNode(0)
        curr=head
        while curr:
            newnode=ListNode(curr.val)
            newnode.next=dummy
            dummy = newnode
            curr=curr.next
        while head:
            if head.val != dummy.val:
                return False
            dummy=dummy.next
            head=head.next
        return True