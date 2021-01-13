import sys
from collections import deque
input=sys.stdin.readline
q=deque()

global n, m, connect, visited, answer, dx,dy

def bfs():
    cnt=0
    while(q):
        now=q.popleft()
        idx=now-1
        if visited[idx]==0:
            visited[idx]=1
            cnt+=1
            
            #now번 컴퓨터와 연결된 컴퓨터를 찾는다.
            for i in range(1,n+1):
                if connect[idx][i-1]==1 and visited[i-1]==0:
                    q.append(i)

    return cnt

n= int(input())
connect=[[0]*n for _ in range(n)]
visited=[0]*n
m= int(input())

for _ in range(m):
    com1, com2= map(int, input().split())
    connect[com1-1][com2-1]=connect[com2-1][com1-1]=1

q.append(1)
answer=bfs()
print(answer-1) #1번 컴퓨터를 뺀다.

