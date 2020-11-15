def solution(board, moves):
    stack=[]
    answer = 0
    
    # 인형 나열
    maps={}
    lenb=len(board)
    for c in range(lenb):
        maps[c]=[]
        for r in range(lenb):
            if board[r][c]!=0:
                maps[c].append(board[r][c])
        maps[c]=maps[c][::-1]
            
            
    for m in moves:
        # 스택이 비어있지 않다면
        if len(maps[m-1])>0:
            #maps[m]에서 인형을 하나 꺼낸다.
            x=maps[m-1][-1]
            
            # 스택이 비어있지 않다면
            if len(stack)>0:
                s= stack[-1]
                #인형과 stack 맨위에있는 인형이 서로 같다면
                if x==s:
                    answer+=1
                    maps[m-1].pop()
                    stack.pop()
                    
                #다르다면
                else:
                    stack.append(x)
                    maps[m-1].pop()
                
                
            # 스택이 비어있다면
            else:
                stack.append(x)
                maps[m-1].pop()
                
    return 2*answer
