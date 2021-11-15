# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = {}
        def dfs(root, row):
            if not root: return
            ans[row] = root.val
            dfs(root.left, row+1)
            dfs(root.right, row+1)
        dfs(root, 0)
        return list(ans.values())
