#view problem: https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3
def solution(arr):
    #arr의 원소개수가 2개미만일 때 => 차라리 그냥 리턴
    if len(arr)<2:
        return arr
    
    #arr의 원소개수가 2개 이상일 때=> 현재원소와 이전원소가 연속적으로 같으면 answer리스트에 추가x
    #만약에 달라지면 추가
    answer = []
    for i in range(0,len(arr)-1):
        if arr[i]!=arr[i+1]: #다음원소와 같지 않다면 sameCount는 0으로 초기화한다. 그리고 answer에 arr[i]번째 원소를 append한다.
            answer.append(arr[i])
    answer.append(arr[len(arr)-1])
    
    return answer
