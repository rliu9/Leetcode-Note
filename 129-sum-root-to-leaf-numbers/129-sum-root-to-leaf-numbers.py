# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root, n):
            if not root:return
            if not root.left and not root.right:
                self.res += int(n+str(root.val))
                return
            return dfs(root.left, n+str(root.val)) or dfs(root.right, n+str(root.val))
        dfs(root, '')
        return self.res