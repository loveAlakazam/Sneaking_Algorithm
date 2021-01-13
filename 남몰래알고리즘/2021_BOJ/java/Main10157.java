package boj_10157;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main10157 {
	private static BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
	private static BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));
	private static Scanner sc= new Scanner(System.in);
	private static StringTokenizer st;
	
	private static int col, row, K, dy, dx;
	private static int[] dY= {-1,0,1,0};
	private static int[] dX= {0,1,0,-1};
	private static boolean[][] visited=new boolean[1000][1000];
	private static int now=1;
	
	public static boolean isAvailable(int y, int x) {
		if((y>=0 && y<row) && (x>=0 && x<col))
			return true;
		return false;
	}
	
	public static String goToK(int nowY, int nowX, int nowVal, int direction) {
		if (K> col*row)
			return "0";
		
		if(nowVal==K)
			return (nowX+1)+" "+(row-nowY);
		
		if(!visited[nowY][nowX]) {
			visited[nowY][nowX]=true;
			direction%=4;
			dy=nowY+dY[direction];
			dx=nowX+dX[direction];
			if(isAvailable(dy,dx) && !visited[dy][dx])
				return goToK(dy, dx, nowVal+1, direction);
		}
		visited[nowY][nowX]=false;
		return goToK(nowY, nowX, nowVal, direction+1);
	}
	
	public static void main(String[] args) throws IOException {
		st= new StringTokenizer(br.readLine());
		col=Integer.parseInt(st.nextToken());
		row=Integer.parseInt(st.nextToken());
		
		K= Integer.parseInt(br.readLine());
		String result=goToK(row-1,0,1,0);
		System.out.println(result);
	}
}
