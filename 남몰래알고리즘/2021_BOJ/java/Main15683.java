package boj_15683;

import java.io.*;
import java.util.*;

class Camera{
	int y, x, kind;
	public Camera(int y, int x, int kind) {
		this.y=y;
		this.x=x;
		this.kind=kind;
	}
}
public class Main {
	private static BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
	private static Scanner sc= new Scanner(System.in);
	private static StringTokenizer st;
	
	private static int N, M;
	private static int MAX=8;
	private static int [][] map=new int [MAX][MAX];
	private static int dy[]= {0,-1,0,1};
	private static int dx[]= {-1,0,1,0};
	private static ArrayList<Camera> cameraList=new ArrayList<Camera>();
	private static int answer=MAX*MAX; //사각지대의 최소크기
	
	public static void main(String[] args) throws IOException  {
		st=new StringTokenizer(br.readLine());
		N=Integer.parseInt(st.nextToken());
		M=Integer.parseInt(st.nextToken());
		
		// map초기화
		for(int r=0; r<N; r++) {
			st=new StringTokenizer(br.readLine());
			int c=0;
			while(st.hasMoreTokens()) {
				map[r][c]=Integer.parseInt(st.nextToken());
				
				//값이 1~5는 카메라이다.
				//카메라 객체를 만들어서, 카메라 리스트에 넣는다.(카메라개수를 알기위해..)
				if(map[r][c]>=1 && map[r][c]<=5)
					cameraList.add(new Camera(r,c,map[r][c]));
				c++;
			}
		}
		
		search(0, map); // 검색시작(발견한 카메라개수:0개), map배열을 이전배열로한다.
		System.out.println(answer);
	}
	
	public static void search(int cameraCnt, int[][] prevMap) {
		if(cameraCnt==cameraList.size()) {
			//감시카메라 모두 발견할 경우
			//영역개수를 구한다.
			int cnt=0;
			for(int r=0; r<N; r++)
				for(int c=0; c<M; c++)
					if(prevMap[r][c]==0)
						cnt++;
			answer=Math.min(answer, cnt);
			return;
		}
		
		//cameraCnt: 0번 인덱스 카메라 ~ cameraList.size()-1 번 인덱스 카메라를 탐색함.
		//cameraList 에 저장된 카메라들을 탐색한다.
		Camera camera= cameraList.get(cameraCnt);
		int cameraKind= camera.kind; //1~5
		int y=camera.y;
		int x=camera.x;
		
		int [][]copyMap=new int[N][M];
		
		
		switch(cameraKind) {
			case 1:{
				//1개 방향
				//4종류를 탐색할 수 있음.
				for(int d=0; d<4; d++) {//d: 탐색 방향 인덱스번호
					//이전배열의 값을 그대로 복사한다.
					for(int r=0; r<N; r++)
						for(int c=0; c<M; c++)
							copyMap[r][c]=prevMap[r][c];
					
					DFS(y,x, d , copyMap); //4종류를 각각 탐색한다.
					search(cameraCnt+1, copyMap); //탐색완료. 다음카메라에서 탐색한 결과를 구한다...
				}
			}break;
			case 2:{
				//2개방향
				//2종류를 탐색할 수 있음.
				for(int d=0; d<2; d++) {
					//이전배열의 값을 그대로 복사한다.
					for(int r=0; r<N; r++)
						copyMap[r]=Arrays.copyOf(prevMap[r], M);
					
					DFS(y,x, d, copyMap);
					DFS(y,x, d+2, copyMap);
					search(cameraCnt+1, copyMap);
				}
			}break;
			case 3:{
				//2개방향
				//4종류를 탐색할 수 잇음.
				for(int d=0; d<4; d++) {
					for(int r=0; r<N; r++)
						copyMap[r]=Arrays.copyOf(prevMap[r], M);
					DFS(y,x, d, copyMap);
					DFS(y,x, (d+1)%4, copyMap);
					search(cameraCnt+1, copyMap);
				}
			}break;
			case 4:{
				//3개방향
				//4종류를 탐색할 수 있음.
				for(int d=0; d<4; d++) {
					for(int r=0; r<N; r++)
						copyMap[r]=Arrays.copyOf(prevMap[r], M);
					
					DFS(y,x, d, copyMap);
					DFS(y,x, (d+1)%4, copyMap);
					DFS(y,x, (d+2)%4, copyMap);
					search(cameraCnt+1, copyMap);
				}
			}break;
			case 5:{
				//4개방향
				//1종류를 탐색할 수 있음.
				for(int r=0; r<N; r++)
					copyMap[r]=Arrays.copyOf(prevMap[r], M);
				DFS(y,x,0,copyMap);
				DFS(y,x,1,copyMap);
				DFS(y,x,2,copyMap);
				DFS(y,x,3,copyMap);
				search(cameraCnt+1, copyMap);
			}break;
		}
	}
	
	public static void DFS(int y, int x, int direction, int [][]tmp) {
		int nextY=y+dy[direction];
		int nextX=x+dx[direction];
	
		if((nextY>=0 && nextY<N)&&(nextX>=0 && nextX<M)) {
			if(tmp[nextY][nextX]==6)//벽을 마주칠경우
				return;
			tmp[nextY][nextX]=7;
			DFS(nextY, nextX, direction, tmp);
		}
	}
	
}
