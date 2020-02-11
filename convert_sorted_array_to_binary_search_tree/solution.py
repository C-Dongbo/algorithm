# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def BST_insert_balanced(root, nums):
    if nums == []:
        return None
    else:
        idx = len(nums)//2
        root = TreeNode(nums[idx])
        root.left = BST_insert_balanced(root.left,nums[:idx])
        root.right = BST_insert_balanced(root.right, nums[idx+1:])
        return root

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        newRoot = TreeNode(0)
        return BST_insert_balanced(newRoot, nums)
