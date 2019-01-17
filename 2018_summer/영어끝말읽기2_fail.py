def solution(n, words):
    answer=[]
    #앞사람이 말한 단어의 맨뒤와 뒷사람이 말한 단어의 맨앞이 서로 같은가?
    for i in range(len(words)-1):
        if words[i][-1] !=words[i+1][0]:
            ans= i+1
            answer=[ans%n+1, ans//n+1]
            return answer
        
    
    history=[]
    for w in words:
        # w가 history에 들어있지 않으면, 계속 원소 추가
        if(w in history)==False:
            history.append(w)
    
    if len(history)==len(words):
        answer= [0,0]
    else:
        for i in range(len(history)):
            if history[i]!=words[i]:
                answer=[i%n+1, i//n+1]
                return answer
        l= len(words)-1
        answer=[l%n+1, l//n+1 ]
    return answer
    
    #90/100
