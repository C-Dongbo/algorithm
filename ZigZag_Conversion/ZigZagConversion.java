package leetCode;

import java.util.ArrayList;
import java.util.List;

public class ZigZagConversion {

	
	public static String convert(String s, int numRows) {
		
		String[] characters = s.split("");
		
		if(numRows == 1) {
			return s;
		}else if(numRows == 2) {
				
			String[] even = new String[(int)Math.round(s.length()/2.0)];
			String[] odd = new String[(int)Math.round(s.length()/2.0)];
			StringBuilder result = new StringBuilder();
			boolean checker = true;
			int i = 0;
			for(String ch : characters) {
				if (checker) {
					even[i] = ch;
					checker = false;
				}else {
					odd[i] = ch;
					checker = true;
					i++;
				}
				
			}
			for(String ch : even) {
				if(ch!=null) {
					result.append(ch);
				}
			}			
			for(String ch : odd) {
				if(ch!=null) {
					result.append(ch);
				}
			}
			return result.toString();
		}
		
		
		int oneLoop = numRows;
		
		int zigzag = numRows - 2;
		int basicLoop = numRows + zigzag;
		int recycle = numRows + zigzag;
		int loopCount = 0;
		int initial = 0;
		int numCol = (int)(Math.ceil(s.length()/(double)basicLoop))*(numRows-1);
//		if(s.length() / numRows > numRows) {
//			numCol = numRows * 3;
//		}else {
//			numCol = numRows * 2;
//		}
//		
		
		String[][] conversionMatrix = new String[numRows][numCol];
		int i = 0;
		int j = 0;
		
		
		for(String ch : characters) {
			if(i < oneLoop) {
				conversionMatrix[i-recycle*initial][j] = ch;
				i++;
				continue;
			}else if(i >= oneLoop && i < basicLoop*(loopCount+1)) {
				j++;
				conversionMatrix[zigzag][j] = ch;
				if(zigzag != 1) {
					zigzag--;
				} 
				i++;
			}
			if (i == basicLoop*(loopCount+1)) {
				initial = 1;
				oneLoop += basicLoop;
				loopCount++;
				recycle = basicLoop*loopCount;
				zigzag = numRows - 2;
				j++;
			}
		}
		StringBuilder result = new StringBuilder();
		for(int k = 0; k<conversionMatrix.length; k++) {
			for(int l = 0; l<conversionMatrix[k].length; l++) {
				if(conversionMatrix[k][l] != null) {
					result.append(conversionMatrix[k][l]);
				}
			}
		}
		return result.toString();
	}
	
	
	public static void main(String[] args) {
		String test = "PAYPALISHIRING";

//		String test = "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.";
		System.out.println(test.length());
		System.out.println(convert(test, 4));
	}
}
