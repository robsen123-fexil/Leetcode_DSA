# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        l=0
        lsts=deque([root])
        while lsts:
            if l%2:
                k , r=0 , len(lsts)-1
                while k<r:
                    lsts[k].val , lsts[r].val=lsts[r].val , lsts[k].val
                    k+=1
                    r-=1
            for i in range(len(lsts)):
                n=lsts.popleft()
                if n.left:
                    lsts.append(n.left)
                if n.right:
                    lsts.append(n.right)
            l+=1
        return root
