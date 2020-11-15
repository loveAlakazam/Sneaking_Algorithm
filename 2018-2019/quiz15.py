# https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3
def solution(s):
    upper=[]
    lower=[]
    l=list(s)
    l.sort() #오름차순 정렬
    for i in l:
        if i.isupper()==True: #대문자라면
            upper.append(i)
        elif i.islower()==True:#소문자
            lower.append(i)
    #내림차순
    lower.sort(reverse=True)
    upper.sort(reverse=True)
    answer=lower+upper #소문자>대문자
    answer=''.join(answer) #리스트=>문자열
    return answer


''' 
# best answer
def solution(s):
    return ''.join(sorted(s, reverse=True))
'''
