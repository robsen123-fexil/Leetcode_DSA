# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def solver(node , mini , maxi):
            if not node:
                return maxi-mini
            mini=min(mini , node.val)
            maxi=max(maxi , node.val)
            left=solver(node.left , mini , maxi)
            right=solver(node.right , mini , maxi)
            return max(left , right)
        return solver(root , inf , -inf)
        