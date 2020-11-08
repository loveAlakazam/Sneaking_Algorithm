def solution(n, words):
    answer = [0,0]
    round=1
    isUsed=[]
    for idx,word in enumerate(words):
        # isUsed 해시맵에 word가 이미 들어있다면 => 탈락자 발생
        
        if (word in isUsed):
            answer[0]=(idx%n)+1 #탈락자
            answer[1]=round
            return answer
            
        else: #word가 처음사용한 단어라면
            # 현재단어의 맨앞자리와 바로이전에 단어의 맨 뒷자리가 서로다르면=> 탈락자발생
            if len(isUsed)>0 and word[0]!=isUsed[-1][-1]:
                answer[0]=(idx%n)+1 #탈락자
                answer[1]=round
                return answer
            else:
                isUsed.append(word)
                
        
        # 라운드종료
        if idx%n==n-1:
            round+=1
    return answer
