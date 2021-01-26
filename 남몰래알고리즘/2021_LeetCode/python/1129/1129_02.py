import sys
from collections import deque


# input
q = deque()
n = int(sys.stdin.readline())
red_len, blue_len = map(int,sys.stdin.readline().split())
red_edges = [[*map(int, sys.stdin.readline().split())] for _ in range(red_len)]
blue_edges = [[*map(int, sys.stdin.readline().split())]
              for _ in range(blue_len)]

# real logic
graph=[ [] for _ in range(n)]
for start, end in red_edges:
    graph[start].append((end,0))

for start, end in blue_edges:
    graph[start].append((end,1))

visited=set()
INF=float('inf')
d=[ INF for _ in range(n)]
getColor=lambda color:'red' if color==0 else 'blue'

def bfs():
    d[0]=0
    visited.add((0,0,0)) #start:0, end:0, color:0(red)
    visited.add((0,0,1)) #start:0, end:0, color:1(blue)
    q.append((0, 0,0)) #path: 0, end:0, color: red(0)
    q.append((0, 0,1)) #path: 0, end:0, color:blue(1)

    while q:
        path, now, color=q.popleft() #path:0부터 현재지점까지 총 이동거리, now: 현재 시작점, 현재색상.
        for next in graph[now]:
            start=now
            end= next[0]
            nextColor=next[1]

            if (start,end,nextColor) not in visited:
                if (color==0 and nextColor==1) or (color==1 and nextColor==0):
                    d[end]=min(d[end], path+1) #최소거리.
                    visited.add((start, end, nextColor))
                    q.append((path+1, end,nextColor))
            

bfs()
for i in range(n):
    if d[i]==INF:
        d[i]=-1

for i in range(n):
    print(d[i], end=' ')
print()