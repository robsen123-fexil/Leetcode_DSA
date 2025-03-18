# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p == root or q==root:
            return root
        def finder(node , val ,res):
            if not node:
                return None
            if node.val==val:
                res.append(val)
                return res
            res.append(node.val)
            if node.val<val:
                finder(node.right , val  , res)
            else:
                finder(node.left , val , res)
            return res
        frsts=finder(root , p.val  , [])
        scnd=finder(root , q.val, [])
        cnt=Counter(frsts+scnd)
        ans=0
        print(cnt)
        for k , v in cnt.items():
            if v!=2:
                return TreeNode(ans)

            ans=k
        return TreeNode(ans) 
        