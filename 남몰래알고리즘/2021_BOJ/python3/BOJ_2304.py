import sys
input=sys.stdin.readline

# max_idx: 막대의 위치값이 최댓값(맨오른쪽에 위치)인 막대의 인덱스번호
# min_idx: 막대의 위치값이 최솟값(맨왼쪽에 위치)인 막대의 인덱스번호
# max_height_idx: 막대높이값이 최대값인 막대의 인덱스번호

global min_idx, max_idx, max_height_idx, wareHouse
min_idx, max_idx, max_height_idx= 1000, 0,0
wareHouse=[0]*1001

# 왼쪽끝에서 가장긴 막대에 도달할 때까지.
def left_sum():
    left_sum=0
    max_area=0
    for now in range(min_idx, max_height_idx):
        max_area=max(wareHouse[now],max_area)
        left_sum+=max_area
    return left_sum

# 오른쪽끝에서 가장긴 막대에 도달할때 까지.
def right_sum():
    right_sum=0
    max_area=0
    for now in range(max_idx,max_height_idx,-1):
        max_area=max(wareHouse[now], max_area)
        right_sum+=max_area
    return right_sum

n=int(input())
for _ in range(n):
    L, H= map(int, input().split())
    wareHouse[L]=H
    min_idx=min(min_idx, L)
    max_idx=max(max_idx, L)
    if(H>wareHouse[max_height_idx]):
        max_height_idx=L

result=wareHouse[max_height_idx]+left_sum()+right_sum()
print(result)