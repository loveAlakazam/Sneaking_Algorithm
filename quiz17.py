# https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3
def solution(n):
    answer = list(str(n))
    answer=answer[::-1]
    for i in range(len(answer)):
        answer[i]=int(answer[i])
    return answer
