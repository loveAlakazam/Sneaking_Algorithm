import sys
input = sys.stdin.readline

# 막대기 개수
n= int(input())

# n개의 막대기들 
polls= [ int(input()) for x in range(n)]
now= n-1

answer=[]
answer.append(polls[-1]) #맨오른쪽 막대기를 먼저 넣는다.
while now>0:
    # polls[now-1]이 answer에 있는 가장오른쪽막대기보다 큰가?
    if polls[now-1]> answer[-1]:
        answer.append(polls[now-1])
    now-=1

print(len(answer))