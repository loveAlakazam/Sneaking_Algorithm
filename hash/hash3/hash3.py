# https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3
def solution(clothes):
    # wear_type: clothes[row][-1] 종류를 나타냄 (중복되는 종류는 제거한다.) 
    wear_type=[]
    for i in range(len(clothes)):
        wear_type.append(clothes[i][-1])
    wear_type=list(set(wear_type)) #중복되는 wear_type원소를 제거.

    #wear_cases: wear_type에 해당하는 의류 개수를 나타냄.
    wear_cases=[] 
    for wt in wear_type:
        wt_sum=0
        for r in range(len(clothes)):
            if wt==clothes[r][-1]:
                wt_sum+=1
        wear_cases.append(wt_sum)
            
    #다르게 위장하는 경우의 수 구하기
    #조합을 이용해서 위장하는 가짓수를 구했으나 테스트1에서 막힘.. => 그이유는 오늘 입은 의상을 제외시켜야한다는점.
    #의상 종류 A,B,C가 각각 a,b,c개있다면, 오늘 입은 옷을 제외한 나머지옷을 서로다르게 입는 경우의수는: (a+1)x(b+1)x(c+1)-1 가지.
    answer=1 #안입는 경우
    for wc in wear_cases:
        answer*=(wc+1)
    answer-=1
    return answer
