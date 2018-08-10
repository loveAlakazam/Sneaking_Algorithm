# https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3
def solution(s):
    #문자열 s의 길이는 50이하의 자연수인가?
    if len(s)<=50:
        yNum,pNum=0,0
        #문자열 s는 알파벳으로만 이루어져있는가?
        if s.isalpha()==True:
            #대문자를 소문자로 변환시켜준다.
            s=s.lower()
            for i in s:
                if i=='y':
                    yNum+=1
                elif i=='p':
                    pNum+=1
        #p와 y의 개수가 서로 같은가?
        if pNum==yNum:
            return True
        else:
            return False
