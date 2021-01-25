INF=float('inf')
d=[INF]*(n)
visited=[False]*(n)
graph=[ [] for _ in range(n)]
        
#red
for edge in red_edges:
    start, end= edge
    graph[start].append((end, -1)) # endpoint , weight, red:-1
    
#blue
for edge in blue_edges:
    start, end =edge
    graph[start].append((end, 1))# endpoint , weight, blue:1

        
def dijkstra():
    from collections import deque
    q=deque()
    d[0]=0 #시작점을 0으로한다.
    
    q.append((0, 0)) # d[0]=0 , start-point, no-color:-0
    
    # 우선순위큐를 이용
    while q:
        now, color =q.popleft()

        #현재 노드와 연결되어있는 노드를 찾는다.
        for g in graph[now]:
            nextNode= g[0]
            nextColor=g[1]
            
            # color가 없을때는 둘다 가능.    
            # color가 red(-1)일때는 다음컬러가 블루(1)만 가능.
            # color가 blue(1)일때는 다음컬러가 red(-1)만 가능
            if (color<=0 and nextColor==1) or (color>=0 and nextColor==-1):
                cost=d[now]+1
                if cost < d[nextNode]:
                    d[nextNode]=cost
                    q.append((d[nextNode], nextNode, nextColor))
                else:
                    q.append((cost, nextNode, nextColor))

    
dijkstra()
answer=[-1]*n
for i in range(n):
    if d[i]!=INF:
        answer[i]=d[i]
return answer