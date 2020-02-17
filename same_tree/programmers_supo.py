# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def dfs(p, q):
            if not p and not q:
                return True
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        tmp = [(p,q)]
        for (p_node, q_node) in tmp:
            if not dfs(p_node, q_node):
                return False
            if p_node:
                tmp.append((p_node.left, q_node.left))
                tmp.append((p_node.right, q_node.right))
        return True