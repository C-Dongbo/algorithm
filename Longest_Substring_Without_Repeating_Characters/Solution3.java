package leetCode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Solution3 {

  public static int lengthOfLongestSubstring(String s) {
    int result = 0;
    
    Set<Character> tmp = new HashSet<>();
    int n = s.length();
  
    if(s.length() == 0) {
    	return 0;
    }else if(s.length() == 1) {
    	return 1;
    }
     
    int j = 0;
    int i = 0;
    while(i < n && j < n) {
    	if(!tmp.contains(s.charAt(j))) {
    		tmp.add(s.charAt(j));
    		j++;
    		result = Math.max(result, j-i);
    	}else {
    		tmp.remove(s.charAt(i));
    		i++;
    	}
    }
    return result;
  }

  public static int lengthOfLongestSubstring2(String s) {
    int result = 0;
    
    Map<Character, Integer> tmp = new HashMap<>();
    int n = s.length();
  
    if(s.length() == 0) {
    	return 0;
    }else if(s.length() == 1) {
    	return 1;
    }
    int j = 0;
    for (int i = 0; i<n; i++) {
    	if(tmp.containsKey(s.charAt(i))) {
    		j = Math.max(tmp.get(s.charAt(j)), i);
    	}else {
    		tmp.put(s.charAt(i), i);
    	}
    }
    return result;
  }
  
  
  public static void main(String[] args) {
  	String test = "dvdf";
//  	String test = "abcabcbb";
  	
  	System.out.println(lengthOfLongestSubstring(test));
  }
}
