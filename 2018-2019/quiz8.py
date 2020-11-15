# https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3
def solution(arr, divisor):
    answer = []
    dividedCnt=0 #'divisor에 나누어떨어지는 arr원소의 개수'를 0으로 초기화
    # arr의 원소 element(자연수)가 divisor에 나누어떨어지는지 확인
    for element in arr:
        if element%divisor ==0: #나누어떨어진다면 answer리스트에 추가
            answer.append(element)
            dividedCnt+=1
    if dividedCnt==0: #나누어 떨어지는 원소가 없다면
        answer.append(-1)
        return answer
            
    # answer리스트를 오름차순으로 정렬
    answer.sort()
    return answer
