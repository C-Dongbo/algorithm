package leetCode;

import java.util.HashMap;
import java.util.Map;

public class CousinsInBinaryTree {

	static Map<Integer, TreeNode> parentMap = new HashMap<>();
	static Map<Integer, Integer> depthMap = new HashMap<>();
		
	public class TreeNode {
	  int val;
	  TreeNode left;
	  TreeNode right;
	  TreeNode(int x) { val = x; }
	}
	
	
  public boolean isCousins(TreeNode root, int x, int y) {
    boolean result = true;
    
    dfs(root, null);
    if (depthMap.get(x) == depthMap.get(y) & parentMap.get(x) != parentMap.get(y)) {
    	return result;
    }
    return false;
  }
  
  public void dfs(TreeNode node, TreeNode parent) {
  	if(node != null) {
  		depthMap.put(node.val, (parent == null)? 0 : depthMap.get(parent.val) + 1);
  		parentMap.put(node.val, parent);
  		dfs(node.left, node);
  		dfs(node.right, node);
  	}
  }

}
