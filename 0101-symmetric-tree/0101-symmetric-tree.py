# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def lefter(node , lsts):
            if not node:
                lsts.append(None)
                return lsts
            lsts.append(node.val)
    
            lefter(node.left , lsts)
            lefter(node.right , lsts)
            
            return lsts
        def righter(node , lsts):
            if not node:
                lsts.append(None)
                return lsts
            lsts.append(node.val)
           
            righter(node.right , lsts)
            righter(node.left , lsts)
           
            return lsts
        return  lefter(root ,[] )==righter(root , [])

            



        