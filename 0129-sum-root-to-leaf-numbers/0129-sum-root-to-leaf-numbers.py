# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def solver(node  , sums , ans):
            if not node:
                return ans
            if not node.left and not node.right:
                sums+=str(node.val)
                ans+=int(sums)
                return ans
            sums+=str(node.val)
            lefter=solver(node.left , sums , ans)
            righter=solver(node.right, sums , ans)
            
            return lefter+righter
        return solver(root , '' , 0)
            