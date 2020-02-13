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
    
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> sequence1 = new ArrayList<>();
        List<Integer> sequence2 = new ArrayList<>();
        dfs(root1, sequence1);
        dfs(root2, sequence2);
        return sequence1.equals(sequence2);
    }
    
    public void dfs(TreeNode root, List<Integer> sequence){
        if (root == null) return;
        
        if(isLeaf(root)){
            sequence.add(root.val);
        }
        dfs(root.left, sequence);
        dfs(root.right, sequence);
    }
    
    public boolean isLeaf(TreeNode node){
        return node.left == null ? node.right == null : false;  
    }
}
