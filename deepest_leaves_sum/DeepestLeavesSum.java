package leetCode;

import javax.xml.ws.Response;

public class DeepestLeavesSum {
	

	public class TreeNode {
	  int val;
	  TreeNode left;
	  TreeNode right;
	  TreeNode(int x) { val = x; }
	}
	
	public class Response{
		int val;
		int level;
		public Response(int val, int level) {
			this.val = val;
			this.level = level;
		}
	}
	
	public int deepestLeavesSum(TreeNode root) {
		int level = 1;
		Response result = calDeepestSum2(root, level);
		
		return result.val;
	}
	
	public Object[] calDeepestSum(TreeNode node, int level) {
		if (node == null) {
			level -= 1; 
			return new Object[] {0, level};
		}
		Object[] left = calDeepestSum(node.left, level+1);
		Object[] right = calDeepestSum(node.right, level+1);
		int maxDepth = Math.max((int) left[1], (int) right[1]);
		int sum = 0;
		if (level == maxDepth) sum += node.val;
		if ((int)left[1] == maxDepth) sum += (int) left[0];
		if ((int)right[1] == maxDepth) sum += (int) right[0];
		return new Object[] {sum, maxDepth};
	}
	
	public Response calDeepestSum2(TreeNode node, int level) {
		if (node == null) {
			level -= 1; 
			return new Response(0,level);
		}
		Response left = calDeepestSum2(node.left, level+1);
		Response right = calDeepestSum2(node.right, level+1);
		int maxDepth = Math.max(left.level, right.level);
		int sum = 0;
		if (level == maxDepth) sum += node.val;
		if (left.level == maxDepth) sum += left.val;
		if (right.level == maxDepth) sum += right.val;
		return new Response(sum, maxDepth);
	}
}
