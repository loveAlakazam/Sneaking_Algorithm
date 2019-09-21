# https://programmers.co.kr/learn/courses/30/lessons/42587

import collections
def updata_max_val(priorities):
    max_val=0
    for  _ , val in priorities:
        if(max_val<val):
            max_val=val
    return max_val
        
def solution(priorities, location):
    #제일 작은/ 제일 큰 우선순위를 먼저 찾는다.
    min_prior= min(priorities)
    max_prior= max(priorities)
    print('우선순위 가장 높은 숫자: ',max_prior)

    # 리스트에서 큐로 변경한다.
    priorities= list(enumerate(priorities))
    priorities= collections.deque(priorities)
    
    # 프린트 큐
    print_order_queue=[]

    while(len(priorities)>0):
        target=priorities.popleft()
        idx,data=map(int, target) #맨앞에있는걸 뺀다.
        
        if (max_prior==min_prior) and not(idx in print_order_queue):
            print_order_queue.append(idx)
            
        if data>min_prior and data==max_prior:
            print_order_queue.append(idx)
            max_prior=updata_max_val(priorities) #max_prior갱신
            
        elif (max_prior>min_prior) and (data<max_prior) :
            priorities.append(target)
    answer=print_order_queue.index(location)+1
    return answer
