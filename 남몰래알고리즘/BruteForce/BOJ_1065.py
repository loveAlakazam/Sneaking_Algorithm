import sys
input= sys.stdin.readline

# 한수인지 확인해주는 함수 
def isHanSu(n):
    tmp=[int(x) for x in str(n)]
    diff=tmp[1]-tmp[0]
    for i in range(1,len(tmp)):
        if not (tmp[i]-tmp[i-1]== diff):
            return False
    return True
            

def countHanSu(n):
    # n의 길이가 2이하이면 모두 한수. (즉, 1~99는 모두 한수이다.)
    if len(str(n))<=2:
        return n
    
    result=99
    for i in range(100,n+1):
        if isHanSu(i):
            result+=1
    return result


N=int(input())
print(countHanSu(N))
