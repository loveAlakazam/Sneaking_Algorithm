import sys
input=sys.stdin.readline

n=int(input())

p=[ [*map(int,input().strip().split())] for _ in range(n)]
rank=[1]*n

for i in range(n):
    for j in range(n):
        if i!=j:
            if p[i][0]<p[j][0] and p[i][1]<p[j][1]:
                rank[i]+=1

print(' '.join(str(r) for r in rank))