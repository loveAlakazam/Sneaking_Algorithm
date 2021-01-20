import sys
from collections import deque
q= deque()
def bfs(a,b):
    q.append((a,''))
    visited=[False]*10000
    next=[0]*4
    while q:
        num, r= q.popleft()
        
        if num==b:
            return r
        
        if not visited[num]:
            visited[num]=True
            #D: next[0]
            next[0]=(num*2)%10000

            #S: next[1]
            if num==0:
                next[1]=9999
            else:
                next[1]=num-1
            #L
            next[2]=(num%1000)*10+(num//1000)

            #R
            next[3]=(num//10)+(num%10)*1000

            if  next[0]<10000 and not visited[next[0]]:
                q.append((next[0], r+'D'))
            if  next[1]<10000 and not visited[next[1]]:
                q.append((next[1], r+'S'))
            if next[2]<10000 and not visited[next[2]]:
                q.append((next[2], r+'L'))
            if next[3]<10000 and not visited[next[3]] :
                q.append((next[3], r+'R'))

T=int(sys.stdin.readline())
for _ in range(T):
    A,B= map(int, sys.stdin.readline().split())
    print(bfs(A,B))
    q.clear() #큐를 비운다.