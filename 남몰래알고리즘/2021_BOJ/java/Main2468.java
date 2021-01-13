package boj_2468;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main2468 {
	private static BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
	private static Scanner sc= new Scanner(System.in);
	private static StringTokenizer st;
	
	static int answer=1; // 잠기지않은 영역은 최소 1개
	private static int N;
	private static int[] dy= {-1,1,0,0};
	private static int[] dx= {0,0,-1,1};
	private static int[][] map=new int[100][100];
	private static int[] nums= new int[101];
	private static boolean[][] visited;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		N=Integer.parseInt(br.readLine());
		int maxNum=0;
		for(int r=0; r<N; r++) {
			st=new StringTokenizer(br.readLine());
			for(int c=0; c<N; c++) {
				map[r][c]=Integer.parseInt(st.nextToken());
				if(nums[map[r][c]]==0) {
					nums[map[r][c]]=1;
					maxNum=Math.max(map[r][c], maxNum);
				}
			}
		}
		
		for(int i=1;i<=maxNum; i++){
			if(nums[i]==0)
				continue;
			else
				answer=Math.max(answer,countSafetyArea(i));
		}
		
		System.out.println(answer);
	}
	
	public static int countSafetyArea(int dh) {
		int cnt=0;
		visited=new boolean[100][100];
		// dh이하는 물에잠김.
		for(int r=0; r<N; r++) {
			for(int c=0; c<N; c++) {
				if(map[r][c]<=dh || visited[r][c]) //물에잠기거나, 이미 방문한경우
					continue;
				else {
					cnt+=1;
					DFS(r,c, dh);
				}	
			}
		}
		return cnt;
	}
	public static void DFS(int nowY, int nowX, int dh) {
		int nextY, nextX;
		if(!visited[nowY][nowX]) {
			visited[nowY][nowX]=true;
			for(int i=0; i<4; i++) {
				nextY=nowY+dy[i];
				nextX=nowX+dx[i];
				if(isAvailable(nextY, nextX) && (map[nextY][nextX]>dh))
					DFS(nextY, nextX, dh);
			}
		}
	}
	
	public static boolean isAvailable(int y, int x) {
		if((y>=0 && y<N) && (x>=0 && x<N))
			return true;
		return false;
	}
}