import sys
from collections import deque
q= deque()

global visited, l
dy=(-2,-2, -1,-1 , 1,1, 2,2)
dx=(-1,1,  -2,2,  -2,2, -1,1)

def bfs(starty, startx, endy, endx):
    q.append((starty, startx, 0))
    while q:
        nowy, nowx, cnt=q.popleft()
        if (nowy==endy) and (nowx==endx):
            return cnt

        visited[nowy][nowx]=True
        for i in range(8):
            nexty=nowy+dy[i]
            nextx=nowx+dx[i]
            if (nexty>=0 and nexty<l) and (nextx>=0 and nextx<l):
                if not visited[nexty][nextx]:
                    visited[nexty][nextx]=True
                    q.append((nexty, nextx, cnt+1))

T= int(sys.stdin.readline())
for _ in range(T):
    l= int(sys.stdin.readline())
    visited=[ [False]*l for _ in range(l)]
    
    starty, startx= map(int, sys.stdin.readline().split())
    endy, endx=map(int, sys.stdin.readline().split())
    result=bfs(starty, startx, endy, endx)
    q.clear()
    print(result)
    