package boj_review.boj_1753;

import java.io.*;
import java.util.*;


class Node implements Comparable<Node>{
	int end, weight;
	public Node(int end, int weight) {
		this.end=end;
		this.weight= weight;
	}
	
	@Override
	public int compareTo(Node n) {
		return this.weight-n.weight;
	}
}

public class Main1753 {
	private static final BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
	private static final int INF= Integer.MAX_VALUE;
	
	private static StringTokenizer st;
	private static PriorityQueue<Node> q=new PriorityQueue<Node>();
	
	private static int V,E;
	private static int S;//시작점
	private static boolean[] visited;
	private static ArrayList<ArrayList<Node>> maps; 
	private static int d[];
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		st=new StringTokenizer(br.readLine());
		V=Integer.parseInt(st.nextToken());
		E=Integer.parseInt(st.nextToken());
		S=Integer.parseInt(br.readLine());
		
		// 방문리스트
		visited= new boolean[V+1];
		
		// 최단거리
		d=new int[V+1];
		Arrays.fill(d, INF); //d를 INF로 초기화
		
		
		maps=new ArrayList<>();
		for(int i=0; i<V+1; i++)
			maps.add(new ArrayList<Node>());
		
		int start, end, weight;
		for(int i=0; i<E; i++) {
			st=new StringTokenizer(br.readLine());
			start=Integer.parseInt(st.nextToken());
			end=Integer.parseInt(st.nextToken());
			weight=Integer.parseInt(st.nextToken());
			
			Node edge= new Node(end,weight);
			maps.get(start).add(edge);
		}
		
		dijkstra(S);
		
		for(int i=1; i<=V; i++) {
			if(d[i]==INF)
				System.out.println("INF");
			else
				System.out.println(d[i]);
		}
	}

	
	public static void dijkstra(int start) {
		d[start]=0;
		q.add(new Node(start, 0));
		while(!q.isEmpty()) {
			Node node=q.poll();
			int now= node.end;
			visited[now]=true;
		
			for(Node nextNode : maps.get(now)) {
				int next=nextNode.end;
				int weight= nextNode.weight;
				
				if(!visited[next]) {
					int cost=d[now]+weight;
					if(cost<d[next]) {
						d[next]=cost;
						q.add(new Node(next,cost));
					}
				}
			}
		}
	}
}
