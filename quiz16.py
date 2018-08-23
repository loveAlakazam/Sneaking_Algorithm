https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3
import math
def solution(n):
    r=int(math.sqrt(n)) #n의 제곱근=> 실수형태를 정수로 변환
    if r**2==n:#r의 제곱이 n이라면
        return (r+1)**2
    else:
        return -1
