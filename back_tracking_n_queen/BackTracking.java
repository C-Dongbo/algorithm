package dummy;

public class BackTracking {
	
	private static int[] column;
	private static int n;
	private static int result;
	
	public static void dfs(int row) {
		
		if(row > n) {
			result ++;
		}else {
			for(int i=1; i<=n; i++) {
				column[row] = i;
				if(isPossible(row)) {
					dfs(row + 1);
				}else {
					column[row] = 0;
				}
			}
		}
	}
	
	public static boolean isPossible(int row) {
		for(int i=1; i<row; i++) {
			if(column[i] == column[row]) {
				return false;
			}
			if(Math.abs(column[i]-column[row]) == Math.abs(i-row)) {
				return false;
			}
		}
		return true;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		n = 4; // size of chess board
		
		for(int i=1; i<=n; i++) {
			column = new int[n+1];
			column[1] = i;
			dfs(2);
		}
		System.out.println(result);
		
	}

}
