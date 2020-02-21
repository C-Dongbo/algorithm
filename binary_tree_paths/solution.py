# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    		
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        result = []
        
        def dfs(node, path, result):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                result.append('->'.join(path))
            if node.left:
                dfs(node.left, path, result)
            if node.right:
                dfs(node.right, path, result)
            path.pop()

        path = []
        dfs(root, path, result)
        return result



