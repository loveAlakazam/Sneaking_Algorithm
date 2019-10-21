def solution(arrangement):
    len_arrangement=len(arrangement)
    if len_arrangement==0:
        return 0
    open_idx_stack=[] # '('의 인덱스번호를 모으는 스택이다.
    layser_points=[] #레이저의 위치이다.
    polls=[]#막대기 : (막대기 시작점, 막대기 끝점)
    
    # 막대의 시작점/끝점, 레이저포인트를 구한다.
    for idx in range(len_arrangement):
        # 만일 idx에 해당하는 글자가 ( 라면 open_idx_stack에 넣는다.
        if arrangement[idx]=='(':
            open_idx_stack.append(idx)
        else:#idx에 해당하는 글자가 )라면 open_idx_stack에 있는 넘버를 pop한다.
            close_idx=idx
            open_idx=open_idx_stack.pop()
            
            #close_idx-open_idx=1이라면 open_idx를 레이저 포인트로 한다.
            if close_idx-open_idx==1:
                layser_points.append(open_idx)
                
            #close_idx-open_idx>1이라면 막대의 길이이다.
            else:
                polls.append([open_idx, close_idx])

    tmp=[1]*len_arrangement
    for p in layser_points: #layser_point부분은 0으로 한다
        tmp[p]=0
    
    answer=0
    for start, end in polls:
        answer+= tmp[start:end+1].count(0)+1 #각 막대기의 레이저점개수+1=> 만들어진 막대기개수
    return answer
