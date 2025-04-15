# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que=deque([root])
        ans=[]
        if not root:
            return []
        while que:
            leng=len(que)
            lvl=[]
            for _ in range(leng):
                cur=que.popleft()
                lvl.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            ans.append(lvl)
        return ans