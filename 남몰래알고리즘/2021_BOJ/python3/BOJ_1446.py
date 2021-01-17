import sys
input=sys.stdin.readline

N,D= map(int, input().split())
vectors=[]

for _ in range(N):
    start, end, distance= map(int, input().split())
    if end>D:
        continue
    if distance>=end-start:
        continue
    vectors.append([start, end, distance])

d=[i for i in range(D+1)]
for i in range(D+1):
    if i !=0:
        # 최단거리를 갱신한다.
        d[i]=min(d[i], d[i-1]+1)

    # i 와 연결된 그래프를 탐색하여 최단거리를 구한다.
    for v in vectors:
        if v[0]==i: #출발점이 i일때
            d[v[1]]=min(d[v[1]], d[v[0]]+v[2])
        
print(d[D])