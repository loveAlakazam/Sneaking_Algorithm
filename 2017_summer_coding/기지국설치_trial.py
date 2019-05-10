def solution(n, stations, w):
    connected=[]
    for s in stations:
        if s==1:
            for i in range(s,s+w+1):
                connected.append(i)
        elif s==n:
            for i in range(s,s-w-1,-1):
                connected.append(i)
        else:
            for i in range(s-w,s+w+1):
                connected.append(i)
    #정렬
    connected.sort()
    print(connected)
    start,cnt=1,0
    while start<=n:
        if not start in connected:
            cnt+=1
            start+=(2*w)+1
        else:
            start+=1
    return cnt
