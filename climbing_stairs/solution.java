class Solution {
    public static int climbStairs(int n) {
        int[] memoization = new int [n+1];
        return recursive(0,n,memoization);
    }

    public static int recursive(int step, int n, int[] memo){
        if (step > n){
            return 0;
        }
        if (step == n){
            return 1;
        }
        if(memo[step] > 0){
            return memo[step];
        }
        memo[step] = recursive(step+1, n, memo) + recursive(step+2, n, memo);

        return memo[step];
    }



    public static void main(String[] args){
        System.out.println(climbStairs(5));
    }
}