# to see question => https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3
def solution(a, b):
    '''
    나눠서 나머지가
    1:금
    2:토
    3:일
    4:월
    5:화
    6:수
    0:목
    '''
    weekDay={0:'THU', 1:'FRI', 2:'SAT', 3:'SUN', 4:'MON', 5:'TUE', 6:'WED'}
    MonthDay=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    days=0
    #a월이 5월이라면 1~4월까지 전체요일 계산
    for x in range(0,a):
        days+=MonthDay[x]
    days += b
    days %=7
    return weekDay[days]
    
    #answer = ''
    #return answer
