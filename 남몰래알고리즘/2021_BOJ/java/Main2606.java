package boj_2606_bfs;

import java.io.*;
import java.util.*;

public class Main {
	private static BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
	private static Scanner sc= new Scanner(System.in);
	private static StringTokenizer st;
	private static int N,M;
	private static Deque<Integer> q= new LinkedList<>();
	private static boolean[] visited;
	private static boolean[][] connection;
	
	public static int BFS() {
		int cnt=0;
		int nowCom;
		while(!q.isEmpty()) {
			nowCom=q.pollFirst();
			if(!visited[nowCom-1]) {
				visited[nowCom-1]=true;
				cnt++;
				
				for(int i=0;i<N; i++) {
					if(!visited[i] && connection[nowCom-1][i])
						q.addLast(i+1);
				}
			}
		}
		return cnt;
	}
	
	public static void main(String[]args) throws NumberFormatException, IOException {
		N=Integer.parseInt(br.readLine());
		M=Integer.parseInt(br.readLine());
		visited=new boolean[N];
		connection=new boolean[N][N];
		int com1, com2;
		for(int i=0; i<M; i++) {
			st=new StringTokenizer(br.readLine());
			com1=Integer.parseInt(st.nextToken());
			com2=Integer.parseInt(st.nextToken());
			connection[com1-1][com2-1]=connection[com2-1][com1-1]=true;	
		}
		
		q.addLast(1);
		int result=BFS();
		System.out.println(result-1);
	}
}
