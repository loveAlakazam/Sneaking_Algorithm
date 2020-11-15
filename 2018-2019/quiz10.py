# https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3
def powerTen(p):
    if p==0:# 10^0=1
        return 1
    else: #10^p= 10* 10^(p-1) (p=1,2,3,...)
        return 10*powerTen(p-1)

def partNum(n,p,nums):
    if p==0:
        nums.append(n)
        return nums
    
    else: #p!=0
        nums.append(int(n/powerTen(p))) #n ÷(10^p)의 몫
        n=int(n%powerTen(p))
        p=p-1
        return partNum(n,p,nums)
    
def solution(n):
    if n>=1 and n<=100000000: #n은 100,000,000이하의 자연수
        p=0
        while n>=powerTen(p):
            p=p+1
        # n<10^p일 때 while문을 빠져나간다.
        largestP=p-1
        
        nums=[]
        #nums는 n의 각 자리 숫자를 나타내는 리스트이다. 원소는 int로 되어있음.
        nums=partNum(n,largestP,nums)
        print(nums)
        answer = 0
        for i in nums:
            answer+=i

        return answer
