# 문제 : https://programmers.co.kr/learn/courses/30/lessons/12899
# 참고 : https://chickenpaella.tistory.com/59
def solution(n):#n은 10진수
    answer=''
    arr=[4,1,2]
    while(n>0):
        rest=n%3
        n=n//3
        if(rest==0):
            n=n-1
        answer=str(arr[rest])+answer
    return answer
