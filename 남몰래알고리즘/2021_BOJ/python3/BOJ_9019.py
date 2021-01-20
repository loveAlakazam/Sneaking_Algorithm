import sys
from collections import deque
q= deque()
global visited

def bfs(a,b):
    q.append((a,''))
    while q:
        num, r= q.popleft()
        
        if num==b:
            return r
        
        if not visited[num]:
            visited[num]=True

            #D
            curr=(num*2)%10000
            if  not visited[curr]:
                q.append((curr, r+'D'))

            #S
            if num==0:
                curr=9999
            else:
                curr=num-1
            if  not visited[curr]:
                q.append((curr , r+'S'))
            
            #L
            curr=(num%1000)*10+(num//1000)
            if not visited[curr]:
                q.append((curr, r+'L'))

            #R
            curr=(num//10)+(num%10)*1000
            if not visited[curr] :
                q.append((curr, r+'R'))


T=int(sys.stdin.readline())
for _ in range(T):
    A,B= map(int, sys.stdin.readline().split())
    visited=[False]*10000
    print(bfs(A,B))
    q.clear()
    