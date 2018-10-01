# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3
def solution(citations):
    citations.sort(reverse=True)
    if len(citations)<1:
        return 0    
    for c in range(len(citations)):
        if c >= citations[c]:
            return c
    return c+1
