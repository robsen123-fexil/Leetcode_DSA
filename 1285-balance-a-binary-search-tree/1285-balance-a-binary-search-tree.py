# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums=[]
        def folver(node):
            nonlocal nums
            if not node:
                return 
            folver(node.left)
            nums.append(node.val)
            folver(node.right)
            return nums
        lsts=sorted(folver(root))
        print(lsts)
        def solver(l , r):
            nonlocal lsts
            if l>r:
                return None
            mid=(l+r)//2
            root=TreeNode(nums[mid])
            root.left=solver(l , mid-1)
            root.right=solver(mid+1 , r)
            return root
        return solver(0 , len(lsts)-1)

        
        
            
            