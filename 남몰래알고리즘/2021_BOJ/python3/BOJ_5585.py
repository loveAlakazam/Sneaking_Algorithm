import sys

# 나머지 금액
rest=1000-int(sys.stdin.readline())
coins=[500, 100, 50, 10 , 5, 1]
cnts=[0]*6

for i in range(6):
    if coins[i]>rest:
        continue
    cnts[i]=rest//coins[i]
    rest%=coins[i]

print(sum(cnts))
