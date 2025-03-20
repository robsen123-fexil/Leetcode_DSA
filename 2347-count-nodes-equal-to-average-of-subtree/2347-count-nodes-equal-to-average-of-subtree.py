class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def solver(node, count):
            if not node:
                return count           
            def goer(node):
                if not node:
                    return (0, 0)
                sums, leng = goer(node.left)
                sums2, leng2 = goer(node.right)
                
                totalsum = sums + sums2 + node.val
                totalcount = leng + leng2 + 1
                return (totalsum, totalcount)
            tot, cnt = goer(node)
            if node.val == tot // cnt:
                count += 1
            count = solver(node.left, count)
            count = solver(node.right, count)
            
            return count
        
        return solver(root, 0)
