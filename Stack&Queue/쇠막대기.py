def solution(arrangement):
    answer = 0
    polls=[]
    arrangement=arrangement.replace('()', '.')
    for idx, now in enumerate(arrangement):
        if now=='(':#막대기1개가 생겼다.
            polls.append(1)
        elif now==')':
            #한개를 더한다.
            answer=answer+polls.pop()
        else:#now=='.'
            #.을 만나자마자 현재 막대개수를 더한다.
            answer= answer+len(polls)
    return answer
