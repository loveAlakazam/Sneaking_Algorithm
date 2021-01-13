# O(N^2)
import sys
input=sys.stdin.readline
n,k= map(int, input().split()) #n: 인원수, k:방1개당 최대인원수

grade=[ [0,0] for _ in range(6)]

for _ in range(n):
    s, g= map(int, input().split()) #s:성별(여자:0, 남자:1), g:학년
    grade[g-1][s]+=1

room_cnt=0
for g in range(6):
    for s in range(2):
        person_cnt= grade[g][s]
        if person_cnt%k==0:
            room_cnt+=person_cnt//k
        else:
            room_cnt+=person_cnt//k+1

print(room_cnt)