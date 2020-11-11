def solution(strings, n):
    # n번째 문자에 대해서 정렬을 한다.
    # 만약에 n번째 문자가 동일하다면, 나오는 순서를 기준으로 정렬
    
    answer = sorted(strings, key= lambda x: (x[n], x))
    return answer
