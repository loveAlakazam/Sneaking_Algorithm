import sys
from collections import deque
input=sys.stdin.readline
global M,N,K,Map,visited,dy,dx

q=deque()
M,N,K= map(int, input().split())
Map=[[1]*N for _ in range(M)]
visited=[[0]*N for _ in range(M)]
dy=(-1,1,0,0)
dx=(0,0,-1,1)

def bfs():
    area=0
    while(q):
        y,x=q.popleft()
        if visited[y][x]==0: #아직 방문안함
            visited[y][x]=1#방문표시
            area+=1
            for i in range(4):
                nexty=y+dy[i]
                nextx=x+dx[i]
                if ((nexty>=0 and nexty<M) and (nextx>=0 and nextx<N)):
                    if visited[nexty][nextx]==0 and Map[nexty][nextx]>0: #아직방문 안한상태 and 사각형영역이아니라면
                        q.append((nexty,nextx))

    return area

for _ in range(K):
    x1,y1,x2,y2=map(int,input().split())
    r1,c1= M-y1-1, x1
    r2,c2= M-y2, x2-1
    
    # Map[r][c]=0 : 사각형영역
    for r in range(r2,r1+1):
        for c in range(c1,c2+1):
            Map[r][c]=0
    
cnt=0
areas=[]
for r in range(M):
    for c in range(N):
        if Map[r][c]==1 and visited[r][c]==0:
            q.append((r,c))
            areas.append(bfs())
            cnt+=1
print(cnt)
print(' '.join(str(a) for a in sorted(areas)))
