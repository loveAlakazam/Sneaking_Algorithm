# https://programmers.co.kr/learn/courses/30/lessons/12933?language=python3
def divider(n,p, nums):    
    if p==0:
        nums.append(n)
        return nums
    
    else: #p!=0
        nums.append(int(n/powerTen(p)))
        n=int(n%powerTen(p))
        p=p-1
        return divider(n,p,nums)
    
def powerTen(p):
    if p==0: #10^0= 1
        return 1
    else: #p!=0 , 10*(10^(p-1))
        return 10*powerTen(p-1)
    
def solution(n):
    if n>=1 and n<=8000000000: #n은 1이상 8000000000 이하인 자연수
        #p =0으로 초기화
        p=0
        
        # n< 10^p를 성립할 때 while문을 벗어난다.
        while n>=powerTen(p):
            p=p+1
        #largestP: n보다 작으면서 가장 큰 지수
        #예를 들면 118372의 경우 p=6일때 while문을 벗어나고.. 10^5이 가장큰 10의 제곱수이므로..largestP=5
        largestP=p-1
        
        nums=[] #리스트 초기화
        
        answer=divider(n,largestP,nums)
        answer.sort(reverse=True) #내림차순 정렬

        lp=largestP
        result=0
        while lp>-1:
            result+= answer[len(answer)-1-lp]*powerTen(lp)
            lp-=1

        return result  
