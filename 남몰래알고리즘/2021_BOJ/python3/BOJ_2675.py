import sys
input= sys.stdin.readline

def solution(R,S):
    P=''
    for s in list(S):
        P=P+s*R
    return P


T=int(input())
for _ in range(T):
    tmp=input().strip().split()
    R=int(tmp[0])
    S=tmp[1] #길이: 1~20
    print(solution(R,S))