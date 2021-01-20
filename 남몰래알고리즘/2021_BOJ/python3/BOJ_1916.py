import sys
import heapq
INF=float('inf')
N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
cities=[[] for n in range(N+1)] # 0~N
visited=[False]*(N+1)
p=[INF]*(N+1)
q=[]

def dijkstra(start):
    p[start]=0 # start에서의 최소비용은 0
    heapq.heappush(q, (0, start)) #우선순위큐에 시작점을 넣는다.
    while q:
        pay, nowCity = heapq.heappop(q)

        # 방문표시
        visited[nowCity]=True

        # 현재도시와 연결된 도시를 구한다.
        for city in cities[nowCity]:
            nextCity=city[0]
            pay=city[1]

            # 다른도시가 방문되어있는 상태인지 확인.
            if not visited[nextCity]:
                cost= p[nowCity]+pay #현재도시에서 nextCity 까지 가는데 비용
                if cost< p[nextCity]:
                    p[nextCity]=cost
                    heapq.heappush(q, (cost, nextCity))

for _ in range(M):
    s,e,w= map(int, sys.stdin.readline().split())
    cities[s].append((e,w))

start, end= map(int, sys.stdin.readline().split())
dijkstra(start)
print(p[end])


