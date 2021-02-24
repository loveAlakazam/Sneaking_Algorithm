# 설탕배달 - greedy 알고리즘
# 헐.. 식스샵 코딩테스트네...ㅎㅎ;;; 이거 망햇구먼...ㅎㅎ;

import sys


def main(N):
    cnt = 0
    while N > 0:
        if N % 5 == 0:
            N -= 5
            cnt += 1

        elif N % 3 == 0:
            N -= 3
            cnt += 1

        elif N > 5:
            N -= 5
            cnt += 1
        else:
            return -1
    return cnt


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    result = main(N)
    print(result)
