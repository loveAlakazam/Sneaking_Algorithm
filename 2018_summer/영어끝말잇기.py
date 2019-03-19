# https://programmers.co.kr/learn/courses/30/lessons/12981?language=python3
def solution(n, words):
    answer = []
    find_wrong =0 # 중간에 규칙위반이 생겼음을 알리는 변수/ 1이면 생긴거고, 0이면 생기지 않음을 의미.
    i=1 # words의 맨 처음 단어의 시작인덱스(1부터 시작)
    past=[] #이전단어
    for w in words:
        if i==1:
            past.append(w) #맨앞단어 past에 추가
        elif i>1:  
            #현재 단어(w)가 past에 이미 있는 단어인가?
            if w in past:
                if i%n==0: #i가 n에 나누어떨어질때 ex) i=9이고 n=3일때 3번째 판에서 3번째사람이 틀렸는데 i%n==0이면 0번째사람, i//n+1=4 번째 판이므로..예상과 다른 결과가 나올수있다.
                    answer=[n,i//n]
                else:
                    answer=[i%n, i//n+1] #0번째 인덱스: 몇번째사람이 틀렸는가? / 1번째인덱스: 몇번째 판에서 틀렸는가?
                find_wrong=1
                break
        
            #현재 단어(w)의 맨 앞 글자가 past[i-1]의 마지막글자와 다른가?
            if w[:1] != past[i-1][-1:]:
                if  i%n==0:
                    answer=[n,i//n]
                else: 
                    answer=[i%n, i//n+1]
                find_wrong=1
                break
        i+=1
        past.append(w)

    if find_wrong==0:
        answer=[0,0]
    return answer
