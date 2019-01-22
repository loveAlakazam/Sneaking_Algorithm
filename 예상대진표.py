# https://programmers.co.kr/learn/courses/30/lessons/12985?language=python3
def solution(n,a,b):
    game_round =0
    while abs(a-b)>=1:
        game_round+=1
        if a%2 ==0:
            a=a//2
        else:#홀수
            a=a//2+1

        if b%2==0:
            b=b//2
        else:
            b=b//2+1
    return game_round
