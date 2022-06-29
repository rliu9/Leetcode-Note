# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, cur_sum):
            if not root: return
            cur_sum += root.val
            if not root.left and not root.right:
                return cur_sum == targetSum
            else:
                return dfs(root.left, cur_sum) or dfs(root.right, cur_sum)
        return dfs(root,0)
    
    # O(n)
    # O(n) worst(unbalanced: one child) and O(logn) best
    
if __name__ == '__main__':
    s = Solution()
    t = TreeNode(1)
    t.left,t.right = TreeNode(2),TreeNode(3)
    assert False == s.hasPathSum(t, 5)
        