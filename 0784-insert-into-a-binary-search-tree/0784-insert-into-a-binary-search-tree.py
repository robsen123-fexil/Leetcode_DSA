# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
 
        def solver(node , val):
            if not node:
                return TreeNode(val)
            if node.val<val:
                if not node.right:
                    node.right=TreeNode(val)
                else:
                    return solver(node.right , val)
            else:
                if not node.left:
                    node.left=TreeNode(val)
                else:
                    return solver(node.left , val)
            return node 
        if not root:
            return TreeNode(val)      
        solver(root , val)
        return root


        