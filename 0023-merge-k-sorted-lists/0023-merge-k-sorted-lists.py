# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lsts=[]
        for l in lists:
            while l:
                heapq.heappush(lsts , l.val)
                l=l.next
        dummy=ListNode(0)
        curr=dummy
        while lsts:
            curr.next=ListNode(heapq.heappop(lsts))
            curr=curr.next
        return dummy.next
