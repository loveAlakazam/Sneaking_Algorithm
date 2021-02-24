# greedy - 4796 캠핑
import sys


def main(L, P, V):
    # 내가 캠핑장을 사용하는 기간: L
    # V라는 나의 휴가중 캠핑장을 사용할 수 있는 횟수: V/P
    # 내가 실제로 사용하는 기간 V/P*L
    option = 0
    if V % P > L:
        option = L
    else:
        option = V % P
    result = (V//P)*L + option
    return result


if __name__ == '__main__':
    idx = 1
    while True:
        L, P, V = map(int, sys.stdin.readline().split())
        if L == 0 and P == 0 and V == 0:
            break
        result = main(L, P, V)
        print('Case {idx}: {result}'.format(idx=idx, result=result))
        idx += 1
