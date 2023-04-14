# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = collections.defaultdict(int)
        def dfs(root, depth):
            if not root:return
            d[depth] = root.val
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root, 0)
        return d.values()