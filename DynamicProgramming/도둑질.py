def solution(money):
    if len(money)==0:
        return 0
    elif len(money)==1:
        return money[0]

    case1=[m for m in money] #첫번째 집을 털 수 잇다.
    case2=[m for m in money] #첫번째 집을 털 수 없다

    case1[1]=max(money[0], money[1])
    case2[0]=0

    for i in range(2, len(money)):
        case1[i]=max(case1[i-1], case1[i-2]+case1[i])
        case2[i]=max(case2[i-1], case2[i-2]+case2[i])

    return max(case1[-2], case2[-1])
