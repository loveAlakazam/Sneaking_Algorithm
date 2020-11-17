import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 내림차순 정렬로 한다.
cards= [int(x) for x in input().split()]

# bruteforce
answer=0
total=0
for i in range(N):
    for j in range( i+1, N):
        for k in range(j+1, N):
            total= cards[i]+cards[j]+cards[k]
            if total<= M:
                answer= max(answer, total)
    
print(answer)