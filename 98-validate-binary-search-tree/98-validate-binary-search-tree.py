# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, Min, Max):
            if not root:return True
            if Min < root.val < Max:
                return dfs(root.left, Min, root.val) and dfs(root.right, root.val, Max)
            return False
        return dfs(root, float('-inf'), float('inf'))