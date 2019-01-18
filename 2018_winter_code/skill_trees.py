# https://programmers.co.kr/learn/courses/30/lessons/49993?language=python3

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        skill_indexs=[]
        #1. skill_indexs를 채운다.
        for s in skill:
            # s가 가리키는 문자가 tree에 있는가?
            if(s in tree)==True:
                # tree가 가리키는 문자열을 구성하는 문자중 s가 가리키는 문자의 인덱스번호를 추가한다.
                skill_indexs.append(tree.index(s))
            #s가 가리키는 문자가 tree에 존재하지 않는다면, tree가 가리키는 문자열의 길이를 넣는다.
            else:
                skill_indexs.append(len(tree))
        
        #2. skill_indexs가 오름차순으로 되어있는가?
        a=1 #오름차순이 되어있다고 기본설정으로 해놓자.
        for i in range(len(skill_indexs)-1):
            #오름차순으로 되어있지 않은 경우
            if skill_indexs[i]> skill_indexs[i+1]:
                a=0
        if a==1:#오름차순으로 되어있으면 answer 값에 +1한다.
            answer+=1
    return answer
