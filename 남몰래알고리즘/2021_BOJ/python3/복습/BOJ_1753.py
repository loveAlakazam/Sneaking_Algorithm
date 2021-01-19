import sys
import heapq

INF = float('inf')
V, E = map(int, sys.stdin.readline().split())
S = int(sys.stdin.readline())

maps = [[] for _ in range(V+1)]
d = [INF]*(V+1)  # 최단거리
visited = [False]*(V+1)

for _ in range(E):
    start, end, w = map(int, sys.stdin.readline().split())
    maps[start].append((end, w))


def dijkstra(start):
    q = []
    d[start] = 0
    heapq.heappush(q, (0, start))  # 시작점을 넣는다. 시작점의 최단거리는 0
    while q:
        _,now = heapq.heappop(q)
        
        visited[now] = True

        # now와 연결된 노드를 찾는다.
        for node in maps[now]:
            end = node[0]
            weight = node[1]

            if not visited[end]:
                cost = d[now]+weight
                if cost < d[end]:
                    d[end] = cost
                    heapq.heappush(q, (cost,end))


dijkstra(S)


for i in range(1, V+1):
    if d[i] == INF:
        print('INF')
    else:
        print(d[i])