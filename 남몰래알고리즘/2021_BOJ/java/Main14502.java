package boj_14502;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.StringTokenizer;

class Point{
	int y, x;
	public Point(int y, int x) {
		this.y=y;
		this.x=x;
	}
}

public class Main{
	private static BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
	private static Scanner sc=new Scanner(System.in);
	private static StringTokenizer st;
	
	private static int MAX=8;
	private static int[][] map= new int[MAX][MAX];
	private static int[][] tmp= new int[MAX][MAX];
	private static Deque<Point> queue=new LinkedList<Point>();
	
	private static int answer=0; //안전영역 최대개수
	private static int dy[]= {-1,1,0,0};
	private static int dx[]= {0,0,-1,1};
	
	private static int N,M;
	public static void main(String[] args) throws IOException {
		st=new StringTokenizer(br.readLine());
		N=Integer.parseInt(st.nextToken());
		M=Integer.parseInt(st.nextToken());
		
		// 초기화
		for(int r=0; r<N; r++) {
			st=new StringTokenizer(br.readLine());
			for(int c=0; c<M; c++) {
				map[r][c]=Integer.parseInt(st.nextToken());
			}
		}
		
		for(int y=0; y<N; y++) 
		{
			for(int x=0; x<M; x++) 
			{
				if(map[y][x]==0) 
				{//현재 위치가 빈칸일때
					//1. 복사본을 먼저 만든다.
					for(int r=0; r<N; r++) {
						for(int c=0; c<M; c++)
							tmp[r][c]=map[r][c];
					}
					
					//2. 복사본(tmp)의 현위치(y행,x열)에서 벽을 세운다.
					tmp[y][x]=1;
					
					//3. 벽3개를 세워서, 안전영역의 개수를 구한다.
					addWall(1);
					
					//4. 현위치에서 세운벽을 허문다.
					tmp[y][x]=0;
				}
			}
		}
		
		
		System.out.println(answer);
	}
	
	public static void addWall(int wallCnt) {
		if(wallCnt==3) {
			// 현재 세운벽의개수가 3개라면
			BFS(); //바이러스를 퍼뜨린후, 안전영역(0)의 개수를 구한다.
			return;
		}
		
		// 벽개수(WallCnt)가 3개가 될때까지 빈칸을 찾아서 벽을 세운다.
		for(int r=0; r<N; r++) {
			for(int c=0; c<M; c++) {
				if(tmp[r][c]==0) {
					tmp[r][c]=1; //벽을세운다.
					addWall(wallCnt+1); //재귀함수시행
					tmp[r][c]=0; //벽을 허문다.
				}
			}
		}
	}
	
	public static void BFS() {
		//tmp에서 초기 바이러스 위치를 구하여, 바이러스 위치를 큐에 넣는다.
		for(int r=0; r<N; r++) {
			for(int c=0; c<M; c++) {
				if(map[r][c]==2) {
					queue.add(new Point(r,c));
				}
			}
		}
		
		// afterSpread는 바이러스가 퍼진후의 모습이다.
		int [][] afterSpread=new int[MAX][MAX];
		for(int r=0; r<N; r++)
			for(int c=0; c<M; c++)
				afterSpread[r][c]=tmp[r][c];
		
		//바이러스를 퍼뜨린다.
		int nextX, nextY;
		while(!queue.isEmpty()) {
			Point p= queue.poll();
			
			for(int i=0; i<4; i++) {
				nextY=p.y+dy[i];
				nextX=p.x+dx[i];
				
				if((nextY>=0 && nextY<N)&&(nextX>=0 && nextX<M)) {
					if( afterSpread[nextY][nextX]==0) {
						afterSpread[nextY][nextX]=2;//바이러스 감염
						queue.add(new Point(nextY,nextX));
					}
				}
			}
		}
		
		// 안전영역(0) 개수를 구한다.
		int cnt=0;
		for(int r=0; r<N; r++)
			for(int c=0; c<M; c++)
				if(afterSpread[r][c]==0)
					cnt+=1;
		answer=Math.max(answer, cnt);
	}

}