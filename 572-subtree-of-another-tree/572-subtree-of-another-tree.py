# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def if_same(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2 or root1.val != root2.val:
                return False
            return if_same(root1.left, root2.left) and if_same(root1.right, root2.right)
        
        def dfs(root, subRoot):
            if not root:
                return False
            if root.val == subRoot.val and if_same(root, subRoot):
                return True
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        if not subRoot:
            return True
        return dfs(root, subRoot)