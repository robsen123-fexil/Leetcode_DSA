# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lsts=deque([root])
        l=0
        ans=[]
        if not root:
            return []
        while lsts:
            if l%2:
             
                k=0
                r=len(lsts)-1
                while k<r:
                    lsts[k].val , lsts[r].val=lsts[r].val , lsts[k].val
                    k+=1
                    r-=1
            ll=[]
            lng=len(lsts)
            for _ in range(lng):
                n=lsts.popleft()
               
                ll.append(n.val)
                if n.left:
                    lsts.append(n.left)
                if n.right:
                    lsts.append(n.right)
            ans.append(ll)
            l+=1
        return ans
            


