# https://programmers.co.kr/learn/courses/30/lessons/12981?language=python3
def solution(n, words):
    answer=[]
    '''
    1단계
    앞사람의 영단어의 맨뒤 알파벳과
    그 다음 사람의 영단어의 맨앞 알파벳이 서로 같은가?
    yes라면 2단계로 넘어간다.
    no라면 틀린단어를 말한사람(뒷사람)의 인덱스(x)를 구한다.
    answer[0]: 몇번째사람이 틀렸는가?: (x% n)+1
    answer[1]: 몇번째 경기에서 틀렸는가?: (x//n)+1
    '''     
    for y in range(len(words)-1):
        #앞 단어의 맨 뒤문자와 뒷사람의 맨앞문자가 서로 다르다면 
        if(words[y][-1]!= words[y+1][0]):            
            no_indx = y+1 #틀린단어의 인덱스는 y+1이므로..
            answer.append((no_indx%n) +1) #몇번째 사람이 틀렸는가?
            answer.append((no_indx//n) +1) #몇번째 경기에서 틀렸는가?
            return answer
    '''
    2단계
    한글자인 단어를 말했는가? 중복된 단어가 존재하는가?
    yes라면 중복된 단어를 말한 인덱스번호를 구한다.
    no라면 문제 없이 규칙을 잘 지키므로 [0,0]을 리턴한다.
    '''
    compare =list(set(words)) #중복된 단어를 제거.
    no_indx=0
    if len(compare)==len(words): #규칙을 잘지킨 경우..
        answer=[0,0]
    
    else:#이전에 말했던 단어를 말한 경우..
        for c in compare:
            i= words.index(c)
            words[i]=0
        for w in words:
            if w!=0:
                no_indx=words.index(w)
                answer.append( (no_indx%n)+1) #몇번째 사람이 단어를 중복해서 말했는가?
                answer.append( (no_indx//n)+1) #몇번째 경기에서 단어를 중복해서 말했는가?
                return answer

    return answer
