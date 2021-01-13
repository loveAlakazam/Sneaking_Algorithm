# 메모리 초과로 실패.
import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

global col, row, K, visited, dY, dX

col, row= map(int, input().split())
K= int(input())
visited=[[False]*col for _ in range(row)]

#위, 오른쪽, 아래, 왼쪽
dY=[-1,0,1,0]
dX=[0,1,0,-1]

def isAvailable(y,x):
    if (y>=0 and y<row) and (x>=0 and x<col):
        return True
    return False

def goToK(nowY, nowX, nowVal, direction):
    if K> col*row:
        return 0

    ## 현재위치가 K인가?
    if nowVal==K:
        return ' '.join(map(str,(nowX+1, row-nowY) ))
    
    #아직 방문하지 않은 상태라면
    if not visited[nowY][nowX]:
        visited[nowY][nowX]=True

        direction%=4
        dy=nowY+dY[direction]
        dx=nowX+dX[direction]
        if isAvailable(dy,dx):
            if not visited[dy][dx]:
                return goToK(dy, dx, nowVal+1, direction)
    visited[nowY][nowX]=False
    return goToK(nowY, nowX, nowVal, direction+1)
    

# 리턴답: (col+1 ,row-nowY)
result=goToK(row-1,0,1, 0)
print(result)