package boj_review.boj_2309;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main2309 {
	private static BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
	private static int heights[]=new int[9];
	public static void main(String[] args) throws NumberFormatException, IOException {
		int sum=0;
		for(int i=0; i<9; i++) {
			heights[i]=Integer.parseInt(br.readLine());
			sum+=heights[i];
		}
		
		ArrayList<Integer> answer=new ArrayList<Integer>();
		for(int i=0; i<8; i++) 
		{ //첫번째 난장이
			for(int j=i+1; j<9; j++) 
			{//두번째 난장이
				if( sum-(heights[i]+heights[j])==100 ) 
				{
					//두 난장이의 키를 제외한 일곱난장이의 키의 합이 100이면
					for(int k=0;k<9; k++) {
						if( k==i || k==j ) 
							continue;
						else{//i,j번째난장이를 제외한 나머지만 리스트에 넣는다.
							answer.add(heights[k]);
						}
					}
					
					//answer에 저장된 난장이키들을 오름차순 정렬을 한다.
					Collections.sort(answer);
					
					//정렬된 내용을 출력한다.
					for(int h:answer) {
						System.out.println(h);
					}
					
					return;
				}
			}
		}		
	}
}
