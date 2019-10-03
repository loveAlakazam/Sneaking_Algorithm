import collections
def solution(progresses, speeds):
    complete_days= collections.deque([])
    for progress, speed in zip(progresses, speeds):
        days=(100-progress)//speed
        if (100-progress)%speed==0:
            complete_days.append(days)
        else:
            complete_days.append(days+1)
        
    # 뒤에 있는 기능은 앞에있는 기능이 배포될때 함께 배포된다.
    tmp=complete_days[0]
    cnt=0
    answer=[]
    while(len(complete_days)>0):
        if complete_days[0]>tmp:
            answer.append(cnt)
            cnt=1
            tmp=complete_days.popleft()
            
        else: #complete_days<=tmp
            cnt+=1
            complete_days.popleft()
    answer.append(cnt)
    return answer
