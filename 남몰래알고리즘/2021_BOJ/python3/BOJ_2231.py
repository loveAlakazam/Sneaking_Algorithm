# 2300 ms 
import sys
input=sys.stdin.readline
n=int(input())
nums={num:[] for num in range(1,n+1)}

for num in range(1,n+1):
    s=num+sum(int(i) for i in list(str(num)))

    # 숫자 num은 숫자s의 생성자이다.
    if s <= n: 
        nums[s].append(num)
    else:
        pass

if len(nums[n])>0:
    print(nums[n][0])
else:
    print(0)