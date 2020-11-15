def solution(N):
    # 타일길이 초기화
    lengths=(N+1)*[1]
    if N>=2:
        for i in range(2,N+1):
            lengths[i]=lengths[i-1]+lengths[i-2]
    return (lengths[N]*2)+(lengths[N-1]*2)
