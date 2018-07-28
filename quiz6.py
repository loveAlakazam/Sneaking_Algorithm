#view quiz: https://programmers.co.kr/learn/courses/30/lessons/12918?language=python3
def solution(s):
    pureNum=[0,1,2,3,4,5,6,7,8,9]
    pureNumCount =0 #순수 숫자 개수
    for i in range (len(s)):
        try:#s[i]가 숫자인 경우
            if int(s[i])==pureNum[int(s[i])]:
                pureNumCount+=1
                continue
        except:
            return False
                
           
    if len(s)==4 or len(s)==6:
        if pureNumCount==len(s): #입력한 s의 길이 = 순수숫자카운트값 => s가 모두 순수숫자인 경우
            return True
        else:
            return False
    else:
        return False
