package leetCode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;




	

public class Solution2 {

	public static class TreeNode {
	  int val;
	  TreeNode left;
	  TreeNode right;
	  TreeNode(int x) { val = x; }
	}
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode test = new TreeNode(3);
		test.left = new TreeNode(9);
		test.right = new TreeNode(20);
		test.right.left = new TreeNode(15);
		test.right.right = new TreeNode(7);
		System.out.println(levelOrderBottom(test).toString());
		
	}

	
	

	
  public static List<List<Integer>> levelOrderBottom(TreeNode root) {
  	
    List<List<Integer>> result = new ArrayList<List<Integer>>();
    
    if(root == null){
        return result;
    }
 
    LinkedList<TreeNode> current = new LinkedList<TreeNode>();
    LinkedList<TreeNode> next = new LinkedList<TreeNode>();
    current.offer(root);
    
    ArrayList<Integer> numberList = new ArrayList<Integer>();
 
    // need to track when each level starts
    while(!current.isEmpty()){
        TreeNode head = current.poll();
 
        numberList.add(head.val);
 
        if(head.left != null){
            next.offer(head.left);
        }
        if(head.right!= null){
            next.offer(head.right);
        }
 
        if(current.isEmpty()){
            current = next;
            next = new LinkedList<TreeNode>();
            result.add(numberList);
            numberList = new ArrayList<Integer>();
        }
    }
    Collections.reverse(result);
    return result;
//    List<List<Integer>> reversedResult = new ArrayList<List<Integer>>();
//    for(int i=result.size()-1; i>=0; i--){
//        reversedResult.add(result.get(i));
//    }
// 
//    return reversedResult;
  }
}
