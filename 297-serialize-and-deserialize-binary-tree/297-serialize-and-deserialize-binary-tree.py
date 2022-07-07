# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append('none')
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def preorder_decode():
            if data[self.curr_idx] == 'none':
                self.curr_idx += 1
                return
            node = TreeNode(int(data[self.curr_idx]))
            self.curr_idx += 1
            node.left = preorder_decode()
            node.right = preorder_decode()
            return node
        
        data = data.split(",")
        self.curr_idx, n = 0, len(data)
        return preorder_decode()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))