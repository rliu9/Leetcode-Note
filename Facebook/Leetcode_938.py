# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.res += node.val
                dfs(node.left)
                dfs(node.right)
        self.res = 0
        dfs(root)
        return self.res
