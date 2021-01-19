import sys
from collections import deque

q=deque()
n=int(sys.stdin.readline())
rooms=[]
INF=float('inf')
changeCnt=[[INF]*n for _ in range(n)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]

for _ in range(n):
    rooms.append(list(sys.stdin.readline().strip()))

def dijkstra():
    changeCnt[0][0]=0
    q.append((0,0))
    while q:
        y,x=q.popleft()

        for i in range(4):
            nextX=x+dx[i]
            nextY=y+dy[i]
            if (nextY>=0 and nextY<n) and (nextX>=0 and nextX<n):
                # 벽인경우
                if rooms[nextY][nextX]=='0':
                    if changeCnt[y][x]+1< changeCnt[nextY][nextX]:
                        changeCnt[nextY][nextX]=changeCnt[y][x]+1
                        q.append((nextY, nextX))

                else:
                    if changeCnt[y][x]< changeCnt[nextY][nextX]:
                        changeCnt[nextY][nextX]=changeCnt[y][x]
                        q.append((nextY,nextX))


dijkstra()
print(changeCnt[n-1][n-1])