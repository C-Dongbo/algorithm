/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {
        boolean result = false;
        result = isOpposite(root, root);
  	    return result;
    }
    public boolean isOpposite(TreeNode tree1, TreeNode tree2) {
      	if(tree1 == null && tree2 == null) return true;
      	if(tree1 == null || tree2 == null) return false;
      	return tree1.val == tree2.val && isOpposite(tree1.left, tree2.right) && isOpposite(tree1.right, tree2.left);
  }
}
