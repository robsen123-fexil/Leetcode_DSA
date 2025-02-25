# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fst=head
        slow=head
        while fst and fst.next:
            slow=slow.next
            fst=fst.next.next
        # dummy=ListNode(0)
        # tail=dummy
        # while slow:
        #     temp=slow.next
            
        #     slow.next=tail
        #     tail=slow
           
        #     slow=temp
        # print(dummy)
        prv=None
        frst=slow
        while frst:
            tmp=frst.next
            frst.next=prv
            prv=frst
            frst=tmp
        frst=head
        scnd=prv
        maxima=0
        while scnd!=None:
            maxima=max(maxima , (scnd.val+frst.val))
            frst=frst.next
            scnd=scnd.next
        return maxima

