def solution(phone_number):
    phone_number=phone_number[::-1]
    answer=''.join([  str(p) if idx<4  else '*' for idx, p in enumerate(phone_number)][::-1])
    return answer
