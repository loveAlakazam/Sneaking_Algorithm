package boj_review.boj_14502;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;


class Virus{
	int y, x;
	public Virus(int y, int x) {
		this.y=y;
		this.x=x;
	}
}

public class Main14502 {
	private static final BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
	private static final BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));
	
	private static StringTokenizer st;
	
	private static int N,M;
	private static boolean [][] visited;
	private static int [][] copiedMap;
	private static int [][] map;
	
	private static int dy[]= {-1,1,0,0};
	private static int dx[]= {0,0,-1,1};
	private static int answer=0;
	private static Queue<Virus> q=new LinkedList<Virus>();
	
	
	public static void main(String[] args) throws IOException {
		st=new StringTokenizer(br.readLine());
		N=Integer.parseInt(st.nextToken());
		M=Integer.parseInt(st.nextToken());
		
		map=new int[N][M];
		copiedMap=new int[N][M];
		for(int r=0; r<N; r++) {
			st=new StringTokenizer(br.readLine());
			for(int c=0; c<M; c++)
				map[r][c]=Integer.parseInt(st.nextToken());
		}
		
		for(int r=0; r<N; r++) {
			for(int c=0; c<M; c++) {
				if(map[r][c]==0) {//첫번째 벽
					
					//원본맵을 복사하여 복사본을 만든다.
					for(int y=0; y<N; y++) {
						copiedMap[y]=Arrays.copyOf(map[y], M);
					}
					
					copiedMap[r][c]=1; //첫번째 벽을 세운다.
					makeWall(1); //벽이 3개가 될때까지 세운후에 안전영역의 개수를 구한다.
					copiedMap[r][c]=0; //벽을 허문다.
				}
			}
		}
		
		bw.write(answer+"\n");
		bw.flush();
		bw.close();
	}
	
	public static void makeWall(int wallCnt) {
		if(wallCnt==3) {
			//벽의개수가 3개이면, 바이러스를 퍼뜨린후에 안전영역개수를 구한다.
			BFS(copiedMap);
			return;
		}
		
		for(int r=0; r<N; r++) {
			for(int c=0;c<M; c++) {
				if(copiedMap[r][c]==0) {
					copiedMap[r][c]=1;//두번째(세번째) 벽을 세운다.
					makeWall(wallCnt+1);
					copiedMap[r][c]=0; //벽을 허문다.
				}
			}
		}
		
	}
	
	public static void BFS(int [][] map) {
		//바이러스 퍼뜨린 후의 맵 초기화
		int afterSpreadMap[][]=new int[N][M];
		
		//초기 바이러스 위치를 찾는다.
		for(int r=0; r<N; r++) {
			for(int c=0; c<M; c++) {
				afterSpreadMap[r][c]=map[r][c];
				if(map[r][c]==2)
					q.add(new Virus(r,c));
			}
		}
		
		//퍼뜨린다.
		while(!q.isEmpty()) {
			Virus v=q.poll();

			for(int i=0; i<4; i++) {
				int nextY=v.y+dy[i];
				int nextX=v.x+dx[i];
				if((nextY>=0 && nextY<N) && (nextX>=0 && nextX<M)) {
					if(afterSpreadMap[nextY][nextX]==0) {
						afterSpreadMap[nextY][nextX]=2;//감염을 시킨다.
						q.add(new Virus(nextY,nextX));
					}
				}
			}
		}
		
		int cnt=0;
		
		//퍼뜨린후에 안전영역 개수를 찾는다.
		for(int r=0; r<N; r++)
			for(int c=0; c<M; c++)
				if(afterSpreadMap[r][c]==0)
					cnt+=1;
		answer=Math.max(answer, cnt);
	}
}
