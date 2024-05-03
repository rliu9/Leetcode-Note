# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        def if_same(root1,root2):
            if not root1 and not root2:
                return True
            if (not root1 and root2) or (root1 and not root2):
                return False
            if root1.val != root2.val:
                return False
            return if_same(root1.left,root2.left) and if_same(root1.right,root2.right)
        
        def dfs(root, subroot):
            if not root: return False
            if root.val == subroot.val and if_same(root,subroot):
                return True
            return dfs(root.left, subroot) or dfs(root.right,subroot)
        
        return dfs(root,subRoot)