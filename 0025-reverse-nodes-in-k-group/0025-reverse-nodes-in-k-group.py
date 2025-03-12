# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lists=[]
        frsts=head
        while frsts:
            lists.append(frsts.val)
            frsts=frsts.next
        l=0
        r=(k+k)
        res=[lists[i:i+k] for i in range(0 , len(lists) , k)]
       
       
        
        dummy=ListNode(0)
        frsts=dummy
        
        for i in res:
            if len(i)==k:
                i=i[::-1]
                
            
            l=0
            while l<len(i):
                frsts.next=ListNode(i[l])
                l+=1
                frsts=frsts.next
        return dummy.next