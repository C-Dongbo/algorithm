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
    
    int getHeight(TreeNode node) {
		if(node == null) {
			return 0;
		}
		return 1 + Math.max(getHeight(node.left), getHeight(node.right));
	}
    
    public boolean isBalanced(TreeNode root) {
        if(root == null) {
            return true;
        }
        int leftHeight = getHeight(root.left);
        int rightHeight = getHeight(root.right);

        if(Math.abs(leftHeight-rightHeight) <=1 && isBalanced(root.left) && isBalanced(root.right)) {
            return true;
        }
        return false;
    }
}
