# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def getMaxDepth(node, depth):
            if node == None:
                return depth
            depth+=1
            left = getMaxDepth(node.left, depth)
            right = getMaxDepth(node.right, depth)
            
            return max(left,right)
            
        return getMaxDepth(root, 0)
