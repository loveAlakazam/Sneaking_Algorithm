# https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3
def solution(phone_book):
    phone_book.sort() #문자열의 길이가 작은순으로 오름차순
    for phone in range(len(phone_book)-1): 
        standard=phone_book[phone] #기준점
        for compare in range(phone+1, len(phone_book)): #비교대상
            if standard in phone_book[compare]: #python에서의 strcmp와 같은 역할 (기준)이 (비교대상) 안에 있는지 확인
                return False
    return True
