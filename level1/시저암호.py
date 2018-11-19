# https://programmers.co.kr/learn/courses/30/lessons/12926?language=python3
def solution(s, n):
    ans=[]
    for i in s:
        if i.isalpha() ==True:
            s= ord(i)+n
            if (i.islower()==True) and (s>122):
                s=s-26
            if (i.isupper()==True) and(s>90):
                s=s-26
            ans.append(chr(s))
        else: #공백문자
            ans.append(i)
    return ''.join(ans)
