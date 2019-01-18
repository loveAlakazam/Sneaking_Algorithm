# https://programmers.co.kr/learn/courses/30/lessons/12977?language=python3
from itertools import combinations
def solution(nums):
    cases= list(combinations(nums, 3))
    three_sum_cases= []
    
    #cases의 원소는 3개의원소를 갖는 튜플로 구성되어있는데
    #three_sum_cases는 튜플안에있는 3개 원소를 합한 값을 의미한다.
    for i in range(len(cases)):
        three_sum_cases.append(sum(cases[i]))
    
    answer=0
    cnt=0
    #three_sum_cases 가 소수인지를 판별
    for i in three_sum_cases:
        if i%2!=0: #홀수인가?
            cnt=0
            for j in range(1,i+1):#j=1~i까지
                if i%j==0:
                    cnt+=1
            if cnt==2:
                answer+=1
    return answer
    
'''
nums=[1,2,7,6,4]

itertools의 combinations를 이용하여 nums원소를 3가지 뽑는 조합을 구한다.
cases= [(1, 2, 7), (1, 2, 6), (1, 2, 4), (1, 7, 6), (1, 7, 4), (1, 6, 4), (2, 7, 6), (2, 7, 4), (2, 6, 4), (7, 6, 4)]

cases의 각원소는 3개의 원소를 갖는 튜플이므로 이 세개의 원소를 합한 값을 원소로 갖는 리스트를 구한다.
three_sum_cases=[10, 9, 7, 14, 12, 11, 15, 13, 12, 17]

그리고 nums의 원소는 1이상의 자연수이다. 그래서 3개의 수의 합이 2가 나올 수가 없다.
그래서 짝수를 걸러내고 홀수 중에서 소수인 홀수를 찾는 방법을 택했다.
여기서 cnt는 three_sum_cases의 원소의 '약수의 개수'를 의미한다.
반복문을 이용하여 소수를 구하는 건데.. 소수의 정의는 약수가 1과 자기자신밖에 없는 수를 의미한다.
'''

   
