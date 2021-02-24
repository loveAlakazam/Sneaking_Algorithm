# greedy - 13305 주유소
# 제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소비용을 출력

import sys

MAX = 100000


def main(N, dist, price):
    d = [0] * MAX

    # 맨첫번째에서
    d[0] = price[0]*dist[0]
    min_price = price[0]
    for i in range(1, N):
        if price[i] < min_price:
            min_price = price[i]
        d[i] = d[i-1] + (min_price * dist[i])
    return d[N-1]


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    dist = [0]*MAX
    price = [0]*MAX
    for idx, p in enumerate(sys.stdin.readline().split()):
        dist[idx] = int(p)

    for idx, cost in enumerate(sys.stdin.readline().split()):
        price[idx] = int(cost)

    result = main(N, dist, price)
    print(result)
