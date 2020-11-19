def solution(progresses, speeds):
    durations=[(100-progress)//speed if (100-progress)%speed==0  else (100-progress)//speed+1 for progress, speed in zip(progresses, speeds)][::-1]
    
    stack=[]
    answer=[]
    while len(durations)>0:
        target=durations.pop()
        stack.append(target)
        while durations and target>=durations[-1]:
            stack.append(durations[-1])
            durations.pop()
        
        answer.append(len(stack))
        stack=[]
    
    return answer
