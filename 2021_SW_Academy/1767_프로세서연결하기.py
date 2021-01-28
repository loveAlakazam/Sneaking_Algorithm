import sys
from copy import deepcopy
dy=[-1,1,0,0]
dx=[0,0,-1,1]

def findShortestLength()

def solution(N, maps):
    # core의 위치들을 저장한 리스트
    cores=[]

    # 1을 찾는다.
    for r in range(N):
        for c in range(N):
            if maps[r][c]==1:
                tmp=deepcopoy(maps)
                

T= int(sys.stdin.readline())
for t in range(1,T+1):
    N= int(sys.stdin.readline())
    maps=[ [*map(int, sys.stdin.readline().split())] for _ in range(N)]
    result= solution(N, maps)
    print('#{t} {result}'.format(t=t,result=result))

    