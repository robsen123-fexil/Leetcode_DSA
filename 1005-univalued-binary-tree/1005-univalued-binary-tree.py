# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        que=deque([root])
        frst=root.val
        while que:
            cur=que.popleft()
            if frst!=cur.val:
                return False
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
        return True
        