# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root,last,cur):
            if not root:return
            if root.val == last.val + 1 or root == last:
                self.res = max(self.res, cur)
                return dfs(root.left,root,cur+1) or dfs(root.right,root,cur+1)
            else:
                return dfs(root.left,root,2) or dfs(root.right,root,2)
        dfs(root,root,1)
        return self.res
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
        