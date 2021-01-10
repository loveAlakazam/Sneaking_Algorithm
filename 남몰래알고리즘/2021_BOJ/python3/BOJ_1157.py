import sys
input=sys.stdin.readline

s=input().strip().lower()
alpha={ chr(97+i):0 for i in range(26)}

for w in list(s):
    alpha[w]+=1

# 내림차순 정렬
sorted_list=sorted(alpha.items(), key=lambda x: -x[1])
max_cnt=sorted_list[0][1]
if( max_cnt==sorted_list[1][1]):
    print('?')
else:
    print(sorted_list[0][0].upper())

