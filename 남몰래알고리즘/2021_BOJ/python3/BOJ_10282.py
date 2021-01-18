import sys
import heapq
INF=float('inf')
t= int(sys.stdin.readline())

global n,d,c,times, visited, graph

def dijkstra(start):
    times[start]=0 #바이러스 발생시작
    q=[]
    heapq.heappush(q, (0, start))
    while q:
        # curr: 현재시각
        # com: 현재 컴퓨터
        curr, com= heapq.heappop(q)

        # 현재컴퓨터와 연결된 컴퓨터를 구한다.
        for i in graph[com]:
            nextCom= i[0]
            cost= curr+i[1] 
            if cost<times[nextCom]:
                times[nextCom]=cost
                heapq.heappush(q, (cost, nextCom))


for _ in range(t):
    n, d, c=map(int, sys.stdin.readline().split())
    times=[INF]*(n+1)
    graph=[ [] for _ in range(n+1)]
    for _ in range(d):
        a,b,s=map(int, sys.stdin.readline().split())
        graph[b].append((a,s))
    dijkstra(c)

    virused_cnt=0 #감염된 컴퓨터 개수
    virused_times=0 #모든컴퓨터가 감염되기까지 걸린시간
    for i in range(1,n+1):
        if times[i]==INF:
            continue
        virused_cnt+=1
        virused_times=max(virused_times, times[i])
    
    print('{vc} {vt}'.format(vc=virused_cnt, vt=virused_times))
