# https://programmers.co.kr/learn/courses/30/lessons/1845/solution_groups?language=python3&type=my
def solution(nums):
    # 가져갈 수 있는 포켓몬 수 (n/2)
    pick_up = int(len(nums)/2)

    #순수 종류 :중복된 종류 제외
    pure_type = list(set(nums))
    pure_type_len  = len(pure_type)

    if pure_type_len >= pick_up:
        return pick_up
    else : # pure_type_len < pick_up
        return pure_type_len
