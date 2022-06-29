# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, cur_sum, targetSum):
        if not root:return
        cur_sum += root.val
        if cur_sum == targetSum:
            self.res += 1
        self.dfs(root.left, cur_sum, targetSum)
        self.dfs(root.right, cur_sum, targetSum)
    
    def dfs2(self, root, targetSum):
        if not root:return
        self.dfs(root, 0, targetSum)
        self.dfs2(root.left, targetSum)
        self.dfs2(root.right, targetSum)
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        self.dfs2(root, targetSum)
        return self.res
        