package boj_review.boj_1065;

import java.io.*;
import java.util.*;

public class Main1065 {
	private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static final BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));
	private static StringTokenizer st;
	
	public static boolean isOrderedNum(int n) {
		int len=Integer.toString(n).length();
		int nums[]= new int[len];
		int i=0;
		while(n>0) {
			nums[i++]=n%10;
			n=(int)n/10;
		}
		
		int diff=nums[1]-nums[0];
		for(int j=1; j<len-1; j++) {
			if( diff!=(nums[j+1]-nums[j]) )
				return false;
		}
		return true;
	}
	
	public static void main(String[] args) throws IOException{
		st=new StringTokenizer(br.readLine());
		int n=Integer.parseInt(st.nextToken());
		int answer;
		if(n<100) {
			answer=n;
		}else {
			answer=99;
			for(int i=100;i<=n; i++) {
				if(isOrderedNum(i))
					answer+=1;
			}
		}
		
		bw.write(answer+"\n");
		bw.flush();
		bw.close();
	}
}
