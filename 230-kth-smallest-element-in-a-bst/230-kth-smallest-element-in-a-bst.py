# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []
        def dfs(root):
            if not root:return
            l.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        heapq.heapify(l)
        return heapq.nsmallest(k, l)[-1]
    
    # O(n)
    # O(n)