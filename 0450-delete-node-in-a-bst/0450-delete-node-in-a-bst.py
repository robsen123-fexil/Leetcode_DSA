# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #the solver will do jump the root to be deleted
        def solver(node):
            if not node.left:
                return node
            return solver(node.left)
        def finder(node , val):
            if not node:
                return None
            if node.val<val:
                node.right=finder(node.right  , val)
            elif node.val>val:
               node.left= finder(node.left , val)
            else:
                if not node.left and  not node.right:
                    return None
                elif node.left and not node.right:
                    return node.left
                elif node.right and not node.left:
                    return node.right
                succ=solver(node.right)
                if succ:
                    node.val=succ.val
                    node.right=finder(node.right , succ.val)
            return node
        return finder(root , key)