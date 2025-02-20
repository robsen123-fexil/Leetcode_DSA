# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        tail=dummy
        cnt=0
        frst=head
        while frst:
            cnt+=1
            frst=frst.next
        leng=cnt-n
        print(leng)
        frst=head
        ff=0
        while frst:
            tmp=frst
            if ff==leng:
                frst=frst.next

            if frst:
                tail.next=ListNode(frst.val)
                tail=tail.next
                frst=frst.next
            ff+=1
        return dummy.next        