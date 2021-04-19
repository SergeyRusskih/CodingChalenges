# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/submissions/
def max_roduct(root):
    result = total = 0
        
    def dfs_sum(node):
        if not node: return 0
        
        left = dfs_sum(node.left)
        right = dfs_sum(node.right)
            
        result = max(result, left * (total - left), right * (total - right))
            
        return left + right + node.val
        
    total = dfs_sum(root)
    dfs_sum(root)
        
    return result % (10**9+7)