# 간단한 다익스트라(힙큐x)
# 노드개수가 10000개 이하일때는 가능함.

import sys
input=sys.stdin.readline
INF=int(1e9)

# V: 정점개수(Vertex), E: 간선(Edge)
V,E= map(int, input().split())

# 정점 시작 번호
start= int(input()) 
graph=[ [] for _ in range(V+1)] #그래프 인덱스: 정점
visited=[False]*(V+1)
d=[INF]*(V+1) #d[정점]=정점까지의 최소거리값


def findNextNode():
    shortestPath=INF
    nextNode=0
    # start와 연결된 노드를 찾아서, 최단거리를 갖는 노드를 찾는다.
    for i in range(1,V+1):
        if d[i]<shortestPath and not visited[i]: #방문하지 않은 노드를 찾는다.
            shortestPath=d[i]
            nextNode=i
    return nextNode
                 

# 다익스트라 - 간단한 다익스트라 알고리즘.
def dijkstra(start):
    d[start]=0 #시작점 최단거리:0
    visited[start]=True #방문

    #그래프 start와 연결된 노드의 최단거리를 먼저 초기화
    for g in graph[start]:
        d[g[0]]=g[1]
    
    # 시작 노드를 제외하고 나머지 노드들에 대해서 탐색
    for _ in range(V-1):
        # 최단거리를 갖는 노드를 구한다.
        now= findNextNode()
        visited[now]=True

        for j in graph[now]:
            d[j[0]]=min( d[j[0]], d[now]+j[1])

for _ in range(E):
    s,e,w= map(int,input().split())
    graph[s].append((e,w))

dijkstra(start)

for v in range(1,V+1):
    if d[v]==INF:
        print('INF')
    else:
        print(d[v])