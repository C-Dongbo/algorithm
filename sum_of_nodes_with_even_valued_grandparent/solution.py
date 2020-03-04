# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def getSumVal(node, grandparent, parent):
            sum = 0
            if node is None:
                return 0

            if grandparent is not None and grandparent % 2 == 0:
                sum += node.val

            sum += getSumVal(node.left, parent, node.val)
            sum += getSumVal(node.right, parent, node.val)
            return sum

        return getSumVal(root, None, None)
