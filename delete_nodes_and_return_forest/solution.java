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
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        List<TreeNode> result = new ArrayList<>();
        List<Integer> delete = Arrays.stream(to_delete).boxed().collect(Collectors.toList());
        
        TreeNode node = dfs(root, delete, result);
        if (node != null){
            result.add(node);
        }
        return result;
    }
    
    public TreeNode dfs (TreeNode node, List<Integer> delete, List<TreeNode> result) {
        
        if (node == null) {
            return null;
        }

        node.left = dfs(node.left, delete, result);
        node.right = dfs(node.right, delete, result);

        if (delete.contains(node.val)) {
            if (node.left != null) {
                result.add(node.left);
            }
            if (node.right != null) {
                result.add(node.right);
            }

            return null;
        } else {
            return node;
        }
    }
}
