# https://programmers.co.kr/learn/courses/30/lessons/12922?language=python3
def solution(n):
    answer=""
    for i in range(n): #0~n-1까지
        if i%2==0:
            answer=answer+'수'
        else:
            answer=answer+'박'
    return answer 
