# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.move = 0
        
        def dfs(node: TreeNode):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.move += abs(left) + abs(right)
            return node.val + left + right -1
        
        dfs(root)
        return self.move
