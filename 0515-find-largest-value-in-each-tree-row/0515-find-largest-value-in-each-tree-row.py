# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def solver(node , res):
            lsts=deque([node])
            while lsts:
                maxima=lsts[0].val
                for i in range(len(lsts)):
                    node=lsts.popleft()
                    maxima=max(maxima , node.val)
                    if node.left:
                        lsts.append(node.left)
                    if node.right:
                        lsts.append(node.right)
                res.append(maxima)
            return res
        return solver(root , [])