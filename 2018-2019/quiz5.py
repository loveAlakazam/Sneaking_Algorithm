#view problem: https://programmers.co.kr/learn/courses/30/lessons/12925?language=python3
#reference: http://thrillfighter.tistory.com/275 =>type변환
def solution(s):
    #문자열 s를 리스트로 나타낸다.list(문자열)
    s=list(s)
    #리스트를 뒤집는다.
    s.reverse()
    #리스트를 문자열로 바꾼다.
    s=''.join(s)
    num=0
    for i in range(0,len(s)): 
        if i==len(s)-1 and s[i]=="+":
            num= num*1
        elif i==len(s)-1 and s[i]=="-":
            num= num*(-1)
        else:#문자열을 int형으로 바꾸기
            num=num+(int(s[i])*(10**i))

    return num
