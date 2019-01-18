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
'''
skill="CBD" 

skill_trees= [ 'BACDE', 'CBADF', 'AECB, 'BDA' ]

skill_indexs =[ 스킬 C의 인덱스번호, 스킬 B의 인덱스번호, 스킬 D의 인덱스번호 ]
C-> B -> D 순으로 나열되어야한다.

tree라는 문자열은 skill_trees의 원소를 의미한다.

tree= 'BACDE'일때 --> skill_indexs=[ 2, 0, 3 ] => 오름차순 정렬([0, 2, 3])이 아니므로 answer값 카운트 x
tree= 'CBADF'일때 --> skill_indexs=[ 0, 1, 3 ] => 오름차순 정렬([0, 1, 3])과 일치하므로 answer값 카운트 o
tree= 'AECB' 일때 --> skill_indexs=[ 2, 3, 4(존재하지않으면 tree문자열의 길이를 넣는다)] => 오름차순 정렬([2,3,4])와 일치-> answer값 카운트ㅇ
tree= 'BDA'  일때 --> skill_indexs=[ 3, 0, 1] ==> 오름차순 정렬([0,1,3])과 일치하지 않으므로 answer값 카운트 x
'''
