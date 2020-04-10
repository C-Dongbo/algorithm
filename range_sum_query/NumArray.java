
public class NumArray {

    private int[] nums;

    public NumArray(int[] nums){
        this.nums = nums;
    }

    public int sumRange(int i, int j){
        int sum = 0;
        for(int k = i; k <= j; k++){
            sum += nums[k];
        }
        return sum;
    }


    public static void main(String[] args){
        int[] nums = {-2,0,3,-5,2,-1};
        NumArray obj = new NumArray(nums);
        int i = 0;
        int j = 2;
        System.out.println(obj.sumRange(i,j));
    }
}