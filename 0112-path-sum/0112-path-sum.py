# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def lefter(root , sums , tar):
            if not root:
                return False
            sums+=root.val
            if sums==tar and not root.left and not root.right:
                return True
            return lefter(root.left , sums , tar) or lefter(root.right , sums , tar)
        def righter(root , sums , tar):
            if not root:
                return False
            sums+=root.val
            if sums==tar and not root.left and not root.right:
                return True
            return righter(root.left , sums , tar) or righter(root.right , sums, tar)
        return  lefter(root , 0 , targetSum ) or righter(root , 0 , targetSum)




