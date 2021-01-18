# 힙큐를 사용한 다익스트라
# 20000개 이상의 노드중 최단거리를 탐색하려고할때 사용가능.
import sys
import heapq
input=sys.stdin.readline
INF=float('inf')

# V: 정점개수(Vertex), E: 간선(Edge)
V,E= map(int, input().split())

# 정점 시작 번호
start= int(input()) 
graph=[ [] for _ in range(V+1)] #그래프 인덱스: 정점
d=[INF]*(V+1) #d[정점]=정점까지의 최소거리값

for _ in range(E):
    s,e,w= map(int,input().split())
    graph[s].append((e,w))
                 
# 다익스트라 - 힙큐를 이용.
def dijkstra(start):
    d[start]=0
    q=[]
    heapq.heappush(q, (0, start)) #큐에 넣는다 (최단거리:0, 노드번호:start)
    while q:
        # 최단거리가 짧은 노드에 대한 정보 꺼내기
        distance, now= heapq.heappop(q)
        
        # distance가 d[now]보다 크면 무시.
        if d[now]<distance:
            continue

        for v in graph[now]:
            cost= d[now]+v[1]
            if cost<d[v[0]]:
                d[v[0]]=cost
                heapq.heappush(q, (cost, v[0])) #힙큐에 추가 (최단거리, 종점)

dijkstra(start)

for v in range(1,V+1):
    if d[v]==INF:
        print('INF')
    else:
        print(d[v])