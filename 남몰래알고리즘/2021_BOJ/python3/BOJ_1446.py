import sys
import heapq

input=sys.stdin.readline

N,D= map(int, input().split()) #N: 지름길개수, D: 학교위치
nodes=[]
visited={}
d={}

# 지름길, d를 초기화 및 갱신
for _ in range(N):
    start, end, distance= map(int, input().split())

    # 시작점과 도착점중 하나가 노드리스트에 존재하지 않으면 노드리스트에 추가.
    if start not in nodes:
        nodes.append(start)
        visited[start]=False
        d[start]={}

    elif end not in nodes:
        nodes.append(end)
        visited[end]=False
    
    
    # d[시작노드] 딕셔너리에 (시작노드, 도착노드) 가 존재하지 않으면
    # d[(시작노드,도착노드)]=(도착노드-시작노드) 거리로 초기화
    # d[(시작노드,도착노드)]의 최솟값을 구한다.
    if not (start ,end) in d[start]:
        d[start][(start, end)]=end-start
    d[start][(start,end)]= min(distance, d[start][(start, end)])

nodes= sorted(nodes)

# 연결되지 않은 나머지 노드들간의 사이거리로 연결(바로 연결된 노드를 의미한다.)
for i in range(1,len(nodes)):
    if not (nodes[i], nodes[i+1]) in d[nodes[i]]:
        d[nodes[i]][(nodes[i], nodes[i+1])]=nodes[i+1]-nodes[i]
    else:
        continue

def dijkstra(now):
    # 현재위치: now
    # 현재 위치가 
    return 0

dijkstra(0)