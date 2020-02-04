package leetCode;

public class String2Integer {

	
	
	public static int solution(String str) {
		String condition = "+-"; 
		String[] chars = str.split(" ");
		StringBuilder tmp = new StringBuilder();
		String buho = "";
		String prebuho = "";
		String preChar = "";
		int result = 0;
		int i = 0;
		
		for (String ch : chars) {
			for(String c : ch.split("")) {
				if(c.equals("-") || c.equals("+")) {
					if (!prebuho.equals("") && !isNumeric(preChar)) {
						return 0;
					}
					if(!prebuho.equals("")) {
						break;
					}else if(prebuho.equals("") && condition.contains(c) && tmp.length() !=0) {
						break;
					}
					buho = c;
				}else if (i == 0 && !isNumeric(c) && !c.equals("+") && !c.equals("")) {
					return 0;
				}else if(isNumeric(c)) {
					tmp.append(c);
				}else {
					break;
				}
				if(condition.contains(c) && tmp.length() != 0){
					break;
				}
				prebuho = buho;
				preChar = c;
				i++;
				
			}
			
			if(tmp.length() != 0) {
				break;
			}else if(!prebuho.equals("") && tmp.length() == 0) {
				break;
			}
		}
		try {
			result = Integer.parseInt(tmp.toString());
		}catch(Exception e) {
			if(tmp.length()==0) {
				return 0;
			}
			if(buho.equals("-")) {
				return (int) -Math.pow(2, 31);
			}else {
				return (int) Math.pow(2, 31);
			}
			
		}
		if(buho.equals("-")) {
			return -result;
		}else {
			return result;
		}
	}
	
	
	
	public static boolean isNumeric(String s) {
	  try {
	      Double.parseDouble(s);
	      return true;
	  } catch(NumberFormatException e) {
	      return false;
	  }
	}
	

	public static void main(String[] args) {
		String test = "13-8";
		System.out.println(solution(test));

	}

}
