import sys
input=sys.stdin.readline

n= int(input())
result=0
for i in range(1,n+1):
    sum=i
    part=i

    # 각 자리숫자를 구한다.
    while(part):
        sum+=part%10
        part=part//10
    
    if sum==n:
        result=i
        break
print(result)
        

