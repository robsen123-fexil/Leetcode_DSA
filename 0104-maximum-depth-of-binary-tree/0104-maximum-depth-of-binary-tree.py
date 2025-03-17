# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def solver(node , maxima , l):
            if not node:
                return maxima
            l+=1
            maxima=max(maxima , l)
            return max(solver(node.left , maxima , l) , solver(node.right , maxima , l))
        return solver(root , -inf , 0)