# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def preorderTraversal(self, root: TreeNode):
        if(root != None):
            l = []
            l.append(root.val)
            l.extend(self.preorderTraversal(root.left))
            l.extend(self.preorderTraversal(root.right))
            return l
        return []

    def inorderTraversal(self, root: TreeNode):
        if(root != None):
            l = []
            l.extend(self.inorderTraversal(root.left))
            l.append(root.val)
            l.extend(self.inorderTraversal(root.right))
            return l
        return []

    def postorderTraversal(self, root: TreeNode):
        if(root != None):
            l = []
            l.extend(self.postorderTraversal(root.left))
            l.extend(self.postorderTraversal(root.right))
            l.append(root.val)
            return l
        return []

    def levelOrder(self, root):
        levels = []
        if not root:
            return levels

        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels
