# https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3
def solution(a, b):
    if b>=a:
        first=a
        last=b
    else: #b<a
        first=b
        last=a
    answer = 0
    for i in range(first,last+1): #i=first~ last
        answer+=i
    return answer
