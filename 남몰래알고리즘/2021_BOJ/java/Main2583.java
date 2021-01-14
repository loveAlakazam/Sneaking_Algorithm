package boj_2583;

import java.io.*;
import java.util.*;

class Point{
	int x;
	int y;
	public Point(int y, int x) {
		this.x=x;
		this.y=y;
	}
}

public class Main {
	private static int N;
	private static BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
	private static Scanner sc = new Scanner(System.in);
	private static StringTokenizer st;
	
	private static int [][] map;
	private static boolean[][] visited;
	private static int[]dy= {-1,1,0,0};
	private static int[]dx= {0,0,-1,1};
	
	
	private static Deque<Point> q=new LinkedList<Point>();
	public static void BFS(int y, int x, int dh) {
		int nextY, nextX;
		q.add(new Point(y,x));
		while(!q.isEmpty()) {
			Point p= q.pollFirst();
			
			// 아직 방문안한상태 & 아직 잠기지 않은 상태(높이가 dh보다 큼)
			if(!visited[p.y][p.x] && map[p.y][p.x]>dh) {
				visited[p.y][p.x]=true;
				for(int i=0; i<4; i++ ) {
					nextY=p.y+dy[i];
					nextX=p.x+dx[i];
					
					if((nextY>=0 && nextY<N)&&(nextX>=0 && nextX<N))
						if(!visited[nextY][nextX] && map[nextY][nextX]>dh)
							q.addLast(new Point(nextY, nextX));
				}
			}
			
		}
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		N=Integer.parseInt(br.readLine());
		int max_val=0;
		int min_val=101;
		map=new int [N][N];
	
		for(int r=0; r<N; r++) {
			st=new StringTokenizer(br.readLine());
			for(int c=0; c<N; c++) {
				map[r][c]=Integer.parseInt(st.nextToken());
				max_val=Math.max(max_val, map[r][c]);
				min_val=Math.min(min_val, map[r][c]);
			}
		}
		
		int answer=1;
		int cnt;
		for(int i=min_val; i<=max_val; i++) {
			visited=new boolean[N][N];
			cnt=0;
			for(int r=0; r<N; r++) {
				for(int c=0; c<N; c++) {
					if(!visited[r][c] && map[r][c]>i) {
						BFS(r,c,i);
						cnt++;
					}
				}
			}
			answer=Math.max(answer, cnt);
		}
		System.out.println(answer);
	}
}
