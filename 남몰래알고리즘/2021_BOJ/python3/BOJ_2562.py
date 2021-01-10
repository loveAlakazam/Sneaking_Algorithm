import sys
input=sys.stdin.readline

ndict={idx: int(input())  for idx in range(1,10)}
ndict= sorted(ndict.items(), key=lambda x: x[1]) # 복잡도: O(NlogN)

print(ndict[-1][1])
print(ndict[-1][0])