# https://programmers.co.kr/learn/courses/30/lessons/12928?language=python3
def solution(n):
    nums=[]
    #1~n사이의 자연수중 나누어떨어지는 수는 nums리스트에 추가
    for i in range(1,n+1):#1~n
        if n%i==0:
            nums.append(i)
    
    answer = 0
    for i in nums:
        answer+=i
    return answer
