class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def solver(node, count):
            if not node:
                return count           
            def goer(node):
                if not node:
                    return (0, 0)
                left_sum, left_count = goer(node.left)
                right_sum, right_count = goer(node.right)
                
                total_sum = left_sum + right_sum + node.val
                total_count = left_count + right_count + 1
                return (total_sum, total_count)
            
            total_sum, total_count = goer(node)
            if node.val == total_sum // total_count:
                count += 1
            
            count = solver(node.left, count)
            count = solver(node.right, count)
            
            return count
        
        return solver(root, 0)
