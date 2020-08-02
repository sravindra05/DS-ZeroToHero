class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    depth = 0

    def isLeaf(self, node):
        if(node.left == None and node.right == None):
            return 1
        return 0

    def maxDepth(self, root: TreeNode) -> int:
        def helper(node, depth):
            if(node == None):
                return
            if(self.isLeaf(node)):
                self.depth = max(self.depth, depth+1)
                return
            helper(node.left, depth+1)
            helper(node.right, depth+1)
        helper(root, 0)
        return self.depth

    def isSymmetric(self, root: TreeNode) -> bool:

        def isMirror(t1, t2):
            if (t1 == None and t2 == None):
                return 1
            if (t1 == None or t2 == None):
                return 0
            return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

        return isMirror(root, root)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def helper(root, csum):
            if(root == None):
                return 0
            if self.isLeaf(root):
                if(csum+root.val == sum):
                    return 1
                return 0
            return helper(root.left, csum+root.val) or helper(root.right, csum+root.val)
        return helper(root, 0)

    def processChild(self, childNode, prev, leftmost):
        if childNode:

            # If the "prev" pointer is alread set i.e. if we
            # already found atleast one node on the next level,
            # setup its next pointer
            if prev:
                prev.next = childNode
            else:
                # Else it means this child node is the first node
                # we have encountered on the next level, so, we
                # set the leftmost pointer
                leftmost = childNode
            prev = childNode
        return prev, leftmost

    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        # The root node is the only node on the first level
        # and hence its the leftmost node for that level
        leftmost = root

        # We have no idea about the structure of the tree,
        # so, we keep going until we do find the last level.
        # The nodes on the last level won't have any children
        while leftmost:

            # "prev" tracks the latest node on the "next" level
            # while "curr" tracks the latest node on the current
            # level.
            prev, curr = None, leftmost

            # We reset this so that we can re-assign it to the leftmost
            # node of the next level. Also, if there isn't one, this
            # would help break us out of the outermost loop.
            leftmost = None

            # Iterate on the nodes in the current level using
            # the next pointers already established.
            while curr:

                # Process both the children and update the prev
                # and leftmost pointers as necessary.
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)
                curr = curr.next

        return root
