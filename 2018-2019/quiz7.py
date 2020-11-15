# question: https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3
def solution(s):
    if len(s)>=1 and len(s)<=100: #입력 단어s의 길이는 1이상 100이하
        answer=''
        if len(s)%2==0: # 단어의 길이가 짝수이다.
            half=(len(s)-1)/2 # 입력 단어의 마지막 인덱스의 절반 
            answer=answer+s[int(half)]+s[int(half)+1]#half의 타입은 float이므로=> 정수로 바꾼다.
            
        
        else: # len(s)%2!=0 단어의 길이가 홀수이다.
            half=(len(s)-1)/2
            answer=answer+s[int(half)]
        return answer
