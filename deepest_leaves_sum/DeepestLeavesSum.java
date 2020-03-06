package leetCode;

public class DeepestLeavesSum {
	

	public class TreeNode {
	  int val;
	  TreeNode left;
	  TreeNode right;
	  TreeNode(int x) { val = x; }
	}
	
	
	public int deepestLeavesSum(TreeNode root) {
		int level = 1;
		Object[] result = calDeepestSum(root, level);
		
		return (int) result[0];
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
	
}
