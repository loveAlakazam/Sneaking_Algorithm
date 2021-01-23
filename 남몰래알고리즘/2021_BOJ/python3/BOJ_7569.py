import sys
from collections import deque
M,N,H= map(int, sys.stdin.readline().split())
q=deque()
# 앞, 뒤, 상, 하, 좌, 우
dz=(-1,1,0,0,0,0)
dy=(0,0,-1,1,0,0)
dx=(0,0,0,0,-1,1)

tomatoes=[ [] for _ in range(H)]

for h in range(H):
    for _ in range(N):
        tomatoes[h].append([*map(int, sys.stdin.readline().split())])


def isAllRipen():
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if tomatoes[h][r][c]==0:
                    return False
    return True

def BFS():
    while q:
        z,y,x,t= q.popleft()
        
        for i in range(6):
            nextz=z+dz[i]
            nexty=y+dy[i]
            nextx=x+dx[i]

            if (nextz>=0 and nextz<H) and (nexty>=0 and nexty<N) and (nextx>=0 and nextx<M):
                if tomatoes[nextz][nexty][nextx]==0:
                    tomatoes[nextz][nexty][nextx]=1
                    q.append((nextz,nexty,nextx,t+1))
    return t


# 토마토 전체가 익는데 걸린 시간
answer = 0

# 토마토가 다 익었는지 확인한다. 
if isAllRipen():# 다익음
    answer=0
else:
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if tomatoes[h][r][c]==1:#초기에 익은 토마토를 큐에 넣는다.
                    q.append((h,r,c,0)) # 4번째인자는 익는데 걸린 시간이다.

    answer=BFS() #익는데 걸린 시간을 구한다.
    
    # 모두 다 익었는지 확인
    if not isAllRipen(): #다 익지 않으면
        answer=-1

print(answer)