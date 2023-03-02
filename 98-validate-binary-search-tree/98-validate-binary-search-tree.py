# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, Max, Min):
            if not root:return True
            if not (Min < root.val < Max):return False
            return dfs(root.left, root.val, Min) and dfs(root.right, Max, root.val)
        
        return dfs(root, float('inf'), float('-inf'))