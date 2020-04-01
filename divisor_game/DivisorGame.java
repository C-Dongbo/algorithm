package leetCode;

public class DivisorGame {
	
	private static int number = 0;
	private static int check = 0;
	
  public static boolean divisorGame(int N) {
  	
  	number = N;
  	
  	while(number != 1) {
  		number = number - getNum(number);
  	}
  	
    if(check % 2 == 0) {
    	return false;
    }else{
    	return true;
    }
    
  }
  
  public static int getNum(int N) {
  	number = N;
  	check += 1;
  	for(int i=1; i<N; i++) {
  		if(number % i == 0) {
  			return i;
  		}
  	}
  	return 0;
  }
	
	
	public static void main(String[] args) {
		System.out.println(divisorGame(3));
	}
}
