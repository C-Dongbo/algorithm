# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        
        def getMinDepth(node, depth):
            if node == None:
                return depth
            depth += 1
            left = getMinDepth(node.left, depth)
            right = getMinDepth(node.right, depth)
            if left ==1 or right == 1:
                if left > right :
                    return left
                elif left < right :
                    return right            

            if node.left == None or node.right == None:
                return max(left,right)
            else:
                return min(left,right)                
                
            return min(left,right)
        return getMinDepth(root, 0)
