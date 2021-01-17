import sys
input=sys.stdin.readline

# Key Error 발생 ...ㅠㅠ
INF=int(1e9)
N,D= map(int, input().split()) #N: 지름길개수, D: 학교위치
nodes=[]
visited={} #방문여부
cost={} # 시작점-도착점 의 최단거리
d={} #최단거리

# 지름길, cost를 초기화 및 갱신
for _ in range(N):
    start, end, distance= map(int, input().split())

    # 시작점이 노드리스트에 없다면
    if start not in nodes:
        nodes.append(start) #노드리스트에 추가
        visited[start]=False #visited에도 추가
        d[start]=INF
    
    # 도착점이 노드리스트에 없다면
    if end not in nodes:
        nodes.append(end)
        visited[end]=False
        d[end]=INF

    # start가 cost에 없다면
    if start not in cost:
        cost[start]={}
    
    # start가 cost에 있다면
    # cost[시작노드] 딕셔너리에 (시작노드, 도착노드) 가 존재하지 않으면
    if not (start ,end) in cost[start]:
        # cost[(시작노드,도착노드)]=(도착노드-시작노드) 거리로 초기화
        cost[start][(start, end)]=end-start
    # cost[(시작노드,도착노드)]의 최솟값을 구한다.
    cost[start][(start,end)]= min(distance, cost[start][(start, end)])

# D가 노드에 존재하지 않는다면
if D not in nodes:
    nodes.append(D)
    visited[D]=False
    d[D]=INF

    for node in nodes:
        if node<D :
            if node not in cost:
                cost[node]={}
            cost[node][(node, D)]=D-node

# 노드들을 재정렬
nodes= sorted(nodes)

# D보다 작은 노드들끼리 연결.
for i in range(len(nodes)-1):
    if nodes[i]<D:
        if nodes[i] not in cost:
            cost[nodes[i]]={}
        
        for j in range(i+1, len(nodes)):
            if (nodes[i], nodes[j]) not in cost[nodes[i]]:
                cost[nodes[i]][(nodes[i], nodes[j])]=nodes[j]-nodes[i]



def dijkstra(now):
    # 현재위치: now
    # 현재 위치가 D라면 최단거리(d[D])를 리턴한다.
    if now==D:
        return d[D]
    #방문체크
    visited[now]=True
    nextNode=D
    shortestPath=INF

    #now와 연결된 노드(방문아직 안한 노드)를 찾는다.
    for vector in cost[now]:
        end= vector[1] #도착점

        # 도착점까지의 최단거리를 갱신한다.
        d[end]=min(d[end], d[now]+cost[now][(now, end)])

        if end<=D:        
            # 도착점은 방문하지 않은 상태여야한다.
            if not visited[end]:
                # now와 연결된 노드중 가중치가 작은 노드를 찾는다.
                if shortestPath>d[end]:
                    shortestPath=d[end]
                    nextNode=end
                elif shortestPath==d[end] and end>nextNode:
                    nextNode=end

    dijkstra(nextNode)

d[0]=0 #시작점은 0으로 초기화
dijkstra(0)

for node in nodes:
    if node<D:
        print('cost[{}]: {}'.format(node, cost[node]))
# print('d: ',sorted(d.items(), key=lambda x: x[0]))
# print(cost)
# print('visited: ', sorted(visited.items(), key=lambda x: x[0]))
print(d[D])