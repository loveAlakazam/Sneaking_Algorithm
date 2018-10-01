# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3
def solution(array, commands):
    answer=[]
    for y in range(len(commands)): #commands의 행개수
        tmp=[]
        #commands의 열개수(3개, i,j,k)
        i=commands[y][0] #i
        j=commands[y][1] #j
        k=commands[y][2] #k
        #자른다.
        tmp=array[i-1:j] # i번째수(index: i-1): j번째수(index: j-1)
        #자른후 오름차순 정렬
        tmp.sort()
        answer.append(tmp[k-1])
    return answer
