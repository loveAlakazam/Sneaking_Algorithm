# https://programmers.co.kr/learn/courses/30/lessons/12980?language=python3
def solution(n):
    # n 이 홀수 인지 짝수인지를 판별
    # n 이 0이 될때까지 계속 카운트한다
    ans =0
    while(n !=0):
        if n%2 ==0: #n이 짝수라면
            n= n/2
        else: #n이 홀수라면
            n= n-1
            ans +=1
    return ans
