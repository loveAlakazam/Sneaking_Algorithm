def solution(nums):
    answer=''
    if len(nums)==0: #nums에 아무것도 없다면 비어있는 문자열을 리턴
        return answer  
    elif len(nums)==1: #nums에 하나의 원소만 있다면, str(nums[0])를 리턴
        return str(nums[0])
    return str(int("".join(sorted(map(str,nums), key=lambda x:-float(x)/(10**len(x)-1)))))
