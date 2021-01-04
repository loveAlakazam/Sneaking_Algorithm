import sys
input= sys.stdin.readline

# 난쟁이들의 키
h=sorted([ int(input()) for _ in range(9)])

# 난쟁이 키 합
h_sum=sum(h)

# flag
flag=False

for i in range(8):
    for j in range(i+1,9):
        tmp=h_sum-(h[i]+h[j])
        if tmp==100:
            for k in range(9):
                if h[k]==h[i] or h[k]==h[j]:
                    continue
                print(h[k])
            flag=True
    # for문을 벗어난다.
    if flag:
        break