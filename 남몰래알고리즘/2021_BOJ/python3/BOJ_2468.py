import sys
from collections import deque 
input=sys.stdin.readline
q= deque()

global n, Map, visited, answer, dy, dx
dy=(-1,1,0,0)
dx=(0,0,-1,1)

def bfs(y,x, dh):
    q.append((y,x))
    while(q):
        nowY, nowX=q.popleft()
        # 아직 방문 안한상태이고, dh보다 크다면
        if visited[nowY][nowX]==0 and Map[nowY][nowX]>dh:
            visited[nowY][nowX]=1 #방문표시
            for i in range(4):
                nextY=nowY+dy[i]
                nextX= nowX+dx[i]
                if (nextY>=0 and nextY<n) and (nextX>=0 and nextX<n):
                    q.append((nextY,nextX))


answer=1
n=int(input())
Map=[ [int(i) for i in input().strip().split() ] for _ in range(n)]
min_val, max_val= 101, 0

for r in range(n):
    for c in range(n):
        min_val= min(Map[r][c], min_val)
        max_val=max(Map[r][c], max_val)

for i in range(min_val, max_val+1):
    cnt=0
    visited=[ [0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            # 아직 방문안한상태 & Map[r][c]가 잠기지 않은 안전영역
            if visited[r][c]==0 and Map[r][c]>i:
                bfs(r,c,i)
                cnt+=1
    answer=max(answer, cnt)

print(answer)